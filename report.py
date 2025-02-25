# cbmi/report.py
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(df, keywords, start_time, end_time, freq, sentiment_trend, trends, analysis, assessment, reasoning):
    """Create a PDF report with analysis and visuals."""
    doc = SimpleDocTemplate("report.pdf", pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("Cerberus-Misinformation Report", styles["Title"]))  # Updated title
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Keywords: {', '.join(keywords)}", styles["Normal"]))
    elements.append(Paragraph(f"Time Frame: {start_time} to {end_time}", styles["Normal"]))
    elements.append(Paragraph(f"Total Posts Analyzed: {len(df)}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Sentiment Analysis
    avg_sentiment = df["sentiment"].mean()
    elements.append(Paragraph("Sentiment Analysis", styles["Heading2"]))
    elements.append(Paragraph(f"Average Sentiment Score: {avg_sentiment:.2f} (-1 to 1)", styles["Normal"]))
    elements.append(Image("sentiment.png", width=400, height=300))
    elements.append(Spacer(1, 12))

    # Post Frequency
    elements.append(Paragraph("Post Frequency Over Time", styles["Heading2"]))
    elements.append(Image("frequency.png", width=400, height=300))
    elements.append(Spacer(1, 12))

    # Google Trends Correlation
    correlation = df.groupby("date")["sentiment"].mean().corr(trends[keywords[0]]) if keywords[0] in trends else 0
    elements.append(Paragraph("Google Trends Correlation", styles["Heading2"]))
    elements.append(Image("trends.png", width=400, height=300))
    elements.append(Paragraph(f"Correlation with Google Trends: {correlation:.2f}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Detailed Analysis
    elements.append(Paragraph("Detailed Analysis", styles["Heading2"]))
    elements.append(Paragraph(f"Top Keywords: {', '.join([f'{k}: {v}' for k, v in analysis['keywords'].items()])}", styles["Normal"]))
    elements.append(Paragraph(f"Top Users: {', '.join([f'{u}: {c}' for u, c in analysis['users'].items()])}", styles["Normal"]))
    if analysis["bots"] is not None:
        elements.append(Paragraph(f"Potential Bots: {', '.join([f'{u}: {c}' for u, c in analysis['bots'].items()])}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Intelligence Brief
    elements.append(Paragraph("Intelligence Brief", styles["Heading2"]))
    elements.append(Paragraph(assessment, styles["Normal"]))
    elements.append(Paragraph(reasoning, styles["Normal"]))

    doc.build(elements)