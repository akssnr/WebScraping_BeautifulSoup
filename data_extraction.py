# Importing the important libraries

import pandas as pd
import csv
import json
import requests
from bs4 import BeautifulSoup

# Function to extract useful data and basic clean of data from url

def scrape_data(url):
    try:
        # send the 'GET' request to the url
        response = requests.get(url)
        if response.status_code == 200:
            print('Data Fetching Started')
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract text and basic cleaning
            text = ' '.join([text.get_text() for text in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])])
            text = text.replace('\n',"").replace('\t','')
            
            # Extract image urls from the url
            image_urls = [img['src'] for img in soup.find_all('img') if 'src' in img.attrs]
            
            # Extract link urls from the url
            # link_urls = [link['href'] for link in soup.find_all('a') if 'href' in link.attrs]
            link_urls = [link['href'] for link in soup.find_all('a', href=True) if link['href'].startswith('https:')]
                         
            # Extract Title from the url
            title = [title.text for title in soup.find('title')]

            print(f'Data fetching Successful from {url}')
                         
            return {
                'URLS': url,
                'TITLE' : title,
                'TEXT': text,
                'IMAGE LINKS': ', '.join(image_urls),
                'WEB LINKS': ', '.join(link_urls)
            }
        else:
            print(f"Failed to fetch content from {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while extracting content from {url}: {e}")
        return None


def main(): 
    # List to store the extracted data
    data = []
    # Load the url from the excel file provided with no headers
    df = pd.read_excel('urls.xlsx', header=None) 
    for url in df[0]:  
        extraction = scrape_data(url)
        if extraction:
            data.append(extraction)
        else:
            print(f'Skipping URL : {url} due to missing content/article ')
    
    # Store the data in CSV format
    csv_path = 'scraped_data.csv'
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['URLS','TITLE', 'TEXT', 'IMAGE LINKS', 'WEB LINKS']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for info in data:
            writer.writerow(info)

    # Store the data in JSON format
    json_path = 'scraped_data.json'
    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)

    print("Data stored successfully in CSV and JSON formats.")

        
if __name__ == '__main__': 
    main()