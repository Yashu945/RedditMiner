from google.cloud import bigquery
import logging
import os

# Load dataset ID from environment variables for better security
DATASET_ID = os.getenv('BQ_DATASET_ID', 'YOUR_DATASET_ID')

posts_schema = [
    bigquery.SchemaField('id', 'STRING', mode='REQUIRED'),
    bigquery.SchemaField('title', 'STRING'),
    bigquery.SchemaField('selftext', 'STRING'),
    bigquery.SchemaField('author', 'STRING'),
    bigquery.SchemaField('created_utc', 'TIMESTAMP'),
    bigquery.SchemaField('score', 'INTEGER'),
    bigquery.SchemaField('num_comments', 'INTEGER'),
    bigquery.SchemaField('subreddit', 'STRING'),
    bigquery.SchemaField('url', 'STRING'),
    bigquery.SchemaField('upvote_ratio', 'FLOAT'),
    bigquery.SchemaField('over_18', 'BOOLEAN'),
]

comments_schema = [
    bigquery.SchemaField('id', 'STRING', mode='REQUIRED'),
    bigquery.SchemaField('post_id', 'STRING'),
    bigquery.SchemaField('parent_id', 'STRING'),
    bigquery.SchemaField('body', 'STRING'),
    bigquery.SchemaField('author', 'STRING'),
    bigquery.SchemaField('created_utc', 'TIMESTAMP'),
    bigquery.SchemaField('score', 'INTEGER'),
    bigquery.SchemaField('subreddit', 'STRING'),
]

def create_dataset(client):
    dataset_ref = client.dataset(DATASET_ID)
    try:
        client.get_dataset(dataset_ref)
        logging.info(f"Dataset {DATASET_ID} exists.")
    except bigquery.NotFound:
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = "US"
        client.create_dataset(dataset)
        logging.info(f"Created dataset {DATASET_ID}.")

def create_table(client, table_name, schema):
    table_ref = client.dataset(DATASET_ID).table(table_name)
    try:
        client.get_table(table_ref)
        logging.info(f"Table {table_name} exists.")
    except bigquery.NotFound:
        table = bigquery.Table(table_ref, schema=schema)
        client.create_table(table)
        logging.info(f"Created table {table_name}.")

def load_dataframe_to_bigquery(client, df, table_name):
    table_ref = client.dataset(DATASET_ID).table(table_name)
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND
    )
    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()  # Wait for job to complete
    logging.info(f"Loaded {len(df)} rows into {DATASET_ID}:{table_name}.")
