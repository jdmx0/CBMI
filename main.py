# main.py
from cbmi.data_collection import get_x_posts, get_reddit_posts, get_google_trends
from cbmi.analysis import analyze_data
from cbmi.visualization import generate_plots
from cbmi.report import generate_pdf_report
from cbmi.config import MAX_SAMPLE_SIZE

def run_analysis(keywords, sample_size, start_time, end_time):
    """Execute the full Cerberus-Misinformation analysis pipeline."""
    sample_size = min(sample_size, MAX_SAMPLE_SIZE)
    max_per_platform = sample_size // 2

    print(f"Collecting up to {max_per_platform} posts from X and Reddit...")
    x_posts = get_x_posts(keywords, start_time, end_time, max_per_platform)
    reddit_posts = get_reddit_posts(keywords, start_time, end_time, max_per_platform)
    all_posts = x_posts + reddit_posts

    if not all_posts:
        print("No posts collected. Check API credentials or time frame.")
        return

    df, freq, sentiment_trend, analysis = analyze_data(all_posts)
    if df is None:
        print("Analysis failed due to no data.")
        return

    trends = get_google_trends(keywords, start_time, end_time)
    generate_plots(df, freq, sentiment_trend, trends, keywords)

    # Misinformation assessment
    spike_detected = freq.max() > freq.mean() * 3 if not freq.empty else False
    bot_activity = analysis["bots"] is not None and len(analysis["bots"]) > 0
    sentiment_shift = sentiment_trend.max() - sentiment_trend.min() > 0.5 if not sentiment_trend.empty else False
    correlation = df.groupby("date")["sentiment"].mean().corr(trends[keywords[0]]) if keywords[0] in trends else 0

    assessment = "Potential misinformation campaign detected" if spike_detected or bot_activity or sentiment_shift else "No clear signs of a misinformation campaign"
    reasoning = []
    if spike_detected:
        reasoning.append(f"A significant spike in post frequency (peak: {freq.max()}) was observed, exceeding three times the average ({freq.mean():.1f}).")
    if bot_activity:
        reasoning.append(f"Detected {len(analysis['bots'])} accounts created within 30 days posting frequently, suggesting possible bot activity.")
    if sentiment_shift:
        reasoning.append(f"A notable sentiment shift of {sentiment_trend.max() - sentiment_trend.min():.2f} occurred, which may indicate coordinated messaging.")
    reasoning.append(f"Social media activity correlates with Google Trends at {correlation:.2f}, suggesting {'aligned' if abs(correlation) > 0.5 else 'unaligned'} public interest.")
    reasoning = " ".join(reasoning) or "Activity appears organic with no significant anomalies."

    generate_pdf_report(df, keywords, start_time, end_time, freq, sentiment_trend, trends, analysis, assessment, reasoning)
    print("PDF report generated: report.pdf")

def main():
    """Collect user inputs and run analysis."""
    keywords = input("Enter keywords (space-separated): ").split()
    sample_size = int(input("Enter sample size (1-1000000): "))
    start_time = input("Enter start time (YYYY-MM-DD): ")
    end_time = input("Enter end time (YYYY-MM-DD): ")
    run_analysis(keywords, sample_size, start_time, end_time)

if __name__ == "__main__":
    main()