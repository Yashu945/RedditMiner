# Reddit Data Pipeline Project

This project is designed to gather, process, and analyze data from Reddit to generate insights into trending topics and discussions. Using Reddit's API, we collect posts from various subreddits, clean and structure the data, and store it in Google BigQuery for further analysis. The project integrates with Google Cloud for secure storage and scalable data processing.

## Key Components

1. **Data Extraction**: Connects to Reddit's API to collect posts based on keywords, subreddits, or timeframes, providing a snapshot of popular discussions. The extraction process utilizes `praw`, a Python library designed for easy Reddit access.

2. **Data Cleaning**: Cleans the extracted data by removing unnecessary information, structuring it for clarity, and ensuring it's ready for analysis. This stage focuses on formatting data consistently, handling missing values, and preparing the data for storage.

3. **Data Loading**: Stores the cleaned data in Google BigQuery, a scalable data warehouse. This enables efficient querying and analysis, especially helpful for tracking trends and patterns over time.

4. **Configuration and Environment Management**: To protect sensitive information, the project uses environment variables for all API keys and credentials, ensuring secure integration with Reddit and Google Cloud services.

5. **Helpers and Modularization**: Key functions are broken down into reusable modules, allowing easy updates, testing, and debugging. This also makes the code adaptable for future modifications or additional data sources.

## Use Case

This project is ideal for researchers, analysts, or data scientists interested in monitoring social media trends. By gathering data from Reddit, it allows users to analyze sentiment, emerging topics, or user engagement over time. The processed data can support various applications, from social research to business intelligence.

## Requirements

- **Python** with packages listed in `requirements.txt` (includes `praw` for Reddit API access and `google-cloud-bigquery` for data storage).
- **Google Cloud Account** for BigQuery access.
- **Reddit Developer Account** to obtain API credentials for data extraction.
