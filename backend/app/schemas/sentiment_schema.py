from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class NewsItem(BaseModel):
    ticker: str = Field(..., max_length=10, description="Asset ticker symbol (e.g. NVDA, AAPL, BTC)")
    headline: str = Field(..., min_length=10, description="Financial news headline or earnings summary")
    source: Optional[str] = Field(default="Bloomberg / SEC Wire")

class SentimentResponse(BaseModel):
    ticker: str
    headline_preview: str
    sentiment_label: str
    compound_score: float
    bullish_prob: float
    bearish_prob: float
    neutral_prob: float
    impact_assessment: str
    timestamp: datetime
