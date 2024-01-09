import requests
from bs4 import BeautifulSoup
import json
import csv


def get_google_search_results(query, num_results=10):
    url = f"https://www.google.com/search?q={query}&&num=100"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('div', class_='tF2Cxc')

        results_data = []

        # Extract and print the search results
        for i, result in enumerate(search_results[:num_results]):
            title = result.find('h3').text
            link = result.find('a')['href']
            print(f" {i + 1}: {title}\nLink: {link}\n")
            results_data.append({
                "Rank": i + 1,
                "Title": title,
                "Link": link
            })

        # Save results to JSON
        with open('Page_Keyword_website.json', 'w', encoding='utf-8') as json_file:
            json.dump(results_data, json_file, ensure_ascii=False, indent=4)
        print(f"Results saved to 'Page_Keyword_website.json'")

        # Save results to CSV
        with open('Page_Keyword_website.csv', 'w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ["Rank", "Title", "Link"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for result in results_data:
                writer.writerow(result)
        print(f"Results saved to 'Page_Keyword_website.csv'")

        return search_results

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    website = input("Enter the website URL: ")
    keyword = input("Enter the keyword to track: ")
    num_results = int(input("Number of results to check (1 to 100): "))

    query = f"{keyword} site:{website}"
    get_google_search_results(query, num_results)
