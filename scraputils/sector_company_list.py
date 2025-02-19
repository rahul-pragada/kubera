import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_screener_data(company_url):
    """Scrapes financial data from screener.in for a given company URL.

    Args:
        company_url (str): The URL of the company page on screener.in.

    Returns:
        dict or None: A dictionary containing scraped financial data,
                       or None if an error occurred.
    """
    try:
        response = requests.get(company_url)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'html.parser')

        return soup

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None
    except AttributeError as e:
        print(f"Error parsing HTML: {e}")
        return None


def fetch_sector_list():
    company_url = "https://www.screener.in/company/compare/00000085/"
    company_data = scrape_screener_data(company_url)

    if company_data:
        # Find the table you want to extract
        table = company_data.find('table', {'class': 'data-table'}) # Replace with the actual class name

        if table:
            # Extract data from the table
            rows = []
            for row in table.find_all('tr'):
              cols = row.find_all('td')
              rows.append([ele.text.strip() for ele in cols])

            # Create a Pandas DataFrame
            df = pd.DataFrame(rows)
            return df
        else:
            print("Table not found on the page.")
    else:
        print("Failed to retrieve company data.")