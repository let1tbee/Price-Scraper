# Web Price Scraper with Google Sheets Integration

A robust web scraping application that extracts product data from e-commerce websites and automatically organizes the information in Google Sheets with proper formatting and styling. 

This application retrieves items from a test e-commerce webpage: https://webscraper.io/test-sites/e-commerce/static/computers/laptops.

## 🚀 Features

- **Automated Web Scraping**: Extracts product names, prices, and descriptions from e-commerce websites
- **Data Processing**: Sorts products by price for easy comparison
- **Google Sheets Integration**: Automatically uploads data to Google Sheets
- **Worksheet Management**: Creates new worksheets with timestamps for each scraping session
- **Rich Formatting**: Applies professional styling to the spreadsheet including:
  - Hyperlinked product names
  - Proper column sizing
  - Table borders
  - Header formatting
- **Comprehensive Logging**: Detailed logs of the entire process for monitoring and debugging
- **Error Handling**: Robust error handling throughout the application

## 📋 Requirements

```
# Core dependencies
requests>=2.31.0
beautifulsoup4>=4.12.2
pandas>=2.0.0

# Google APIs
google-auth>=2.22.0
google-auth-oauthlib>=1.0.0
google-auth-httplib2>=0.1.0
gspread>=5.10.0
gspread-formatting>=1.1.2

# Configuration management
python-dotenv>=1.0.0
```

## 🔧 Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/let1tbee/Price-Scraper
   cd Price-Scraper
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Google Sheets API**
   - Create a project in [Google Cloud Console](https://console.cloud.google.com/)
   - Enable the Google Sheets API and Google Drive API
   - Create OAuth credentials and download as `credentials.json`
   - Place `credentials.json` in the project root directory

5. **Configure environment variables**
   Create a `.env` file with:
   ```
   SHEET_URL=your_google_sheet_url
   ```

## 🏃‍♂️ Usage

```bash
# Run the scraper
python main.py
```

The application will:
1. Scrape product data from the configured e-commerce website
2. Process and sort the data
3. Create a new worksheet in your Google Sheet
4. Upload and format the data
5. Log the entire process

## 🔍 How It Works

### Workflow

1. **Web Scraping** (`web_scraper.py`)
   - Makes HTTP requests to target websites
   - Parses HTML with BeautifulSoup
   - Extracts product information

2. **Data Processing** (`google_sheets_handler.py`)
   - Converts data to pandas DataFrame
   - Sorts by price
   - Prepares data for Google Sheets

3. **Google Sheets Integration** (`google_sheets_handler.py`, `google_auth.py`)
   - Authenticates with Google API
   - Creates new worksheet
   - Uploads data
   - Applies formatting

4. **Logging** (`logger.py`)
   - Records detailed information about each step
   - Helps with monitoring and debugging

## 📂 Project Structure

```
├── main.py               # Main entry point
├── web_scraper.py       # Web scraping functionality
├── google_sheets_handler.py  # Google Sheets integration
├── google_auth.py        # Google authentication
├── config.py             # Configuration settings
├── logger.py             # Logging functionality
├── requirements.txt      # Project dependencies
├── .env                  # Environment variables (not in repo)
└── credentials.json      # Google API credentials (not in repo)
```
## 📊 Sample Output

The application generates a Google Sheet file with analysis results. Google sheet example could be found in 'Price_scraper_results_example.xlsx'

<img width="1315" height="528" alt="зображення" src="https://github.com/user-attachments/assets/5f643c8b-8abe-4daf-aa78-d33a6bac0dba" />

## 📝 Logging

All operations are logged to:
- **Console** - basic information and errors
- **Log files** - detailed information in the `logs/` directory

Log file format: `logs_YYYYMMDD.log`

## 🔒 Security

- OAuth 2.0 authentication for Google API
- All sensitive data is stored in the .env file
- The .env file is added to .gitignore
- Token caching for efficient authentication

## ⚙️ Configuration

### Configurable parameters in `config.py`:
```python
URL = "https://your-target-website.com/products?page="
RANGE_OF_PAGES = 5  # Number of pages to scrape
BASE_URL = "https://your-target-website.com"
```


---

⭐ If you found this project helpful, please give it a star on GitHub!
