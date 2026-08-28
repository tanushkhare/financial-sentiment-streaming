from pydantic import BaseModel, Field
from typing import List, Optional

class SentimentRequest(BaseModel):
    ticker: str = Field(default="NVDA", min_length=1, max_length=10, description="Asset ticker symbol")
    headline: str = Field(..., min_length=5, description="Financial news headline or earnings report snippet")

class SentimentResponse(BaseModel):
    ticker: str
    headline: str
    sentiment_label: str
    polarity_score: float
    confidence: float
    volatility_impact: str
    key_drivers: List[str]
