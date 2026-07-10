"""Quiz Models"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID
from enum import Enum


class QuestionType(str, Enum):
    """Question types"""
    MULTIPLE_CHOICE = "multiple_choice"
    TRUE_FALSE = "true_false"


class QuizQuestionCreate(BaseModel):
    """Quiz question creation model"""
    lesson_id: UUID
    question_text: str = Field(..., min_length=5)
    question_type: QuestionType = QuestionType.MULTIPLE_CHOICE
    option_a: Optional[str] = None
    option_b: Optional[str] = None
    option_c: Optional[str] = None
    option_d: Optional[str] = None
    correct_answer: str = Field(..., regex="^[A-D]$")
    explanation: Optional[str] = None
    xp_reward: int = Field(default=5, ge=0)


class QuizQuestionResponse(BaseModel):
    """Quiz question response model"""
    id: UUID
    question_text: str
    question_type: str
    option_a: Optional[str]
    option_b: Optional[str]
    option_c: Optional[str]
    option_d: Optional[str]
    explanation: Optional[str]
    xp_reward: int

    class Config:
        from_attributes = True


class QuizAnswerSubmit(BaseModel):
    """Quiz answer submission model"""
    question_id: UUID
    user_answer: str = Field(..., regex="^[A-D]$")


class QuizResultResponse(BaseModel):
    """Quiz result response model"""
    question_id: UUID
    user_answer: str
    correct_answer: str
    is_correct: bool
    xp_earned: int
    explanation: Optional[str]


class QuizSubmissionResponse(BaseModel):
    """Quiz submission response"""
    lesson_id: UUID
    total_questions: int
    correct_answers: int
    score_percentage: float
    total_xp_earned: int
    results: list[QuizResultResponse]
