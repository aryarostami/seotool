import requests
from bs4 import BeautifulSoup
import html5lib
import json
import csv

def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the page: {e}")
        return None

def validate_html(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html5lib')
        return True, None  # The HTML is valid
    except html5lib.html5parser.ParseError as e:
        return False, str(e)  # The HTML is invalid, return the error message

if __name__ == "__main__":
    website_url = input("Enter the website URL: ")
    webpage_content = fetch_webpage(website_url)

    if webpage_content:
        is_valid, error_message = validate_html(webpage_content)

        if is_valid:
            print("HTML is valid and adheres to HTML standards.")
        else:
            print("HTML contains errors and does not adhere to HTML standards.")
            print(f"Error Message: {error_message}")

            # Save the error information to a JSON file
            error_data = {
                "Website URL": website_url,
                "Error Message": error_message
            }
            with open('html_validation_errors.json', 'w', encoding='utf-8') as json_file:
                json.dump(error_data, json_file, ensure_ascii=False, indent=4)
            print("Error data saved to 'html_validation_errors.json'")

            # Save the error information to a CSV file
            with open('html_validation_errors.csv', 'w', newline='', encoding='utf-8') as csv_file:
                fieldnames = ["Website URL", "Error Message"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(error_data)
            print("Error data saved to 'html_validation_errors.csv'")
    else:
        print("Failed to retrieve the web page content.")
