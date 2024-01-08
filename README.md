
# News Search

News Search is a web application that allows users to search and browse through the latest news articles. It includes a web scraper (`news_scraper.py`) for collecting news data and a search functionality (`news_search.py`) using the Whoosh search engine.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Sashank-Krovvidi/News-Search.git
   cd News-Search
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the web scraper to collect news data:

   ```bash
   python news_scraper.py
   ```

2. Start the Flask application:

   ```bash
   python app.py
   ```

   The application will be accessible at `http://localhost:5000`.

3. Access the web application in your web browser.

## Folder Structure

- `__pycache__`: Compiled Python files (automatically generated).
- `indexdir`: Directory to store the Whoosh search engine index.
- `static`: Static files such as stylesheets.
- `templates`: HTML templates for Flask.
- `all_news_data.json`: JSON file containing the collected news data.
- `app.py`: Main Flask application.
- `news_scraper.py`: Web scraper for collecting news data.
- `news_search.py`: Module for creating a search index and performing searches.
- `README.md`: Project documentation.
- `requirements.txt`: List of Python dependencies.
- `news_scraper.log`: Log file for the web scraper.

## Dependencies

- [Flask](https://flask.palletsprojects.com/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Whoosh](https://whoosh.readthedocs.io/)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
