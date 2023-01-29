import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def save_images(url):
    # Make a request to the website and parse the HTML
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the links on the website
    links = [a.attrs.get('href') for a in soup.select('a[href]')]

    # Iterate over each link and check if it leads to an image
    for link in links:
        # Join the link with the base URL to form a full URL
        full_url = urljoin(url, link)

        # Make a request to the link and parse the HTML
        response = requests.get(full_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the images on the page
        images = [img.attrs.get('src') for img in soup.select('img[src]')]

        # Iterate over each image and save it to the local file system
        for img in images:
            response = requests.get(img)
            open(img.split('/')[-1], 'wb').write(response.content)

save_images('https://www.example.com')
