from typing import Dict, Any, List

class FinancialSentimentService:
    def __init__(self):
        self.bullish_keywords = ["surge", "jump", "record", "growth", "beat", "profit", "bullish", "rally", "exceed", "upgrade", "gain", "revenue"]
        self.bearish_keywords = ["drop", "fall", "plunge", "loss", "miss", "recession", "bearish", "inflation", "risk", "downgrade", "deficit", "slump"]

    def evaluate_sentiment(self, ticker: str, headline: str) -> Dict[str, Any]:
        text_lower = headline.lower()
        bullish_hits = [w for w in self.bullish_keywords if w in text_lower]
        bearish_hits = [w for w in self.bearish_keywords if w in text_lower]

        b_score = len(bullish_hits)
        r_score = len(bearish_hits)
        
        if b_score > r_score:
            label = "BULLISH"
            polarity = round(min(0.95, 0.4 + (b_score * 0.2)), 2)
            confidence = round(min(0.98, 0.65 + (b_score * 0.1)), 2)
            impact = "High Upside Volatility" if b_score >= 2 else "Moderate Bullish Drift"
            drivers = [f"Bullish catalyst: '{w}'" for w in bullish_hits]
        elif r_score > b_score:
            label = "BEARISH"
            polarity = round(max(-0.95, -0.4 - (r_score * 0.2)), 2)
            confidence = round(min(0.98, 0.65 + (r_score * 0.1)), 2)
            impact = "Downside Risk Exposure" if r_score >= 2 else "Mild Bearish Pressure"
            drivers = [f"Risk indicator: '{w}'" for w in bearish_hits]
        else:
            label = "NEUTRAL"
            polarity = 0.05
            confidence = 0.72
            impact = "Low Market Impact / Consolidation"
            drivers = ["Balanced macroeconomic signals"]

        return {
            "ticker": ticker.upper(),
            "headline": headline,
            "sentiment_label": label,
            "polarity_score": polarity,
            "confidence": confidence,
            "volatility_impact": impact,
            "key_drivers": drivers
        }

sentiment_service = FinancialSentimentService()
