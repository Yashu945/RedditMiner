import os
from google.cloud import secretmanager
from google.oauth2 import service_account

def get_secret(secret_name):
    """
    Retrieves a secret from Google Cloud Secret Manager using service account credentials.
    Credentials are loaded from environment variables.
    """
    # Load credentials from environment variables
    credentials_info = {
        "type": "service_account",
        "project_id": os.getenv('GCP_PROJECT_ID', 'YOUR_PROJECT_ID'),
        "private_key_id": os.getenv('GCP_PRIVATE_KEY_ID', 'YOUR_PRIVATE_KEY_ID'),
        "private_key": os.getenv('GCP_PRIVATE_KEY', 'YOUR_PRIVATE_KEY'),
        "client_email": os.getenv('GCP_CLIENT_EMAIL', 'YOUR_CLIENT_EMAIL'),
        "client_id": os.getenv('GCP_CLIENT_ID', 'YOUR_CLIENT_ID'),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.getenv('GCP_CLIENT_X509_CERT_URL', 'YOUR_CLIENT_X509_CERT_URL')
    }

    # Initialize Secret Manager client with credentials from environment
    credentials = service_account.Credentials.from_service_account_info(credentials_info)
    client = secretmanager.SecretManagerServiceClient(credentials=credentials)

    # Access the secret
    project_id = credentials_info['project_id']
    name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
    response = client.access_secret_version(name=name)
    return response.payload.data.decode('UTF-8')
