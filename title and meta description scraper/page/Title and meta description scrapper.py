import requests
from bs4 import BeautifulSoup
import json

def get_title_and_meta(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text if soup.find('title') else None
    meta = soup.find('meta', attrs={'name': 'description'})
    description = meta['content'] if meta else None

    return {
        "Title": title,
        "Meta Description": description
    }

if __name__ == "__main__":
    url = input("Enter a website URL: ")
    data = get_title_and_meta(url)

    if data:
        with open("URL_Title_Desription.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print("Title and Meta Description data saved to 'website_info.json' using UTF-8 encoding.")
    else:
        print("No title or meta description found on the website.")
