# gui.py: Simple Tkinter GUI for CBMI input collection
import tkinter as tk
from tkinter import messagebox
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

def start_analysis():
    """Collect inputs from GUI and run analysis."""
    try:
        keywords = keywords_entry.get().split()
        sample_size = int(sample_size_entry.get())
        if not (1 <= sample_size <= 1000000):
            raise ValueError("Sample size must be between 1 and 1,000,000.")
        start_time = start_time_entry.get()
        end_time = end_time_entry.get()
        # Basic date validation
        from datetime import datetime
        datetime.strptime(start_time, "%Y-%m-%d")
        datetime.strptime(end_time, "%Y-%m-%d")
        run_analysis(keywords, sample_size, start_time, end_time)
        messagebox.showinfo("Success", "Report generated: report.pdf")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the GUI window
root = tk.Tk()
root.title("CBMI - Cerberus-Misinformation")
root.geometry("400x200")

# Input fields
tk.Label(root, text="Keywords (space-separated):").grid(row=0, column=0, padx=5, pady=5)
keywords_entry = tk.Entry(root, width=40)
keywords_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Sample Size (1-1,000,000):").grid(row=1, column=0, padx=5, pady=5)
sample_size_entry = tk.Entry(root, width=40)
sample_size_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Start Time (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
start_time_entry = tk.Entry(root, width=40)
start_time_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="End Time (YYYY-MM-DD):").grid(row=3, column=0, padx=5, pady=5)
end_time_entry = tk.Entry(root, width=40)
end_time_entry.grid(row=3, column=1, padx=5, pady=5)

# Start button
tk.Button(root, text="Start Analysis", command=start_analysis).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()