import requests
from bs4 import BeautifulSoup
from datetime import date
import os
import re

url = 'https://theconversation.com/europe/topics/autism-533'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Send a GET request to the website
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all article elements with the specified class
    article_elements = soup.find_all('article', class_='clearfix')

    # Get today's date in the specified format
    today_date = date.today().strftime('%Y-%m-%d')

    # Write the headlines and URLs to a temporary file with the specified format
    with open('eight.txt', 'w', encoding='utf-8') as report_file:
        report_file.write(f"{today_date}: Found headlines\n")

        for article_element in article_elements:
            # Find the <a> tag within the current <article> element
            a_tag = article_element.find('a', class_='article-link')

            if a_tag:
                headline = a_tag['aria-label']
                # Remove <span> tags from the headline using regular expressions
                headline = re.sub(r'<span[^>]*>(.*?)</span>', '', headline)
                url = "https://theconversation.com" + a_tag['href']
                report_file.write(f"{headline.strip()}\t{url}\n")

        report_file.write('-' * 80 + '\n')

    print("Data written to eight.txt")
else:
    print(f"Error: Unable to retrieve data from {url}. Status code: {response.status_code}")
