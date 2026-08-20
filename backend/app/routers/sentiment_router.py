from fastapi import APIRouter, HTTPException
from backend.app.schemas.sentiment_schema import NewsItem, SentimentResponse
from backend.app.services.sentiment_service import sentiment_engine

router = APIRouter(prefix="/api/v1/sentiment", tags=["Financial Market Sentiment Engine"])

@router.post("/analyze", response_model=SentimentResponse)
async def score_news_stream(payload: NewsItem):
    try:
        result = sentiment_engine.analyze_headline(payload.ticker, payload.headline)
        return SentimentResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
