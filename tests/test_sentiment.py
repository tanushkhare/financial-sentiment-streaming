import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_bullish_sentiment():
    payload = {"ticker": "AAPL", "headline": "Apple reports record revenue growth and profits surge."}
    res = client.post("/api/v1/sentiment/analyze", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["sentiment_label"] == "BULLISH"
    assert data["polarity_score"] > 0

def test_bearish_sentiment():
    payload = {"ticker": "TSLA", "headline": "Tesla experiences sudden drop in deliveries amid recession fears."}
    res = client.post("/api/v1/sentiment/analyze", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["sentiment_label"] == "BEARISH"
    assert data["polarity_score"] < 0
