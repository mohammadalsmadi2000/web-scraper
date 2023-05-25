# Wikipedia Citations Scraper

## Author: `Mohammad Al-Smadi`

This Python script allows you to scrape a Wikipedia page and retrieve the passages that need citations. It provides functions to count the number of citations needed and generate a report listing the passages.

## How to Use

1. Make sure you have Python installed on your system.
2. Install the required dependencies by running the following command:
3. Download the `scraper.py` file from this repository.
4. Import the `WikipediaScraper` class from `scraper.py` in your Python script.
5. Create an instance of the `WikipediaScraper` class.
6. Use the available methods to interact with the Wikipedia scraper:
- `get_citations_needed_count(url)`: Retrieves the count of citations needed on a Wikipedia page.
- `get_citations_needed_report(url)`: Generates a report listing the passages that need citations on a Wikipedia page.
- `create_report_file(url, filename)`: Creates a Markdown file with the citations report.

Please note that this code can be used for any Wikipedia page that has citations needed. Simply provide the URL of the desired Wikipedia page as an argument when calling the relevant methods.

