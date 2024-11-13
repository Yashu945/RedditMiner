# utils/reddit_client.py

import praw
import logging
import os  # Import os to use environment variables

def initialize_reddit_client():
    """
    Initializes and returns a Reddit client instance using PRAW with credentials from environment variables.
    """
    CLIENT_ID = os.getenv('REDDIT_CLIENT_ID', 'YOUR_CLIENT_ID')
    CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET', 'YOUR_CLIENT_SECRET')
    USER_AGENT = os.getenv('REDDIT_USER_AGENT', 'YOUR_USER_AGENT')

    # Set up logging for this module
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    try:
        reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent=USER_AGENT,
        )
        
        logger.info("Reddit client initialized successfully.")
        return reddit

    except Exception as e:
        logger.error(f"Failed to initialize Reddit client: {e}")
        return None
