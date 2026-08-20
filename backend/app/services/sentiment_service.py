from typing import Dict, Any, List
import math

class FinancialSentimentEngine:
    def __init__(self):
        self.bullish_keywords = ["soars", "record", "growth", "outperform", "dividend", "surge", "beats", "rally", "profit"]
        self.bearish_keywords = ["plunges", "missed", "layoffs", "downgrade", "losses", "recession", "drop", "investigation", "decline"]

    def score_headline(self, ticker: str, headline: str) -> Dict[str, Any]:
        text_lower = headline.lower()
        bull_hits = sum(1 for k in self.bullish_keywords if k in text_lower)
        bear_hits = sum(1 for k in self.bearish_keywords if k in text_lower)
        
        raw_score = (bull_hits - bear_hits) / max(bull_hits + bear_hits, 1)
        sentiment_score = round(math.tanh(raw_score * 1.5), 3)
        
        label = "BULLISH" if sentiment_score > 0.15 else "BEARISH" if sentiment_score < -0.15 else "NEUTRAL"
        confidence = round(abs(sentiment_score) if label != "NEUTRAL" else 0.70, 3)
        
        return {
            "ticker": ticker.upper(),
            "headline": headline,
            "sentiment_label": label,
            "sentiment_score": sentiment_score,
            "confidence": confidence,
            "trading_signal": "BUY / ACCUMULATE" if label == "BULLISH" else "SELL / HEDGE" if label == "BEARISH" else "HOLD"
        }

sentiment_engine = FinancialSentimentEngine()
