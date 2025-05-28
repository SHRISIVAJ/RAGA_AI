import requests
from bs4 import BeautifulSoup

class ScrapingAgent:
    def __init__(self, base_url):
        self.base_url = base_url

    def scrape_data(self, endpoint=""):
        """
        Scrapes data from a given URL endpoint and returns the relevant information.
        :param endpoint: the relative path or endpoint to scrape from the base URL
        :return: parsed data
        """
        url = self.base_url + endpoint
        response = requests.get(url)

        # Check if the request is successful
        if response.status_code != 200:
            raise Exception(f"Error fetching data from {url}")

        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Let's say we are scraping a table of financial data
        # This is just an example. Adjust the scraping logic based on the actual data structure.
        data = []
        for row in soup.find_all('tr'):
            columns = row.find_all('td')
            if columns:  # Ensure there are columns in the row
                data.append([col.text.strip() for col in columns])

        return data

# Example usage
if __name__ == "__main__":
    # Replace with actual base URL for scraping (e.g., a financial reports URL)
    base_url = "https://www.sec.gov/edgar/searchedgar/companysearch.html"
    scraping_agent = ScrapingAgent(base_url)
    
    # Call the scraping function (replace with the actual endpoint you want to scrape)
    scraped_data = scraping_agent.scrape_data(endpoint="/search")
    
    # Print the scraped data
    print(scraped_data)
