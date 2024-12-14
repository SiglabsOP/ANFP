import requests
from bs4 import BeautifulSoup
from datetime import date

url = 'https://www.nature.com/subjects/autism-spectrum-disorders'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Send a GET request to the website
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all article elements with the specified itemprop
    article_elements = soup.find_all('h3', class_='c-card__title')

    # Get today's date in the specified format
    today_date = date.today().strftime('%Y-%m-%d')

    # Write the headlines and URLs to a temporary file with the specified format
    with open('articlesnature.txt', 'a', encoding='utf-8') as report_file:
        report_file.write(f"{today_date}: Found headlines from {url}\n")

        for article_element in article_elements:
            # Find the <a> tag within the current <h3> element
            a_tag = article_element.find('a', itemprop='url')

            if a_tag:
                headline = a_tag.get_text(strip=True)
                url = "https://www.nature.com" + a_tag['href']
                report_file.write(f"{headline}\t{url}\n")

        report_file.write('-' * 80 + '\n')

    print("Data written to articlesnature.txt")
else:
    print(f"Error: Unable to retrieve data from {url}. Status code: {response.status_code}")
