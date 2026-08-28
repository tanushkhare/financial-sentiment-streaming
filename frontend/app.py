import streamlit as st
import requests
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Financial Sentiment Streaming", layout="wide")

st.title("📈 Real-Time Financial Sentiment & Market Intelligence")
st.markdown("Analyze equity headlines, SEC filings, and financial news for polarity and market volatility signals.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Market Headline Ingest")
    ticker = st.text_input("Ticker Symbol", value="NVDA")
    headline = st.text_area("Financial News Headline", value="NVIDIA reports record quarterly revenue surging 120% year-over-year, beating analyst expectations.", height=120)

    if st.button("Evaluate Sentiment Polarity", type="primary"):
        with st.spinner("Extracting market sentiment signals..."):
            try:
                res = requests.post("http://localhost:8000/api/v1/sentiment/analyze", json={"ticker": ticker, "headline": headline}, timeout=5)
                if res.status_code == 200:
                    st.session_state["p10_result"] = res.json()
                    st.success("Analysis Complete!")
                else:
                    st.error(f"API Error: {res.text}")
            except Exception:
                st.warning("Backend offline. Running client-side simulation.")
                st.session_state["p10_result"] = {
                    "ticker": ticker.upper(),
                    "headline": headline,
                    "sentiment_label": "BULLISH",
                    "polarity_score": 0.85,
                    "confidence": 0.92,
                    "volatility_impact": "High Upside Volatility",
                    "key_drivers": ["Bullish catalyst: 'record'", "Bullish catalyst: 'surging'", "Bullish catalyst: 'beating'"]
                }

with col2:
    if "p10_result" in st.session_state:
        res = st.session_state["p10_result"]
        st.subheader(f"Sentiment Profile: {res['ticker']}")
        
        m1, m2 = st.columns(2)
        m1.metric("Sentiment Label", res["sentiment_label"])
        m2.metric("Polarity Score", f"{res['polarity_score']:+.2f}", delta=res["volatility_impact"])
        
        st.markdown("#### Catalysts & Drivers")
        for driver in res["key_drivers"]:
            st.info(f"📊 {driver}")
