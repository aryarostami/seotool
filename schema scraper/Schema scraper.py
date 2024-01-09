import requests
from bs4 import BeautifulSoup
# Get the URL input from the user
url = input("Enter the URL of the page to retrieve schema information: ")
# Send a request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text
# Use beautifulsoup4 to parse the HTML content and find the schema information
soup = BeautifulSoup(html_content, 'html.parser')
schema_tags = soup.find_all('script', attrs={'type': 'application/ld+json'})
# Print the schema information for each tag found
for schema_tag in schema_tags:
    schema_data = schema_tag.string.strip()
print(schema_data)
with open("Schema-Scrapper.txt", "w", encoding="utf-8") as file:
    file.write(schema_data)
    print("Schema saved to 'Schema-Scrapper.txt' file.")