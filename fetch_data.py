import praw
import sqlite3
from credentials import client_id, client_secret, user_agent
from textblob import TextBlob

#  Reddit API connection
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)


subreddit_name = 'datascience'  # Change as needed
subreddit = reddit.subreddit(subreddit_name)


posts = []
for post in subreddit.hot(limit=100): 
    title = post.title
    score = post.score
    num_comments = post.num_comments
    created_utc = post.created_utc

   
    sentiment_score = TextBlob(title).sentiment.polarity
    if sentiment_score > 0:
        sentiment = 'Positive'
    elif sentiment_score < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    posts.append((post.id, title, score, num_comments, created_utc, sentiment))


conn = sqlite3.connect('reddit_data.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS posts (
    id TEXT PRIMARY KEY, 
    title TEXT, 
    score INTEGER, 
    num_comments INTEGER, 
    created_utc REAL,
    sentiment TEXT)
''')


cursor.executemany('INSERT OR IGNORE INTO posts VALUES (?, ?, ?, ?, ?, ?)', posts)
conn.commit()
conn.close()

print(f" Fetched {len(posts)} posts from r/{subreddit_name} with sentiment analysis.")
