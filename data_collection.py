# cbmi/data_collection.py
import tweepy
import praw
from pytrends.request import TrendReq
from datetime import datetime
from .config import (
    CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET,
    REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
)

# Initialize API clients
X_CLIENT = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

REDDIT = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def get_x_posts(keywords, start_time, end_time, max_posts):
    """Collect posts from X using API v2."""
    posts = []
    for keyword in keywords:
        query = f"{keyword} lang:en"
        try:
            response = X_CLIENT.search_recent_tweets(
                query,
                start_time=start_time,
                end_time=end_time,
                max_results=min(100, max_posts - len(posts)),
                tweet_fields=["created_at", "author_id"],
                user_fields=["created_at"]
            )
            if response.data:
                for tweet in response.data:
                    user = X_CLIENT.get_user(id=tweet.author_id).data
                    posts.append({
                        "text": tweet.text,
                        "created_at": tweet.created_at,
                        "user": user.username,
                        "user_created": user.created_at,
                        "platform": "X"
                    })
                    if len(posts) >= max_posts:
                        return posts
        except Exception as e:
            print(f"Error fetching X posts: {e}")
    return posts

def get_reddit_posts(keywords, start_time, end_time, max_posts):
    """Collect posts from Reddit."""
    posts = []
    start_ts = datetime.strptime(start_time, "%Y-%m-%d").timestamp()
    end_ts = datetime.strptime(end_time, "%Y-%m-%d").timestamp()
    for keyword in keywords:
        try:
            for submission in REDDIT.subreddit("all").search(keyword, limit=None):
                if start_ts <= submission.created_utc <= end_ts:
                    posts.append({
                        "text": submission.title + " " + submission.selftext,
                        "created_at": datetime.fromtimestamp(submission.created_utc),
                        "user": submission.author.name if submission.author else "anonymous",
                        "user_created": datetime.fromtimestamp(submission.author.created_utc) if submission.author else None,
                        "platform": "Reddit"
                    })
                    if len(posts) >= max_posts:
                        return posts
        except Exception as e:
            print(f"Error fetching Reddit posts: {e}")
    return posts

def get_google_trends(keywords, start_time, end_time):
    """Fetch Google Trends data."""
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(keywords, timeframe=f"{start_time} {end_time}", geo="")
    return pytrends.interest_over_time()