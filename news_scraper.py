import requests
from bs4 import BeautifulSoup
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='news_scraper.log', level=logging.INFO)

def scrape_and_store_news(urls):
    unique_news_data = []  # Define the variable outside the try block

    try:
        # Iterate over each URL
        for url in urls:
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

                    # Check if the link exists
                    link_tag = article.find('a')
                    if link_tag:
                        link = link_tag.get('href')
                    else:
                        link = ""

                    # Extracting the description
                    description_tag = article.find_next('p')
                    description = description_tag.text.strip() if description_tag else ""

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
                logging.warning(f"No unique news data extracted from {url}.")
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

            logging.info(f"All news data from {url} successfully saved to all_news_data.json")

    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    # Example: List of URLs to scrape
    news_urls = ['https://indianexpress.com','https://indianexpress.com/section/cities/','https://indianexpress.com/section/india/','https://indianexpress.com/section/explained/','https://indianexpress.com/section/business/','https://indianexpress.com/section/entertainment/','https://indianexpress.com/section/sports/','https://indianexpress.com/section/political-pulse/','https://indianexpress.com/section/lifestyle/','https://indianexpress.com/section/technology/','https://indianexpress.com/section/research/',]

    # Call the function with the list of URLs
    scrape_and_store_news(news_urls)
