import requests
from bs4 import BeautifulSoup
from datetime import date
import logging

# Configure logging
logging.basicConfig(filename='parser1errorsposnews.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

url = 'https://www.positive.news/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

try:
    # Send a GET request to the website
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all elements with the specified class containing headlines and URLs
        headline_elements = soup.find_all('a', class_='card__title')
        url_elements = [element['href'] for element in headline_elements]

        # Get today's date in the specified format
        today_date = date.today().strftime('%Y-%m-%d')

        # Write the headlines and URLs to a file with the specified format
        with open('positive_news.txt', 'w', encoding='utf-8') as report_file:
            report_file.write(f"{today_date}: Found headlines\n")

            for headline_element, url in zip(headline_elements, url_elements):
                headline = headline_element.text.strip()
                report_file.write(f"{headline}\t{url}\n")

            report_file.write('-' * 80 + '\n')

        print("Data written to positive_news.txt")
    else:
        print(f"Error: Unable to retrieve data from {url}. Status code: {response.status_code}")
        logging.error(f"Error: Unable to retrieve data from {url}. Status code: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
    logging.error(f"Error: {e}")
