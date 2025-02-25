# CBMI - Cerberus-Misinformation

## Overview

CBMI (Cerberus-Misinformation) is a Python-based tool designed to analyze social media activity on X and Reddit, helping you identify potential misinformation campaigns. It pulls posts based on your keywords, crunches the data with sentiment analysis, tracks user behavior, and cross-references it with Google Trends to give you a fuller picture. The output? A neat PDF report packed with insights—think sentiment trends, frequency charts, and a quick “is this fishy?” assessment—all backed by visuals you can actually use.

### What It Does Under the Hood

Here’s the technical rundown of how CBMI works:

- **Data Collection**: 
  - Hits X’s API (v2 via `tweepy`) and Reddit’s API (via `praw`) to grab posts matching your keywords within a specified time frame. It respects the free tier limits, capping at 10,000 posts total (split evenly between platforms).
  - Pulls Google Trends data (via `pytrends`) to see how your keywords are trending in search interest over the same period.

- **Analysis**: 
  - Runs sentiment analysis on each post using `TextBlob`—scores range from -1 (negative) to 1 (positive)—and tracks daily averages to spot mood swings.
  - Counts post frequency per day with `pandas` to catch sudden spikes that might signal a coordinated push.
  - Extracts the top 10 keywords from posts using `scikit-learn`’s `CountVectorizer` for a peek at what’s buzzing.
  - Checks user behavior—flags accounts less than 30 days old posting more than 5 times as potential bots.

- **Visualization**: 
  - Generates three plots with `matplotlib` (using the `Agg` backend for file-only output, handy for iOS or headless systems):
    - Post frequency over time.
    - Sentiment trend over time.
    - A dual-axis chart comparing social media posts to Google Trends interest.

- **Misinformation Detection**: 
  - Looks for red flags like frequency spikes (3x the average), big sentiment shifts (>0.5), or bot-like activity. Correlates social media sentiment with Google Trends to see if chatter aligns with public curiosity.
  - Wraps it up in an “Intelligence Brief” with a verdict (e.g., “Potential misinformation detected”) and reasoning tied to the data.

- **Reporting**: 
  - Compiles everything into a PDF via `reportlab`, including raw stats, plots, and the brief. You also get the raw `.png` plot files as a bonus.

It’s not rocket science, but it’s built to cut through the noise and give you something actionable—whether you’re tracking rumors, scams, or just curious about what’s trending.

## Setup

Before you can use CBMI, you’ll need to set it up. Here’s the step-by-step:

### Prerequisites
- **Python**: Version 3.9 or higher. Check with `python --version`.
- **API Access**: You’ll need keys for X and Reddit (details below).
- **A Terminal**: For CLI usage or initial setup.
- **Optional (GUI)**: A desktop OS (Windows, Mac, Linux) with Tkinter installed for the GUI version.

### Installation
1. **Clone the Repository**:
   - Grab the code from GitHub:
     ```bash
     git clone https://github.com/yourusername/cbmi.git
     cd cbmi
     ```

2. **Install Dependencies**:
   - Run this in your terminal to get all the Python libraries CBMI needs:
     ```bash
     pip install -r requirements.txt
     ```
   - This pulls in `tweepy`, `praw`, `textblob`, `pandas`, `matplotlib`, `reportlab`, `pytrends`, and `scikit-learn`. On some systems, you might need `pip install tk` for the GUI.

3. **Configure API Credentials**:
   - Open `cbmi/config.py` in a text editor (e.g., Notepad, VS Code).
   - Add your API keys:
     - **X**: Get these from the [X Developer Portal](https://developer.twitter.com):
       - `CONSUMER_KEY`
       - `CONSUMER_SECRET`
       - `ACCESS_TOKEN`
       - `ACCESS_TOKEN_SECRET`
     - **Reddit**: Create an app at [Reddit Apps](https://www.reddit.com/prefs/apps):
       - `REDDIT_CLIENT_ID`
       - `REDDIT_CLIENT_SECRET`
       - Leave `REDDIT_USER_AGENT` as `"cbmi"` or tweak it if you want.
   - Save the file. These keys let CBMI talk to X and Reddit—without them, you’ll get nada.

## Usage

CBMI offers two ways to run it: **Command-Line Interface (CLI)** for quick, no-frills analysis, and **Graphical User Interface (GUI)** for a point-and-click experience. Here’s how to use both.

### CLI Usage

The CLI is perfect if you’re comfortable with a terminal and want to get straight to it.

#### How to Run
1. **Navigate to the Folder**:
   - In your terminal, move to the `cbmi` directory:
     ```bash
     cd path/to/cbmi
     ```

2. **Launch the Script**:
   - Type and hit Enter:
     ```bash
     python main.py
     ```

3. **Answer the Prompts**:
   - **Keywords**: Type space-separated words (e.g., `election fraud`). Hit Enter.
   - **Sample Size**: Enter a number between 1 and 1,000,000 (e.g., `500`). It’s capped at 10,000 due to API limits. Hit Enter.
   - **Start Time**: Enter a date like `2023-10-01` (YYYY-MM-DD). Must be within X’s 7-day free API window. Hit Enter.
   - **End Time**: Enter a later date like `2023-10-07`. Hit Enter.

4. **Watch It Work**:
   - The terminal shows progress: “Collecting up to 250 posts from X and Reddit...” then “PDF report generated: report.pdf”.
   - It grabs posts, analyzes them, and saves the report.

5. **Check the Output**:
   - Find `report.pdf` in the `cbmi` folder, along with `.png` plot files (`frequency.png`, `sentiment.png`, `trends.png`).
   - Open the PDF to see your analysis.

#### Example
```bash
$ python main.py
Enter keywords (space-separated): vaccine conspiracy
Enter sample size (1-1000000): 1000
Enter start time (YYYY-MM-DD): 2023-10-01
Enter end time (YYYY-MM-DD): 2023-10-07
Collecting up to 500 posts from X and Reddit...
PDF report generated: report.pdf