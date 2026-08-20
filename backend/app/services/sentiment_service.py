def analyze_financial_sentiment(text: str):
    lower_text = text.lower()
    
    # Financial sentiment heuristics & mock NLP classification
    bullish_keywords = ["surge", "growth", "profit", "bullish", "record high", "beat estimates", "rally"]
    bearish_keywords = ["drop", "loss", "crash", "bearish", "recession", "missed", "decline", "inflation"]
    
    bullish_matches = sum(1 for word in bullish_keywords if word in lower_text)
    bearish_matches = sum(1 for word in bearish_keywords if word in lower_text)
    
    if bullish_matches > bearish_matches:
        sentiment = "Bullish (Positive)"
        confidence = 0.89
        polarity = 0.75
    elif bearish_matches > bullish_matches:
        sentiment = "Bearish (Negative)"
        confidence = 0.91
        polarity = -0.80
    else:
        sentiment = "Neutral"
        confidence = 0.75
        polarity = 0.00
        
    return {
        "text": text,
        "sentiment": sentiment,
        "confidence": confidence,
        "polarity_score": polarity
    }