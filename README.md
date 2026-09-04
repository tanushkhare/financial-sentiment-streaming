# ⚡ Financial Sentiment Streaming

[![Live Web Demo](https://img.shields.io/badge/Live_App-Vercel-black?style=for-the-badge&logo=vercel)](https://financial-sentiment-streaming-web.vercel.app)
[![Portfolio Hub](https://img.shields.io/badge/Portfolio_Hub-Live-blue?style=for-the-badge)](https://portfolio-showcase-hub-web11.vercel.app)

🔗 **Production URL:** [https://financial-sentiment-streaming-web.vercel.app](https://financial-sentiment-streaming-web.vercel.app)  
🌐 **Showcase Hub:** [https://portfolio-showcase-hub-web11.vercel.app](https://portfolio-showcase-hub-web11.vercel.app)

---

## 📌 Architectural Overview
ProsusAI/FinBERT market sentiment classifier streaming polarity and volatility indicators across financial news feeds via Server-Sent Events (SSE).

---

## 🛠️ Technology Ecosystem
* **Core Architecture:** ProsusAI/FinBERT, FastAPI SSE, Transformers, Plotly
* **Testing & Quality:** PyTest, Automated GitHub Actions CI
* **Deployment:** Vercel Edge Runtime

---

## 🛡️ Production Standards
* **Domain Transformer Weights:** Aligned to FinBERT architecture rather than general-purpose lexicons.
* **Event Streaming:** Built-in Server-Sent Events (SSE) route for real-time client consumption.
* **Probabilistic Calibration:** Emits confidence scores alongside polarity judgments.

---

## 🚀 API Contracts
```http
POST /api/v1/sentiment/score
Request:
{
  "headline": "Semiconductor manufacturer reports quarterly operating margin growth exceeding 34%..."
}

Response (200 OK):
{
  "polarity": "BULLISH",
  "confidence": 0.964,
  "impact": "POSITIVE",
  "model": "ProsusAI/finbert"
}

GET /health
Response: {"status": "healthy"}

💻 Local Quickstart

Bash

pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
pytest tests/ -v