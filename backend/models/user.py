"""User Models"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from uuid import UUID


class UserBase(BaseModel):
    """Base user model"""
    email: EmailStr
    full_name: Optional[str] = None
    username: Optional[str] = None


class UserCreate(UserBase):
    """User creation model"""
    password: str = Field(..., min_length=8, description="Password must be at least 8 characters")


class UserUpdate(BaseModel):
    """User update model"""
    full_name: Optional[str] = None
    username: Optional[str] = None
    bio: Optional[str] = None
    phone_number: Optional[str] = None
    profile_picture_url: Optional[str] = None


class UserResponse(UserBase):
    """User response model"""
    id: UUID
    protection_score: int = 0
    cyber_xp: int = 0
    is_active: bool = True
    last_login: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserProfile(UserResponse):
    """Extended user profile"""
    bio: Optional[str] = None
    phone_number: Optional[str] = None
    profile_picture_url: Optional[str] = None
    country: str = "Cameroon"
    lessons_completed: int = 0
    quizzes_completed: int = 0
    reports_submitted: int = 0
    badges_earned: int = 0


class PasswordChange(BaseModel):
    """Password change model"""
    current_password: str
    new_password: str = Field(..., min_length=8)
    confirm_password: str = Field(..., min_length=8)

    class Config:
        json_schema_extra = {
            "example": {
                "current_password": "OldPassword123!",
                "new_password": "NewPassword456!",
                "confirm_password": "NewPassword456!"
            }
        }
