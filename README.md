###

# CBMI
# Misinformation analysis tool.

CBMI (Cerberus-Misinformation) - A solid Python tool that digs into X and Reddit posts to spot misinformation campaigns. It blends sentiment analysis, user behavior checks, and Google Trends data to deliver clear PDF reports with practical insights and visuals. Built to sift through social media noise and flag what’s fishy.


## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   
  1.	Configure API Credentials:
	 •	Edit cbmi/config.py with your X and Reddit API keys.
	 •	Get keys from X Developer Portal and Reddit Apps.
	2.	Run the Script

Follow prompts to enter keywords, sample size, and time frame.

CLI Usage

	•	Input: Keywords, sample size (max 10,000 due to API limits), start/end dates.
	•	Output: report.pdf with analysis and plots.

GUI Usage

1.	Navigate to the Folder: In your terminal, cd to the cbmi directory where gui.py is.
	2.	Run the Script: Type and hit Enter:
python gui.py

	3.	See the Window: A small window titled “CBMI - Cerberus-Misinformation” pops up with four input fields and a button.

Step 3: Enter Your Inputs

Fill out the fields in the GUI like this:

	1.	Keywords (space-separated):
	•	Type words or phrases you want to analyze (e.g., “election fraud” or “vaccine conspiracy”).
	•	Separate multiple keywords with spaces.
	•	Example: climate hoax carbon tax
	2.	Sample Size (1-1,000,000):
	•	Enter a number for how many posts to grab (e.g., 500).
	•	Note: It’s capped at 10,000 due to API limits, so anything higher gets trimmed to 10,000.
	•	Example: 1000
	3.	Start Time (YYYY-MM-DD):
	•	Type the start date for your analysis in YYYY-MM-DD format (e.g., 2023-10-01).
	•	Must be within the last 7 days for X’s free API.
	4.	End Time (YYYY-MM-DD):
	•	Type the end date, also in YYYY-MM-DD format (e.g., 2023-10-07).
	•	Make sure it’s after the start time!

Step 4: Start the Analysis

	1.	Hit the Button: Click the “Start Analysis” button at the bottom.
	2.	Wait a Bit: The tool will:
	•	Pull posts from X and Reddit (up to half your sample size each).
	•	Check Google Trends for your keywords.
	•	Analyze everything and make plots.
	•	Save it all to a PDF.
	•	You’ll see some text in the terminal like “Collecting up to 500 posts…” and “PDF report generated: report.pdf”.
	3.	Check for Success: If it works, a pop-up says “Success: Report generated: report.pdf”. If something’s off (e.g., bad date format), an error pop-up explains what went wrong.

Step 5: View Your Report

	1.	Find the PDF: Look in the cbmi folder for report.pdf.
	2.	Open It: Double-click to view it in your PDF reader. Inside, you’ll see:
	•	Total posts analyzed.
	•	Sentiment scores and a trend graph.
	•	Post frequency over time.
	•	Google Trends comparison.
	•	Top keywords, users, and possible bots.
	•	An “Intelligence Brief” calling out if it smells like misinformation.
	3.	Bonus Files: You’ll also get frequency.png, sentiment.png, and trends.png—the graphs used in the report.

Notes

	•	Requires Python 3.9+.
	•	On iOS, uses matplotlib.use('Agg') for plotting compatibility.


