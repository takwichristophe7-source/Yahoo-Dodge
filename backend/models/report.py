"""Report Models"""
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from datetime import datetime, date
from uuid import UUID
from enum import Enum


class ScamType(str, Enum):
    """Types of scams"""
    PHONE = "phone"
    MOBILE_MONEY = "mobile_money"
    WEBSITE = "website"
    JOB = "job"
    ROMANCE = "romance"
    INVESTMENT = "investment"
    SOCIAL_MEDIA = "social_media"


class SeverityLevel(str, Enum):
    """Severity levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ReportStatus(str, Enum):
    """Report status"""
    PENDING = "pending"
    REVIEWED = "reviewed"
    APPROVED = "approved"
    REJECTED = "rejected"


class ScamReportCreate(BaseModel):
    """Scam report creation model"""
    scam_type: ScamType
    description: str = Field(..., min_length=10, max_length=2000)
    location: Optional[str] = None
    phone_number: Optional[str] = None
    website_url: Optional[str] = None
    reported_date: Optional[date] = None
    severity: SeverityLevel = SeverityLevel.MEDIUM


class ScamReportResponse(BaseModel):
    """Scam report response model"""
    id: UUID
    scam_type: str
    description: str
    location: Optional[str]
    phone_number: Optional[str]
    website_url: Optional[str]
    severity: str
    status: str
    is_verified: bool
    is_approved: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PhoneReportCreate(BaseModel):
    """Phone report creation model"""
    phone_number: str = Field(..., min_length=7)
    scam_risk_level: Optional[str] = "unknown"


class PhoneReportResponse(BaseModel):
    """Phone report response model"""
    phone_number: str
    scam_risk_level: str
    report_count: int
    community_rating: Optional[float]
    last_reported: Optional[datetime]
    created_at: datetime

    class Config:
        from_attributes = True
