import praw
import pandas as pd
from telethon import TelegramClient
import asyncio

# for reddit
reddit = praw.Reddit(
    client_id="3hOinW1HCEoiIXwRySGecQ",  
    client_secret="mXRiyGcR7GDeXL06xGlCi-3ZV9PmqQ",
    user_agent="FraudScraper"
)

keywords = ["scam", "fraud", "lottery", "crypto scam", "job scam"]
posts_data = []

for keyword in keywords:
    for submission in reddit.subreddit("scams+india+cryptocurrency").search(keyword, limit=50):
        posts_data.append({
            "platform": "Reddit",
            "fraud_type": keyword,
            "text": submission.title + " " + submission.selftext
        })

print(f"Collected {len(posts_data)} Reddit posts")

# For Tele
api_id = '22232850'
api_hash = 'aa9f1c3e2b4253dd88d8c28d636eaa3c'
phone = '+919881927811'

client = TelegramClient('session_name', api_id, api_hash)

async def scrape_telegram():
    await client.start(phone)
    messages_list = []

    group = '@btccrytodiscussion'  # public group username
    
    async for message in client.iter_messages(group, limit=150):
        if message.text:  # ignore empty messages
            messages_list.append({
                'platform': 'Telegram',
                'fraud_type': 'unknown',
                'text': message.text
            })

    print(f"Collected {len(messages_list)} Telegram messages")
    return messages_list

# run tele scraper
telegram_data = asyncio.run(scrape_telegram())

# Combine dat
all_data = posts_data + telegram_data

df = pd.DataFrame(all_data)
df.to_csv("collected_data.csv", index=False, encoding="utf-8")
print("All data saved to collected_data.csv")
