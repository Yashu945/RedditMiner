# main.py

import logging
from google.oauth2 import service_account
from google.cloud import bigquery
from utils.reddit_client import initialize_reddit_client
from utils.data_extraction import fetch_subreddit_posts, fetch_post_comments
from utils.data_cleaning import clean_posts_data, clean_comments_data, preprocess_dataframe
from utils.data_loading import create_dataset, create_table, load_dataframe_to_bigquery, posts_schema, comments_schema
from config import SUBREDDITS

def main():
    # Initialize logging
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting the Reddit data pipeline.")

    # Embedded credentials directly from service_account.json
    credentials_info = {"Credentials"
        
    }

    # Load credentials from the embedded info
    credentials = service_account.Credentials.from_service_account_info(credentials_info)
    client = bigquery.Client(credentials=credentials, project="default-project-439615")

    # Create the dataset and tables
    create_dataset(client)
    create_table(client, 'posts', posts_schema)
    create_table(client, 'comments', comments_schema)

    # Initialize Reddit client
    reddit = initialize_reddit_client()

    # Process each subreddit
    for subreddit in SUBREDDITS:
        logging.info(f"Processing subreddit: {subreddit}")

        # Fetch posts
        posts = fetch_subreddit_posts(reddit, subreddit)
        if not posts:
            logging.info(f"No new posts found for subreddit: {subreddit}")
            continue

        # Clean posts data
        posts_df = clean_posts_data(posts)
        posts_df = preprocess_dataframe(posts_df, ['title', 'selftext'])
        load_dataframe_to_bigquery(client, posts_df, 'posts')

        # Fetch and clean comments
        for post_id in posts_df['id']:
            comments = fetch_post_comments(reddit, post_id)
            if comments:
                comments_df = clean_comments_data(comments)
                comments_df = preprocess_dataframe(comments_df, ['body'])
                load_dataframe_to_bigquery(client, comments_df, 'comments')

    logging.info("Data pipeline execution completed.")

if __name__ == "__main__":
    main()
