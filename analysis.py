# cbmi/analysis.py
from textblob import TextBlob
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from datetime import datetime

def analyze_sentiment(text):
    """Score text sentiment from -1 (negative) to 1 (positive)."""
    return TextBlob(text).sentiment.polarity

def analyze_data(posts):
    """Analyze posts for sentiment, frequency, keywords, and behavior."""
    if not posts:
        return None, None, None, None

    df = pd.DataFrame(posts)
    df["sentiment"] = df["text"].apply(analyze_sentiment)
    df["date"] = pd.to_datetime(df["created_at"]).dt.date

    # Frequency of posts per day
    freq = df.groupby("date").size()

    # Average sentiment per day
    sentiment_trend = df.groupby("date")["sentiment"].mean()

    # Top keywords in posts
    vectorizer = CountVectorizer(stop_words="english", max_features=10)
    X = vectorizer.fit_transform(df["text"])
    keywords_freq = dict(zip(vectorizer.get_feature_names_out(), X.sum(axis=0).A1))

    # User activity and bot detection
    df["account_age_days"] = (datetime.now() - pd.to_datetime(df["user_created"])).dt.days
    user_activity = df.groupby("user").size().sort_values(ascending=False).head(10)
    bot_suspects = df[df["account_age_days"] < 30].groupby("user").size()
    bots = bot_suspects[bot_suspects > 5] if not bot_suspects.empty else None

    return df, freq, sentiment_trend, {"keywords": keywords_freq, "users": user_activity, "bots": bots}