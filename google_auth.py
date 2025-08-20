import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from logger import get_logger
# Initialize logger
logger = get_logger(__name__)

def get_creds(scopes: list[str] =None) -> object:
    """
    Function to execute the Google Sheets authorization flow and return credentials.
    It creates a token.pickle file after successful authorization and keeps it as credentials until it expires
    If it expires, it refreshes the token or prompts for re-authorization.

    Args:
        scopes: list of scopes to authorize

    Returns:
    creds: credentials - Google credentials object
    """
    logger.info("Starting Google Sheets authorization process")

    creds = None
    token_path = "token.pickle"
    try:
        if os.path.exists(token_path):
            with open(token_path, "rb") as token_file:
                creds = pickle.load(token_file)
            logger.info("Successfully loaded existing credentials")
    except Exception as e:
        logger.warning(f"Error loading existing credentials: {e}")

    try:
        if not creds or not creds.valid:
            logger.info("Credentials expired, attempting to refresh token")
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
                logger.info("Successfully refreshed expired credentials")
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", scopes=scopes)
                creds = flow.run_local_server(port=0)
                logger.info("OAuth flow completed successfully")
    except Exception as e:
        logger.warning(f"Error: {e}")
        raise Exception(f"Failed to get credentials: {e}")

    try:
        with open(token_path, "wb") as token_file:
            pickle.dump(creds, token_file)
            logger.info("Successfully saved credentials to token.pickle")
    except Exception as e:
        logger.warning(f"Error saving credentials to token.pickle: {e}")

    logger.info("Google Sheets authorization completed successfully")
    return creds