import requests
import os
import concurrent.futures
from urllib.parse import urlparse

SAVE_DIR = "aarimaterials_images"
URL_FILE = "image_urls.txt"

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

def download_image(url):
    try:
        url = url.strip()
        if not url:
            return
        
        # Get filename from URL
        path = urlparse(url).path
        filename = os.path.basename(path)
        if not filename:
            return
            
        save_path = os.path.join(SAVE_DIR, filename)
        
        # Skip if already exists
        if os.path.exists(save_path):
            return
            
        response = requests.get(url, timeout=15, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download {url}: Status {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def main():
    with open(URL_FILE, 'r') as f:
        urls = list(set(f.readlines())) # Remove duplicates
    
    print(f"Starting download of {len(urls)} images...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download_image, urls)

if __name__ == "__main__":
    main()
