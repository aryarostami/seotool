import requests
from bs4 import BeautifulSoup
import csv
import json
from selenium import webdriver

def get_page_metrics(url):
    try:
        # Initialize Chrome WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
        driver = webdriver.Chrome(executable_path="path_to_chromedriver_executable", options=options)

        # Start the timer
        start_time = time.time()

        # Send an HTTP GET request to the URL
        driver.get(url)

        # Capture a webpage screenshot
        screenshot_file = "screenshot.png"
        driver.save_screenshot(screenshot_file)

        # Calculate the loading time
        loading_time = time.time() - start_time

        # Parse the HTML content
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')

        # Calculate Total Page Size in kilobytes (KB)
        total_page_size_bytes = len(requests.get(url).text.encode('utf-8'))
        total_page_size_kb = total_page_size_bytes / 1024  # Convert bytes to kilobytes

        # Calculate Total Page Requests (count the number of requests in HTML)
        total_page_requests = len(soup.find_all('script')) + len(soup.find_all('link')) + len(soup.find_all('img'))

        return loading_time, total_page_size_kb, total_page_requests, screenshot_file
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None, None

if __name__ == "__main__":
    website_url = input("Enter the website URL: ")
    loading_time, total_page_size, total_page_requests, screenshot_file = get_page_metrics(website_url)

    if loading_time is not None:
        print(f"Loading Time: {loading_time:.2f} seconds")
        print(f"Total Page Size: {total_page_size:.2f} KB")
        print(f"Total Page Requests: {total_page_requests}")

        # Save the metrics to a CSV file
        with open("website_metrics.csv", "w", newline="", encoding="utf-8") as csv_file:
            fieldnames = ["Metric", "Value"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            writer.writerow({"Metric": "Loading Time (s)", "Value": loading_time})
            writer.writerow({"Metric": "Total Page Size (KB)", "Value": total_page_size})
            writer.writerow({"Metric": "Total Page Requests", "Value": total_page_requests})
        print("Metrics saved to 'website_metrics.csv'")

        # Save the metrics to a JSON file
        metrics_json = {
            "Loading Time (s)": loading_time,
            "Total Page Size (KB)": total_page_size,
            "Total Page Requests": total_page_requests
        }
        with open("website_metrics.json", "w", encoding="utf-8") as json_file:
            json.dump(metrics_json, json_file, ensure_ascii=False, indent=4)
        print("Metrics saved to 'website_metrics.json")

        print(f"Snapshot saved as '{screenshot_file}'")
    else:
        print("Failed to retrieve performance metrics.")
