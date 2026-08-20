import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_bullish_sentiment():
    payload = {"ticker": "NVDA", "headline": "Nvidia reports record revenue and beats quarterly earnings estimates."}
    res = client.post("/api/v1/sentiment/analyze", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["sentiment_label"] == "BULLISH"
    assert data["compound_score"] > 0.0

def test_bearish_sentiment():
    payload = {"ticker": "XYZ", "headline": "Company faces regulatory probe as revenue declined sharply after missed estimates."}
    res = client.post("/api/v1/sentiment/analyze", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["sentiment_label"] == "BEARISH"
    assert data["compound_score"] < 0.0
