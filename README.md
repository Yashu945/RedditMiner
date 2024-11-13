# RedditMiner

This project automates the collection, cleaning, storage, and analysis of data from Reddit. By integrating Reddit's API with Google Cloud services, this pipeline allows users to gain insights into trending topics, popular discussions, and community sentiment across various subreddits. It is designed for researchers, analysts, and data scientists interested in tracking real-time trends and analyzing large-scale Reddit data.

## Key Components

### 1. **Data Extraction**
Data extraction forms the core of the pipeline, where posts and comments are retrieved from Reddit using Reddit's API. This process is simplified with the `praw` library, which is a Python wrapper for the Reddit API. The extraction is customizable, allowing for data collection based on specific keywords, subreddits, or timeframes.

**Features:**
- Collect posts and comments from specific subreddits or globally.
- Filter data by time range (e.g., posts in the last week, month, or year).
- Use keyword-based or hashtag-based queries to focus on specific topics or themes.
- Capture metadata such as upvotes, downvotes, comments, post title, content, and creation time.

### 2. **Data Cleaning**
The extracted data is then cleaned to ensure it is structured, consistent, and ready for analysis. This stage involves handling missing values, filtering out irrelevant or spammy data, and converting raw text or numerical data into usable formats.

**Key Tasks:**
- Remove or impute missing values.
- Standardize text (e.g., convert to lowercase, remove special characters).
- Filter out irrelevant or low-quality posts (e.g., spam, deleted posts).
- Ensure data consistency (e.g., unified timestamp formats, numeric value normalization).
- Enhance data by adding additional features like sentiment scores or categorizing posts by topics.

### 3. **Data Loading**
After cleaning, the data is loaded into **Google BigQuery**, a fully managed, serverless data warehouse. BigQuery is ideal for handling large volumes of data and performing complex SQL queries, making it perfect for analyzing trends over time.

**Benefits of BigQuery Integration:**
- Scalable storage and fast querying capabilities.
- Secure access control for sensitive data.
- Seamless integration with Google Cloud services for advanced analytics (e.g., AI, machine learning).
- SQL-like query language for analyzing data, identifying trends, and generating insights.

### 4. **Configuration & Environment Management**
The project uses environment variables to manage sensitive credentials, such as Reddit API keys and Google Cloud credentials, ensuring security and reducing the risk of exposing sensitive information in the codebase.

**Key Features:**
- Secure handling of credentials via environment variables.
- Centralized configuration management, which simplifies deployment across multiple environments (development, staging, production).
- Integration with Google Cloud IAM for granular access control.

### 5. **Helpers and Modularization**
The pipeline is broken down into modular, reusable components to ensure maintainability and scalability. This approach allows each module to handle a single responsibility (e.g., data extraction, cleaning, transformation, loading), making the codebase easier to update, test, and debug.

**Benefits of Modularization:**
- Reusable components that promote scalability and maintainability.
- Easy testing and debugging of individual modules.
- Flexibility to add new data sources or modify pipeline stages as needed.

## Use Cases

This pipeline is applicable to various domains, including:

- **Social Media Research**: Analyzing public sentiment, emerging trends, or the impact of specific topics or events on Reddit.
- **Business Intelligence**: Tracking brand mentions, customer feedback, and product trends to inform business decisions.
- **Academic Research**: Studying community dynamics, user behavior, or discourse patterns across subreddits.
- **Political Analysis**: Analyzing political discussions, sentiment, and issue prominence to understand public opinion on key political topics.

## Requirements

To run this pipeline, you will need the following:

- **Python 3.x**: The programming language used for building and running the pipeline.
- **Required Python Packages**: These are listed in the `requirements.txt` file and include:
  - `praw` for accessing Reddit's API.
  - `google-cloud-bigquery` for interacting with BigQuery.
  - Other data manipulation libraries like `pandas` and `numpy`.
- **Google Cloud Account**: Necessary for accessing BigQuery and storing data securely.
- **Reddit Developer Account**: You will need to create an account and obtain API credentials from Reddit to access their API.

## Setup & Installation

Follow these steps to set up the pipeline:

1. **Install Dependencies**: Install the required Python libraries using:
   ```bash
   pip install -r requirements.txt
