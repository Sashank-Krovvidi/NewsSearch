import requests
from bs4 import BeautifulSoup
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='news_scraper.log', level=logging.INFO)

def scrape_and_store_news(pages=10):
    unique_news_data = []  # Define the variable outside the try block

    for page_number in range(6, pages + 1):
        try:
            url = f'https://indianexpress.com/section/india/page/{page_number}/'
            
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad responses
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract relevant information from the HTML using BeautifulSoup
            # Modify this part according to the structure of the website you're scraping

            # Example: Extracting titles, links, and descriptions
            news_data = []
            for article in soup.select('.title'):
                try:
                    title = article.text.strip()
                    link = article.find('a')['href']

                    # Extracting the description
                    description = article.find_next('p').text.strip() if article.find_next('p') else ""

                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    # Add data to the list
                    news_data.append({
                        'title': title,
                        'link': link,
                        'description': description,
                        'timestamp': timestamp
                    })
                except AttributeError as e:
                    logging.warning(f"Error extracting data from an article: {e}")

            if not news_data:
                logging.warning(f"No unique news data extracted from page {page_number}.")
                continue

            # Load existing news data from the file, if it exists
            existing_news_data = []
            try:
                with open('all_news_data.json', 'r', encoding='utf-8') as existing_file:
                    existing_news_data = json.load(existing_file)
            except FileNotFoundError:
                pass

            # Combine the new and existing news data
            all_news_data = existing_news_data + news_data

            # Remove duplicates based on title and link
            seen_entries = set()
            unique_news_data = []
            for entry in all_news_data:
                if isinstance(entry, dict):  # Ensure entry is a dictionary
                    title_link_tuple = (entry.get('title'), entry.get('link'))
                    if title_link_tuple not in seen_entries:
                        seen_entries.add(title_link_tuple)
                        unique_news_data.append(entry)

            # Save all news data to a JSON file
            with open('all_news_data.json', 'w', encoding='utf-8') as file:
                json.dump(unique_news_data, file, ensure_ascii=False, indent=2)

            logging.info(f"All news data from page {page_number} successfully saved to all_news_data.json")

        except Exception as e:
            logging.error(f"An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    # Specify the number of pages you want to scrape (adjust as needed)
    scrape_and_store_news(pages=5)
