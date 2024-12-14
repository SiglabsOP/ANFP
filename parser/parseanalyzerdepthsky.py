import requests
from bs4 import BeautifulSoup
from datetime import date
import re

url = 'https://news.sky.com/topic/autism-5901'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Send a GET request to the website SLOW BUT WORKS
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all article elements with the specified class
    article_elements = soup.find_all('article', class_='ui-story')

    # Get today's date in the specified format
    today_date = date.today().strftime('%Y-%m-%d')

    # Write the headlines and URLs to a temporary file with the specified format
    with open('sky_news_autism.txt', 'w', encoding='utf-8') as report_file:
        report_file.write(f"{today_date}: Found headlines\n")

        for article_element in article_elements:
            # Find the <a> tag within the current <article> element
            a_tag = article_element.find('a', href=True)

            if a_tag:
                headline = a_tag.get_text(strip=True)
                url = "https://news.sky.com" + a_tag['href']
                report_file.write(f"{headline}\t{url}\n")

        report_file.write('-' * 80 + '\n')

    print("Data written to sky_news_autism.txt")
else:
    print(f"Error: Unable to retrieve data from {url}. Status code: {response.status_code}")
