from bs4 import BeautifulSoup
from config import URL, HEADERS, RANGE_OF_PAGES, BASE_URL
from logger import get_logger
import requests

logger = get_logger(__name__)

def request_url(url: str, headers: dict[str, str]) -> object:
    """
    Function makes HTTP request to the given URL.

    Args:
        url: URL to make request to
        headers: headers - HTTP headers for the request

    Returns:
        response: response object - HTTP response object returned by the request
    """
    logger.info(f"Making request to URL: {url}")

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        logger.info(f"Successfully received response from {url} (Status: {response.status_code})")

        return response
    except requests.exceptions.RequestException as e:
        logger.warning(f"HTTP error for URL {url}: {e}")


def scrape_data() -> list[str, str, str]:
    """
    Function scrapes data from the given URL.


    Returns:
        dataframe: list - scraped data in a suitable for pandas dataframe format
    """

    logger.info("Starting data scraping process")
    logger.info(f"Will scrape {RANGE_OF_PAGES} pages starting from {URL}")

    try:
        dataframe = []
        for counter in range(1, RANGE_OF_PAGES+1):
            logger.info(f"Scraping page {counter}")

            response = request_url(f'{URL}{counter}', HEADERS)

            if response:

                logger.info("Response received successfully, parsing HTML")
                soup = BeautifulSoup(response.text, "html.parser")
                products = soup.find_all("div", class_="caption")
                for product in products:
                    name = product.find("a", class_="title").text.strip()
                    price = product.find("span", itemprop="price").text.strip()
                    numeric_price = float(price.replace("$", ""))
                    description = product.find("p", class_="description").text.strip()
                    link = BASE_URL + product.find("a", class_="title")["href"]
                    dataframe.append(
                        {"Name": f'=HYPERLINK("{link}","{name}")', "Price, $": numeric_price, "Description": description})
                    logger.info(f"Product scraped: {name}")
        if dataframe:
            return dataframe
    except Exception as e:
        logger.warning(f"Error occurred during scraping: {e}")