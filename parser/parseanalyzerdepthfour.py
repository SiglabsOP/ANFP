import requests
from bs4 import BeautifulSoup
from datetime import date

url = 'https://www.news-medical.net/condition/Autism'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all div elements with the specified class
    div_elements = soup.find_all('div', class_='col-xs-9')

    # Get today's date in the specified format
    today_date = date.today().strftime('%Y-%m-%d')

    # Write the headlines and URLs to a file with the specified format
    with open('autism_news.txt', 'w', encoding='utf-8') as report_file:
        report_file.write(f"{today_date}: Found headlines\n")

        for div_element in div_elements:
            # Find the <a> tag within the current <div> element
            a_tag = div_element.find('a')

            if a_tag:
                headline = a_tag.text.strip()
                url = 'https://www.news-medical.net' + a_tag['href']
                report_file.write(f"{headline}\t{url}\n")

        report_file.write('-' * 80 + '\n')

    print("Data written to autism_news.txt")
else:
    print(f"Error: Unable to retrieve data from {url}. Status code: {response.status_code}")
