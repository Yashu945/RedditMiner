# utils/data_cleaning.py

import pandas as pd

def clean_posts_data(posts):
    """
    Cleans and processes the posts data, preparing it for BigQuery insertion.
    
    Args:
        posts (list): A list of dictionaries where each dictionary represents a post.

    Returns:
        DataFrame: A cleaned DataFrame with posts data.
    """
    # Convert list of posts to DataFrame
    df = pd.DataFrame(posts)
    
    # Fill missing values for certain columns
    df.fillna({'selftext': '', 'author': '[deleted]'}, inplace=True)
    
    # Filter out rows where the 'title' column is empty or consists only of whitespace
    df = df[df['title'].str.strip() != '']
    
    # Ensure data types match BigQuery schema
    df['score'] = df['score'].astype(int)
    df['num_comments'] = df['num_comments'].astype(int)
    df['over_18'] = df['over_18'].astype(bool)
    
    # Convert 'created_utc' to datetime format
    df['created_utc'] = pd.to_datetime(df['created_utc'])
    
    return df

def clean_comments_data(comments):
    """
    Cleans and processes the comments data, preparing it for BigQuery insertion.
    
    Args:
        comments (list): A list of dictionaries where each dictionary represents a comment.

    Returns:
        DataFrame: A cleaned DataFrame with comments data.
    """
    # Convert list of comments to DataFrame
    df = pd.DataFrame(comments)
    
    # Fill missing values for certain columns
    df.fillna({'body': '', 'author': '[deleted]'}, inplace=True)
    
    # Filter out rows where the 'body' column is empty or consists only of whitespace
    df = df[df['body'].str.strip() != '']
    
    # Ensure data types match BigQuery schema
    df['score'] = df['score'].astype(int)
    
    # Convert 'created_utc' to datetime format
    df['created_utc'] = pd.to_datetime(df['created_utc'])
    
    return df

def preprocess_text(text):
    """
    Preprocesses text by removing newlines and extra whitespace.
    
    Args:
        text (str): The text to preprocess.

    Returns:
        str: Preprocessed text.
    """
    # Remove newline characters and extra spaces
    text = text.replace('\n', ' ').replace('\r', ' ').strip()
    return text

def preprocess_dataframe(df, text_fields):
    """
    Applies text preprocessing to specified fields in a DataFrame.
    
    Args:
        df (DataFrame): The DataFrame containing text fields to preprocess.
        text_fields (list): A list of column names (str) to preprocess.

    Returns:
        DataFrame: The DataFrame with preprocessed text fields.
    """
    for field in text_fields:
        df[field] = df[field].apply(preprocess_text)
    return df
