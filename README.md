Below is a reformatted and rewritten version of the README.md for the CBMI (Cerberus-Misinformation) tool. It provides a clear, consistent, and informative guide on how to set up and use the script via both CLI and GUI, while also explaining the tool’s functionality in a technical yet approachable manner.

CBMI - Cerberus-Misinformation
CBMI is a Python tool designed to analyze social media posts from X (formerly Twitter) and Reddit, helping you identify potential misinformation campaigns. It combines sentiment analysis, user behavior checks, and Google Trends data to deliver clear PDF reports with practical insights and visualizations. Built to cut through social media noise, CBMI flags suspicious activity—like sudden spikes or bot-like behavior—so you can focus on what matters.

What CBMI Does
Before diving into setup and usage, here’s a quick look at how CBMI works under the hood:
	•	Data Collection: CBMI pulls posts from X and Reddit using their APIs (tweepy for X, praw for Reddit). It also fetches Google Trends data (pytrends) to see how your keywords are trending in search interest. (Note: Due to API limits, post collection is capped at 10,000 samples.)
	•	Sentiment Analysis: Each post is scored for sentiment using TextBlob (-1 for negative, 1 for positive). Daily averages help track mood shifts over time.
	•	Behavior Analysis: CBMI monitors user activity to spot potential bots—accounts less than 30 days old posting frequently. It also extracts top keywords and identifies the most active users using scikit-learn’s CountVectorizer.
	•	Trend Correlation: Post frequency is compared with Google Trends data to see if social media activity aligns with broader public interest.
	•	Report Generation: The tool creates line graphs for post frequency, sentiment trends, and trend comparisons using matplotlib. These visuals, along with key insights, are compiled into a PDF report using reportlab.

Setup
Follow these steps to get CBMI up and running:
	1	Install Python: Ensure you have Python 3.9 or higher installed. Download it from python.org if needed.
	2	Clone the Repository: Download the CBMI code by cloning the GitHub repository: git clone https://github.com/yourusername/cbmi.git
	3	cd cbmi
	4	
	5	Install Dependencies: Install the required Python libraries using the provided requirements.txt file: pip install -r requirements.txt
	6	
	7	Configure API Credentials:
	◦	X API Keys: Sign up for a developer account at developer.twitter.com to get your Consumer Key, Consumer Secret, Access Token, and Access Token Secret.
	◦	Reddit API Keys: Create an app at reddit.com/prefs/apps to obtain your Client ID and Client Secret.
	◦	Open cbmi/config.py in a text editor and replace the placeholder values with your actual API keys.

CLI Usage
To run CBMI via the command line:
	1	Navigate to the Directory: Open a terminal and change to the cbmi directory: cd path/to/cbmi
	2	
	3	Run the Script: Execute the main script: python main.py
	4	
	5	Follow the Prompts:
	◦	Keywords: Enter space-separated keywords or phrases (e.g., “election fraud”).
	◦	Sample Size: Specify the number of posts to collect (1 to 1,000,000). (Capped at 10,000 due to API limits.)
	◦	Start Time: Enter the start date in YYYY-MM-DD format (e.g., “2023-10-01”). (Must be within the last 7 days for X’s free API.)
	◦	End Time: Enter the end date in YYYY-MM-DD format (e.g., “2023-10-07”). (Must be after the start time.)
	6	Wait for Analysis: CBMI will collect posts, analyze the data, and generate a PDF report. You’ll see progress updates in the terminal, like “Collecting up to 500 posts…” and “PDF report generated: report.pdf”.
	7	View the Report: Find report.pdf in the cbmi directory, along with image files (frequency.png, sentiment.png, trends.png).

GUI Usage
For a more user-friendly experience, you can use the GUI:
	1	Navigate to the Directory: Open a terminal and change to the cbmi directory: cd path/to/cbmi
	2	
	3	Run the GUI Script: Launch the GUI: python gui.py
	4	
	5	Enter Inputs in the Window: A window titled “CBMI - Cerberus-Misinformation” will appear with input fields:
	◦	Keywords: Type your keywords, separated by spaces (e.g., “climate hoax carbon tax”).
	◦	Sample Size: Enter a number between 1 and 1,000,000 (capped at 10,000).
	◦	Start Time: Input the start date (YYYY-MM-DD). (Must be within the last 7 days for X’s free API.)
	◦	End Time: Input the end date (YYYY-MM-DD). (Must be after the start time.)
	6	Start the Analysis: Click the “Start Analysis” button.
	◦	The tool will collect data, run the analysis, and generate the report.
	◦	A pop-up will confirm success (“Success: Report generated: report.pdf”) or display errors (e.g., invalid date format).
	7	View the Report: Locate report.pdf in the cbmi folder to see your analysis.

Understanding the Report
The generated report.pdf includes:
	•	Total Posts Analyzed: How many posts were collected and analyzed.
	•	Sentiment Analysis: Average sentiment score and a trend graph over time.
	•	Post Frequency: A graph showing daily post counts to spot spikes.
	•	Google Trends Comparison: How social media activity aligns with search interest.
	•	Top Keywords & Users: Lists of frequently used words and active posters.
	•	Potential Bots: Accounts flagged for suspicious activity (e.g., new accounts posting frequently).
	•	Intelligence Brief: A summary assessment of whether the data suggests a misinformation campaign.
Additionally, you’ll find the following image files in the cbmi folder:
	•	frequency.png: Post frequency over time.
	•	sentiment.png: Sentiment trend over time.
	•	trends.png: Social media activity vs. Google Trends.

Notes
	•	Python Version: Requires Python 3.9 or higher.
	•	API Limits: X’s free API tier limits data to the last 7 days and 10,000 tweets per month. Reddit API limits also apply.
	•	Plotting on iOS: CBMI uses matplotlib.use('Agg') for compatibility, saving plots as images without needing a display.
	•	Troubleshooting:
	◦	If no posts are collected, check your API keys and ensure the date range is within the last 7 days.
	◦	For large sample sizes, expect longer processing times. Start with smaller samples (e.g., 100) to test.
	◦	Ensure dates are in YYYY-MM-DD format, and the end date is after the start date.

This README.md is now consistent, informative, and balanced—providing both a technical overview and clear instructions for setup and usage via CLI and GUI. It’s ready for your GitHub repo! Let me know if you’d like further tweaks.
