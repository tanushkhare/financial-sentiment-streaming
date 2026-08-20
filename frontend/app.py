import streamlit as st
import requests

st.title("📈 Financial Sentiment Streaming & Analytics")
st.write("Analyze real-time market news headlines, earnings reports, or financial transcripts for automated sentiment scoring.")

headline = st.text_area("Enter Financial Text / Headline:", "Q3 earnings report shows massive profit surge and record growth beating estimates.")

if st.button("Analyze Sentiment"):
    if headline.strip():
        try:
            response = requests.post("http://127.0.0.1:8000/api/analyze", json={"text": headline})
            if response.status_code == 200:
                data = response.json()
                st.success("Analysis Complete!")
                st.metric(label="Detected Sentiment", value=data["sentiment"])
                st.metric(label="Model Confidence", value=f"{data['confidence'] * 100}%")
                st.metric(label="Polarity Score", value=data["polarity_score"])
            else:
                st.error("Failed to fetch sentiment analysis from backend.")
        except Exception as e:
            st.error(f"Connection error: {e}")
    else:
        st.warning("Please enter valid text to analyze.")