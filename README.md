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
	2.	Run the Script:
python main.py

Follow prompts to enter keywords, sample size, and time frame.

Usage

	•	Input: Keywords, sample size (max 10,000 due to API limits), start/end dates.
	•	Output: report.pdf with analysis and plots.

Notes

	•	Requires Python 3.9+.
	•	On iOS, uses matplotlib.use('Agg') for plotting compatibility.
