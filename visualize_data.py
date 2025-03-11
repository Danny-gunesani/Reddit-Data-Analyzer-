import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from SQLite
conn = sqlite3.connect('reddit_data.db')
df = pd.read_sql('SELECT * FROM posts', conn)
conn.close()

# Plot Score Distribution
plt.figure(figsize=(10, 5))
sns.histplot(df['score'], bins=30, kde=True)
plt.title('Distribution of Post Scores')
plt.xlabel('Score')
plt.ylabel('Count')
plt.show()

# Plot Comments Distribution
plt.figure(figsize=(10, 5))
sns.histplot(df['num_comments'], bins=30, kde=True)
plt.title('Distribution of Number of Comments')
plt.xlabel('Number of Comments')
plt.ylabel('Count')
plt.show()

# Plot Sentiment Distribution
plt.figure(figsize=(7, 5))
sns.countplot(x=df['sentiment'], palette='coolwarm')
plt.title('Sentiment Analysis of Posts')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()
