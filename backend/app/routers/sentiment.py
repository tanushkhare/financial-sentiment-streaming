from fastapi import APIRouter
from app.schemas.sentiment import SentimentRequest, SentimentResponse
from app.services.sentiment_service import analyze_financial_sentiment

router = APIRouter(prefix="/api", tags=["Financial Sentiment Engine"])

@router.post("/analyze", response_model=SentimentResponse)
def analyze_sentiment(payload: SentimentRequest):
    return analyze_financial_sentiment(payload.text)