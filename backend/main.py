"""Yahoo Dodge - Main FastAPI Application"""
import os
from contextlib import asynccontextmanager
from typing import Optional
from datetime import datetime

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZIPMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import routers
from api.auth import router as auth_router
from api.users import router as users_router
from api.shield import router as shield_router
from api.reports import router as reports_router
from api.lessons import router as lessons_router
from api.quizzes import router as quizzes_router
from api.leaderboard import router as leaderboard_router
from api.admin import router as admin_router


# Lifespan context manager for startup/shutdown events
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application startup and shutdown"""
    # Startup
    print("🛡️ Yahoo Dodge is starting up...")
    print(f"Environment: {os.getenv('ENVIRONMENT', 'development')}")
    yield
    # Shutdown
    print("🛡️ Yahoo Dodge is shutting down...")


# Create FastAPI application
app = FastAPI(
    title="Yahoo Dodge API",
    description="AI-powered cybersecurity and digital citizenship platform for Cameroon",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
    lifespan=lifespan
)

# Add middleware
app.add_middleware(GZIPMiddleware, minimum_size=1000)

# Configure CORS
cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:8000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Global exception handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "message": exc.detail,
            "timestamp": datetime.utcnow().isoformat()
        },
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """Handle general exceptions"""
    print(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "An internal server error occurred",
            "timestamp": datetime.utcnow().isoformat()
        },
    )


# Health check endpoints
@app.get("/", tags=["Health"])
async def root():
    """Root endpoint - Welcome message"""
    return {
        "message": "🛡️ Welcome to Yahoo Dodge API",
        "version": "1.0.0",
        "status": "operational",
        "description": "AI-powered cybersecurity platform for Cameroon"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "yahoo-dodge-api"
    }


@app.get("/api/health", tags=["Health"])
async def api_health_check():
    """API health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }


# Include routers
app.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])
app.include_router(users_router, prefix="/api/users", tags=["Users"])
app.include_router(shield_router, prefix="/api/shield", tags=["AI Shield"])
app.include_router(reports_router, prefix="/api/reports", tags=["Reports"])
app.include_router(lessons_router, prefix="/api/lessons", tags=["Learning Center"])
app.include_router(quizzes_router, prefix="/api/quizzes", tags=["Quizzes"])
app.include_router(leaderboard_router, prefix="/api/leaderboard", tags=["Leaderboard"])
app.include_router(admin_router, prefix="/api/admin", tags=["Admin"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("BACKEND_PORT", 8000)),
        reload=os.getenv("ENVIRONMENT") == "development",
        log_level="info"
    )
