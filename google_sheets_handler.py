import datetime
import gspread
import pandas as pd
from google_auth import get_creds
from config import SCOPES, SHEET_URL
from logger import get_logger
from gspread_formatting import set_column_width

logger = get_logger(__name__)


def google_conf() -> object:
    """
    Function initializes Google Sheets configuration.
    It creates a new worksheet with the name of the previous month or creates a copy with current date if it already exists.

    Returns:
        sheet: the Google Sheet object for further updates.
    """
    logger.info("Initializing Google Sheets configuration")
    execution_date = datetime.datetime.now()
    # Google Sheets client authorization
    try:
        client = gspread.authorize(get_creds(SCOPES))  # change to gspread.service_account(filename= ) for service account authorization. get_creds function is not needed in this case.
        sheet = client.open_by_url(SHEET_URL)  # choose Google Sheet by URL

        # Create a new worksheet with the name of the previous month or create a copy with current date if it already exists

        sheet = sheet.add_worksheet(title=execution_date.strftime('%Y-%m-%d-%H-%M-%S'), rows="100",
                                    cols="20")  # add worksheet with current date as title
        logger.info("Successfully created new worksheet")
        return sheet

    except Exception as e:
        logger.warning(f"Worksheet creation failed or already exists: {e}")


def data_to_gspread(dataframe: pd.DataFrame) -> list[str, str, str]:
    """
    Function converts scraped data to Google Sheets format.

    Args:
        dataframe: pandas dataframe

    Returns:
        data: list of lists
    """
    logger.info("Converting scraped data to Google Sheets format")
    try:
        df = pd.DataFrame(dataframe)
        df.sort_values(by="Price, $", inplace=True, ascending=True)
        data = [df.columns.values.tolist()] + df.values.tolist()
        logger.info(f"Successfully converted data to Google Sheets format ({len(data)} rows including header)")
        return data

    except Exception as e:
        logger.warning(f"Error converting data to Google Sheets format: {e}")

def draw_borders(sheet: object, range_name: str) -> None:
    """
    Function to draw borders around the specified range in the Google Sheet.

    Args:
        sheet: Google Sheet object.
        range_name: Range in A1 notation to apply borders.

    """
    sheet.format(range_name, {
        "borders": {
            "top": {"style": "SOLID"},
            "bottom": {"style": "SOLID"},
            "left": {"style": "SOLID"},
            "right": {"style": "SOLID"}
        }
    })
def format_header(sheet: object, header_range: str = 'A1:C1'):
    """
    Function to format the header of the Google Sheet.
    It makes the header bold and center-aligned.

    Args:
        sheet: Google Sheet object.
        header_range: Range in A1 notation for the header to format.
    """
    sheet.format(header_range, {
        "horizontalAlignment": "CENTER",
        "textFormat": {
            "bold": True
        }
    })

def update_google_sheet(sheet: object, data: list, df_length: int) -> None:
    """
    Function to update Google Sheet with the Asana task data and format it.

    Args:
        sheet: Google Sheet object.
        data: List of lists containing the data to update the sheet.
        df_length: Length of the DataFrame to determine where to place totals.
    """
    logger.info("Updating Google Sheet with scrapped data")
    # Update the sheet with data
    try:
        sheet.update(
            range_name='A1',
            values=data,
            value_input_option='USER_ENTERED'
        )
    except Exception as e:
        logger.warning(f"Error updating Google Sheet: {e}")

    logger.info("Formatting the sheet")
    try:
        # Set column widths
        set_column_width(sheet, 'C', 800)

        format_header(sheet, 'A1:C1')  # Format header
        # Add borders to the whole table
        draw_borders(sheet, f'A1:C{df_length + 1}')

        logger.info("Google Sheet updated successfully ")
    except Exception as e:
        logger.warning(f"Error formatting Google Sheet: {e}")