# An AI agent that scrapes and displays top news headlines from a website

import requests
from bs4 import BeautifulSoup

def news_scraper_agent(url="https://www.bbc.com/news"):
    """
    Scrapes the top headlines from a news website and prints them.

    Args:
        url (str): The URL of the news website to scrape.
    """
    print("🤖 Fetching the latest news headlines for you...")

    try:
        # 1. Send a request to download the webpage
        # Using headers to mimic a real browser visit
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        # Raise an error if the request was unsuccessful
        response.raise_for_status()

        # 2. Parse the webpage's HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # 3. Find the headlines
        # This part is specific to the website's structure and needs to be updated when the site changes.
        # UPDATED SELECTOR: Instead of looking for a fragile class name, we now look for
        # anchor (<a>) tags where the link (href) contains "/news/articles/".
        # This is a much more stable way to identify actual news story links.
        links = soup.select('a[href*="/news/articles/"]')
        
        # We use a set to store headlines to avoid duplicates
        headlines = set()
        for link in links:
            # Get the text and remove leading/trailing whitespace
            headline_text = link.get_text(strip=True)
            # Add to set only if it's a non-empty string
            if headline_text:
                headlines.add(headline_text)

        if not headlines:
            print("Could not find any headlines. The website structure might have changed again.")
            return

        print("\n--- Top Headlines ---")
        # 4. Loop through the found headlines and print their text
        # We convert the set to a list to slice it for the top 10
        for i, headline in enumerate(list(headlines)[:10], 1):
            print(f"{i}. {headline}")
        print("---------------------\n")

    except requests.exceptions.RequestException as e:
        print(f"Error: Could not connect to the website. Please check your internet connection.")
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # You can change the URL to another news source, but the scraping logic
    # (step 3) would likely need to be adjusted for that site's HTML structure.
    news_scraper_agent()
