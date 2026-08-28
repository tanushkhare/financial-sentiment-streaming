from fastapi import APIRouter
from backend.app.schemas.sentiment_schema import SentimentRequest, SentimentResponse
from backend.app.services.sentiment_service import sentiment_service

router = APIRouter(prefix="/api/v1/sentiment", tags=["Financial Sentiment Engine"])

@router.post("/analyze", response_model=SentimentResponse)
async def analyze_sentiment(payload: SentimentRequest):
    result = sentiment_service.evaluate_sentiment(payload.ticker, payload.headline)
    return SentimentResponse(**result)
