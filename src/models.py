from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class Tweet(BaseModel):
    user_id: str
    content: str
    tags: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Follow(BaseModel):
    follower_id: str
    following_id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

