# Web Scraping Project Using Beautiful Soup

This project involves extracting and cleaning data from websites listed in an Excel file, and then saving the cleaned data in both CSV and JSON formats. The Python script uses libraries such as `pandas`, `requests`, and `BeautifulSoup` to perform web scraping and data handling.

## Environment Setup Instructions:

## 1. Install Python
Make sure you have Python installed on your computer. You can download and install it from [python.org](https://www.python.org/downloads/). Ensure you add Python to your system's PATH during installation.

## Features
- Fetch and clean text, image links, and other links from specified URLs.
- Save extracted data into structured CSV and JSON formats.
- Handles exceptions and errors gracefully, providing feedback on the success or failure of data extraction.

## Dependencies
To run this project, you will need to have the following Python libraries installed:
- `pandas`: For loading URLs from an Excel file.
- `requests`: For sending HTTP requests to web pages.
- `bs4` (BeautifulSoup): For parsing HTML and extracting data.
- `csv`: For writing data to CSV files.
- `json`: For writing data to JSON files.

You can install these dependencies via pip:
```
pip install json 
pip install csv
pip install pandas 
pip install requests 
pip install beautifulsoup4
```

## How to Run the Script
1. Ensure you have an Excel file named `urls.xlsx` in your project directory. This file should contain URLs in the first column with no headers.
2. Place the script in the same directory as the Excel file.
3. Run the script using Python:
   ```
   python data_extraction.py
   ```

## Output Files

After the script completes execution, check the same directory for `scraped_data.json` and `scraped_data.csv` files containing the scraped data.

- `scraped_data.csv`: Contains the scraped data in CSV format with columns for URL, title, text, image links, and web links.
- `scraped_data.json`: Contains the same data in a JSON format, providing an easy-to-read and structured data representation.

## Function Descriptions
- `scrape_data(url)`: This function takes a URL as input, extracts text, images, and web links, and then returns a dictionary containing cleaned and organized data.
- `main()`: This function reads URLs from an Excel file, calls `scrape_data()` for each URL, and writes the results to CSV and JSON files.

## Possible Improvements
- Implementing more robust error handling and retries for network failures.
- Adding configuration options for user-defined output file paths or formats.
- Expanding the data extraction features to include metadata or other HTML elements.
- Optimizing the script for better performance with asynchronous requests.

## Limitations
- The script assumes that the Excel file and the script are in the same directory.
- Only processes URLs that start with "https:".
- Might not handle dynamically loaded content that requires JavaScript execution.

This project is a simple demonstration of web scraping techniques using beautiful soup , as a basis for more complex web data extraction tasks.