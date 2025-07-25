import requests
from bs4 import BeautifulSoup
from src.models import Product
from config.config import Config
import logging
import time 
from urllib.parse import urljoin

class Scraper:
    def __init__(self):
        self.url = Config.TARGET_URL
        self.headers = {
            'User-Agent': Config.USER_AGENT
        }
    
    def fetch_page(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.encoding = 'utf-8'
            response.raise_for_status()
            logging.info(f"Fetched page: {self.url}")
            return response.text
        except requests.RequestException as e:
            logging.error(f"Error fetching page: {e}")
            raise
    
    def parse_page(self, html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            products = []
            for item in soup.select('article.product_pod'):
                name = item.select_one('h3 a')['title']
                price = float(item.select_one('.price_color').text.strip('£'))
                description = item.select_one('.product_description').text.strip() if item.select_one('.product_description') else ""
                products.append(Product(name, price, description))
            logging.info(f"Parsed {len(products)} books")
            return products
        except Exception as e:
            logging.error(f"Error parsing page: {e}")
            raise
    
    def scrape(self):
        products = []
        url = self.url
        while url:
            html = self.fetch_page(url)
            products.extend(self.parse_page(html))
            soup = BeautifulSoup(html, 'html.parser')
            next_page = soup.select_one('.next a')
            url = urljoin(url, next_page['href']) if next_page else None
            time.sleep(1)
        return products