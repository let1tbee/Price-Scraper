from web_scraper import scrape_data
from google_sheets_handler import data_to_gspread, google_conf, update_google_sheet
from logger import get_logger



def main() -> int:
    """
    Main application entry point for price scraping.

     This function orchestrates the entire workflow:
     1. Scrapes data from the given URL
     2. Converts scraped data to Google Sheets format
     3. Updates Google Sheet with the scraped data and formats it
    """
    logger = get_logger(__name__)
    try:
        logger.info("="*60)
        logger.info("Starting web scraping application")
        logger.info("="*60)


        data = scrape_data()
        if not data:
            logger.warning("No data was scraped. Exiting...")
            return 1

        refined_data = data_to_gspread(data)
        if not refined_data:
            logger.error("Failed to process scraped data")
            return 1

        sheet = google_conf()
        if not sheet:
            logger.error("Failed to configure Google Sheets")
            return 1

        update_google_sheet(sheet, refined_data,  len(data))

        logger.info("Web scraping application completed successfully. Data has been uploaded to Google Sheets.")
        return 0
    except Exception as e:
        logger.error(f"An error occurred during web scraping: {e}")
        return 1




if __name__ == "__main__":
    main()

