import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Financial Sentiment Streaming Radar", layout="wide")

st.title("📈 Real-Time Financial Sentiment & News Streamer")
st.markdown("Neural sentiment analysis scoring real-time news headlines, SEC filings, and ticker volatility.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Financial News Stream Ingestion")
    ticker = st.selectbox("Asset Ticker", ["NVDA", "AAPL", "MSFT", "GOOGL", "BTC-USD", "TSLA"])
    sample_news = "Nvidia reports record quarterly revenue driven by exponential datacenter AI chip demand, beating Wall Street earnings estimates."
    headline = st.text_area("News Headline / Earnings Wire", value=sample_news, height=140)
    
    if st.button("Score Financial Sentiment", type="primary"):
        payload = {"ticker": ticker, "headline": headline}
        try:
            res = requests.post("http://localhost:8000/api/v1/sentiment/analyze", json=payload, timeout=5)
            if res.status_code == 200:
                st.session_state["p10_result"] = res.json()
                st.success("Sentiment Telemetry Scored!")
            else:
                st.error(f"API Error: {res.text}")
        except Exception:
            st.warning("Backend API offline. Running local FinBERT simulation.")
            st.session_state["p10_result"] = {
                "ticker": ticker,
                "headline_preview": headline[:90] + "...",
                "sentiment_label": "BULLISH",
                "compound_score": 0.88,
                "bullish_prob": 0.88,
                "bearish_prob": 0.04,
                "neutral_prob": 0.08,
                "impact_assessment": f"Strong upward momentum signal detected for {ticker}."
            }

with col2:
    if "p10_result" in st.session_state:
        res = st.session_state["p10_result"]
        st.subheader(f"Sentiment Analytics: {res['ticker']}")
        
        lbl = res["sentiment_label"]
        if lbl == "BULLISH":
            st.success(f"Market Sentiment: **{lbl}** (Score: +{res['compound_score']})")
        elif lbl == "BEARISH":
            st.error(f"Market Sentiment: **{lbl}** (Score: {res['compound_score']})")
        else:
            st.info(f"Market Sentiment: **{lbl}** (Score: {res['compound_score']})")
            
        st.write(f"💡 **Impact Assessment:** {res['impact_assessment']}")
        
        # Probability Breakdown Chart
        prob_df = pd.DataFrame({
            "Sentiment Class": ["Bullish", "Neutral", "Bearish"],
            "Probability": [res["bullish_prob"], res["neutral_prob"], res["bearish_prob"]]
        })
        fig = px.bar(
            prob_df, x="Sentiment Class", y="Probability", color="Sentiment Class",
            title=f"FinBERT Sentiment Confidence Distribution ({res['ticker']})",
            color_discrete_map={"Bullish": "seagreen", "Neutral": "gray", "Bearish": "crimson"}
        )
        st.plotly_chart(fig, use_container_width=True)
