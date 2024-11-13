# utils/data_extraction.py

from datetime import datetime, timedelta, timezone

def fetch_subreddit_posts(reddit, subreddit_name):
    """
    Fetches the latest posts from a specified subreddit using the Reddit API client.
    Filters out posts older than 1 day.

    Args:
        reddit (praw.Reddit): The initialized Reddit client.
        subreddit_name (str): The name of the subreddit to fetch posts from.

    Returns:
        list: A list of dictionaries, each representing a post.
    """
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    time_threshold = datetime.now(timezone.utc) - timedelta(days=1)

    for submission in subreddit.new(limit=None):
        created_time = datetime.fromtimestamp(submission.created_utc, tz=timezone.utc)
        if created_time < time_threshold:
            break  # Stop fetching older posts

        posts.append({
            'id': submission.id,
            'title': submission.title,
            'selftext': submission.selftext,
            'author': str(submission.author) if submission.author else '[deleted]',
            'created_utc': created_time.isoformat(),
            'score': submission.score,
            'num_comments': submission.num_comments,
            'subreddit': subreddit_name,
            'url': submission.url,
            'upvote_ratio': submission.upvote_ratio,
            'over_18': submission.over_18
        })

    return posts

def fetch_post_comments(reddit, post_id):
    """
    Fetches all comments for a specified Reddit post using the Reddit API client.
    Filters out comments older than 1 day.

    Args:
        reddit (praw.Reddit): The initialized Reddit client.
        post_id (str): The ID of the Reddit post to fetch comments from.

    Returns:
        list: A list of dictionaries, each representing a comment.
    """
    submission = reddit.submission(id=post_id)
    submission.comments.replace_more(limit=None)  # Load all comments
    comments = []
    time_threshold = datetime.now(timezone.utc) - timedelta(days=1)

    for comment in submission.comments.list():
        created_time = datetime.fromtimestamp(comment.created_utc, tz=timezone.utc)
        if created_time < time_threshold:
            continue  # Skip older comments

        comments.append({
            'id': comment.id,
            'post_id': post_id,
            'parent_id': comment.parent_id,
            'body': comment.body,
            'author': str(comment.author) if comment.author else '[deleted]',
            'created_utc': created_time.isoformat(),
            'score': comment.score,
            'subreddit': submission.subreddit.display_name
        })

    return comments
