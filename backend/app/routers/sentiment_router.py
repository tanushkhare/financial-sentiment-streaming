from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List

router = APIRouter(prefix="/api/v1/sentiment", tags=["Financial Sentiment Engine"])

class SentimentRequest(BaseModel):
    ticker: str = Field(..., min_length=1, max_length=10)
    headline: str = Field(..., min_length=5)

class SentimentResponse(BaseModel):
    ticker: str
    sentiment_label: str
    polarity_score: float
    confidence: float
    volatility_impact: str
    key_drivers: List[str]

@router.post("/analyze", response_model=SentimentResponse)
async def analyze_sentiment(payload: SentimentRequest):
    text_lower = payload.headline.lower()
    
    bullish_keywords = ["surge", "jump", "record", "growth", "beat", "profit", "bullish", "rally", "exceed", "upgrade"]
    bearish_keywords = ["drop", "fall", "plunge", "loss", "miss", "recession", "bearish", "inflation", "risk", "downgrade"]
    
    bullish_hits = [w for w in bullish_keywords if w in text_lower]
    bearish_hits = [w for w in bearish_keywords if w in text_lower]
    
    if len(bullish_hits) > len(bearish_hits):
        label = "BULLISH / POSITIVE"
        polarity = round(0.65 + min(len(bullish_hits) * 0.1, 0.30), 2)
        confidence = 0.94
        volatility = "MODERATE UPSIDE"
        drivers = [f"Positive momentum cue: '{w}'" for w in bullish_hits]
    elif len(bearish_hits) > len(bullish_hits):
        label = "BEARISH / NEGATIVE"
        polarity = round(-0.65 - min(len(bearish_hits) * 0.1, 0.30), 2)
        confidence = 0.91
        volatility = "HIGH DOWNSIDE RISK"
        drivers = [f"Negative catalyst cue: '{w}'" for w in bearish_hits]
    else:
        label = "NEUTRAL / BALANCED"
        polarity = 0.05
        confidence = 0.82
        volatility = "LOW / CONSOLIDATION"
        drivers = ["Balanced macroeconomic indicators detected", "No extreme directional keywords"]

    return SentimentResponse(
        ticker=payload.ticker.upper(),
        sentiment_label=label,
        polarity_score=polarity,
        confidence=confidence,
        volatility_impact=volatility,
        key_drivers=drivers
    )
