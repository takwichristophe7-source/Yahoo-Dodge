"""Lesson Models"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID
from enum import Enum


class DifficultyLevel(str, Enum):
    """Lesson difficulty levels"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class LessonCreate(BaseModel):
    """Lesson creation model"""
    title: str = Field(..., min_length=5, max_length=255)
    description: Optional[str] = None
    content: str = Field(..., min_length=10)
    category: str = Field(..., description="e.g., Password Safety, Phishing, etc.")
    difficulty_level: DifficultyLevel = DifficultyLevel.BEGINNER
    duration_minutes: Optional[int] = None
    video_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    xp_reward: int = Field(default=10, ge=0)


class LessonUpdate(BaseModel):
    """Lesson update model"""
    title: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    difficulty_level: Optional[DifficultyLevel] = None
    duration_minutes: Optional[int] = None
    video_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    xp_reward: Optional[int] = None
    is_published: Optional[bool] = None


class LessonResponse(BaseModel):
    """Lesson response model"""
    id: UUID
    title: str
    description: Optional[str]
    content: str
    category: str
    difficulty_level: str
    duration_minutes: Optional[int]
    video_url: Optional[str]
    thumbnail_url: Optional[str]
    xp_reward: int
    is_published: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class LessonProgressResponse(BaseModel):
    """Lesson progress response"""
    lesson_id: UUID
    lesson_title: str
    is_completed: bool
    progress_percentage: int
    started_at: datetime
    completed_at: Optional[datetime]
