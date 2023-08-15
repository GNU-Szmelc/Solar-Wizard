#!/usr/bin/env python3

import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Set the destination directory
destination_dir = os.path.expanduser("~/Pictures/Wallpapers/NASA_APOD")

# Create the directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Get the URLs of all daily photo pages from the archive page
archive_url = "https://apod.nasa.gov/apod/archivepixFull.html"
response = requests.get(archive_url)
soup = BeautifulSoup(response.content, "html.parser")
photo_page_urls = [urljoin(archive_url, a['href']) for a in soup.find_all('a', href=True)]

# Loop through the photo page URLs, extract image URLs, and download each image
for page_url in photo_page_urls:
    response = requests.get(page_url)
    page_soup = BeautifulSoup(response.content, "html.parser")
    
    image_element = page_soup.find('img')
    if image_element and 'src' in image_element.attrs:
        image_url = urljoin(page_url, image_element['src'])
        
        filename = os.path.basename(image_url)
        image_response = requests.get(image_url)
        with open(os.path.join(destination_dir, filename), 'wb') as f:
            f.write(image_response.content)
