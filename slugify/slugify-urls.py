from slugify import slugify

def slugify_url(url):
    # Remove the scheme (http:// or https://)
    if url.startswith("http://"):
        url = url[len("http://"):]
    elif url.startswith("https://"):
        url = url[len("https://"):]

    # Remove common URL prefixes (e.g., www.)
    url = url.lstrip("www.")

    # Slugify the remaining URL
    return slugify(url)

if __name__ == "__main__":
    url = input("Enter a URL: ")
    slug = slugify_url(url)
    print("Slugified URL:", slug)
    with open("Slugified-URL.txt", "w") as file:
        file.write(slug)
        print("Slugified-URL saved to 'Slugified-URL.txt' file.")
