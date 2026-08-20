from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import sentiment

app = FastAPI(
    title="Financial Sentiment Streaming API",
    version="1.0.0",
    description="Real-time financial NLP sentiment analysis microservice."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sentiment.router)

@app.get("/")
def read_root():
    return {"message": "Financial Sentiment Streaming Backend is online!"}