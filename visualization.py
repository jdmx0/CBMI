# cbmi/visualization.py
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend for iOS compatibility
import matplotlib.pyplot as plt

def generate_plots(df, freq, sentiment_trend, trends, keywords):
    """Create plots for frequency, sentiment, and trends comparison."""
    # Post frequency
    plt.figure(figsize=(10, 6))
    freq.plot(kind="line", title="Post Frequency Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Posts")
    plt.savefig("frequency.png")
    plt.close()

    # Sentiment trend
    plt.figure(figsize=(10, 6))
    sentiment_trend.plot(kind="line", title="Sentiment Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Average Sentiment")
    plt.savefig("sentiment.png")
    plt.close()

    # Social media vs Google Trends
    freq_df = freq.reset_index(name="post_count")
    freq_df["date"] = pd.to_datetime(freq_df["date"])
    trends.index = pd.to_datetime(trends.index)
    combined = pd.merge(freq_df, trends, left_on="date", right_index=True, how="outer")
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.plot(combined["date"], combined["post_count"], "b-", label="Post Count")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Post Count", color="b")
    ax1.tick_params(axis="y", labelcolor="b")
    ax2 = ax1.twinx()
    ax2.plot(combined["date"], combined[keywords[0]], "r-", label="Trend Interest")
    ax2.set_ylabel("Google Trends Interest", color="r")
    ax2.tick_params(axis="y", labelcolor="r")
    plt.title("Social Media Activity vs Google Trends")
    plt.savefig("trends.png")
    plt.close()