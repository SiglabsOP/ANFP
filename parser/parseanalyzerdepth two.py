import requests
from bs4 import BeautifulSoup
from datetime import date

url = 'https://autismspectrumnews.org/'

# Send a GET request to the website SEEMS TO WORK
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all dd elements containing h3 tags
    dd_h3_elements = soup.select('dd h3')

    # Get today's date in the specified format
    today_date = date.today().strftime('%Y-%m-%d')

    # Write the headlines and URLs to a file with the specified format
    with open('reportdepth2.txt', 'w', encoding='utf-8') as report_file:
        report_file.write(f"{today_date}: {len(dd_h3_elements)} headlines\n")

        for dd_h3_element in dd_h3_elements:
            # Find the anchor tag within the current dd_h3_element
            anchor_tag = dd_h3_element.find('a')

            if anchor_tag:
                headline = anchor_tag.text.strip()
                url = anchor_tag.get('href', '')
                report_file.write(f"{headline}\t{url}\n")

        report_file.write('-' * 80 + '\n')

    print("Data written to reportdepth2.txt")
else:
    print(f"Error: Unable to retrieve data from {url}. Status code: {response.status_code}")
