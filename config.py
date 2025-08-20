"""
File to add configurations and variables
"""

import os
from dotenv import load_dotenv

load_dotenv()

SHEET_URL = os.getenv("SHEET_URL")
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
URL = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page="
RANGE_OF_PAGES = 3
BASE_URL = "https://webscraper.io"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}