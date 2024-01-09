import requests
from bs4 import BeautifulSoup
import json
import csv

def scrape_url_metadata(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title').text if soup.find('title') else None
        meta = soup.find('meta', attrs={'name': 'description'})
        description = meta['content'] if meta else None

        return {
            "URL": url,
            "Title": title,
            "Meta Description": description
        }
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while processing {url}: {e}")
        return None

if __name__ == "__main__":
    input_file = "urls.txt"  # Replace with your text file containing a list of URLs
    json_output_file = "metadata.json"
    csv_output_file = "metadata.csv"

    urls = []

    with open(input_file, "r") as file:
        urls = [line.strip() for line in file.readlines()]

    metadata = []

    for url in urls:
        data = scrape_url_metadata(url)
        if data:
            metadata.append(data)

    # Save metadata to JSON file
    with open(json_output_file, "w", encoding="utf-8") as json_file:
        json.dump(metadata, json_file, ensure_ascii=False, indent=4)
    print(f"URL metadata saved to {json_output_file}")

    # Save metadata to CSV file
    with open(csv_output_file, "w", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["URL", "Title", "Meta Description"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for data in metadata:
            writer.writerow(data)
    print(f"URL metadata saved to {csv_output_file}")
