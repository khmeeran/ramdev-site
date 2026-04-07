import requests
from bs4 import BeautifulSoup
import os
import time
from urllib.parse import urljoin, urlparse

BASE_URL = "https://aarimaterials.com/"
DOMAIN = urlparse(BASE_URL).netloc
SAVE_DIR = "aarimaterials_images"

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

visited_urls = set()
image_urls = set()

def get_links(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return []
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all internal links
        links = []
        for a in soup.find_all('a', href=True):
            link = urljoin(url, a['href'])
            parsed_link = urlparse(link)
            if parsed_link.netloc == DOMAIN and parsed_link.path.startswith('/') and '#' not in link:
                links.append(link)
        
        # Find all images
        for img in soup.find_all('img'):
            src = img.get('src')
            if src:
                img_url = urljoin(url, src)
                # Try to get larger versions if it's a thumbnail
                # WooCommerce common pattern: -100x100.jpg, -300x300.jpg, -600x600.jpg
                import re
                original_url = re.sub(r'-\d+x\d+(\.[a-z]+)$', r'\1', img_url)
                image_urls.add(original_url)
                image_urls.add(img_url)

        return links
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

def crawl(start_url, max_pages=100):
    to_visit = [start_url]
    count = 0
    while to_visit and count < max_pages:
        url = to_visit.pop(0)
        if url in visited_urls:
            continue
        print(f"Crawling: {url}")
        visited_urls.add(url)
        new_links = get_links(url)
        for link in new_links:
            if link not in visited_urls and link not in to_visit:
                to_visit.append(link)
        count += 1
        time.sleep(0.1) # Be nice to the server

crawl(BASE_URL, max_pages=500) # Increased to 500 to be more thorough

print(f"Found {len(visited_urls)} pages.")
print(f"Found {len(image_urls)} unique image URLs.")

# Save the image URLs to a file
with open("image_urls.txt", "w") as f:
    for url in image_urls:
        f.write(url + "\n")
