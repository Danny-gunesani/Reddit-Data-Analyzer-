import sqlite3
import pandas as pd

# Load data from SQLite
conn = sqlite3.connect('reddit_data.db')
df = pd.read_sql('SELECT * FROM posts', conn)
conn.close()

# Display first few rows
print(df.head())

# Basic Statistics
summary = f'''
 Subreddit Data Summary:
- Total Posts: {len(df)}
- Average Score: {df["score"].mean():.2f} (Max: {df["score"].max()})
- Average Comments: {df["num_comments"].mean():.2f} (Max: {df["num_comments"].max()})
'''

# Sentiment Distribution
sentiment_counts = df['sentiment'].value_counts()
summary += f'''
 Sentiment Analysis:
- Positive Posts: {sentiment_counts.get("Positive", 0)}
- Neutral Posts: {sentiment_counts.get("Neutral", 0)}
- Negative Posts: {sentiment_counts.get("Negative", 0)}
'''

print(summary)
