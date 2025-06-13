import requests
import json

class Scraper():
    def __init__(self, product_name):
        self.product_name = product_name
        self.session = requests.Session()
        self.sites = [
            Amazon(product_name),
            Noon(product_name),
            Jumia(product_name)
        ]

    def scrape_all(self):
        results = {}
        for site in self.sites:
            site_name = site.__class__.__name__.lower()
            try:
                reviews = site.scrape()
                results[site_name] = reviews
            except Exception as e:
                results[site_name] = f"Error: {str(e)}"
        return results

class Amazon(Scraper):
    def __init__(self ):
        super().__init__()
        self.start_urls = f'https://www.amazon.com/s?k={self.product_name}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.session.headers.update(self.headers)

    def scrape(self):
        pass

class Noon(Scraper):
    def __init__(self ):
        super().__init__()
        self.start_urls = f'https://www.noon.com/egypt-ar/search/?q={self.product_name}'

    def scrape(self):
        pass

class Jumia(Scraper):
    def __init__(self ):
        super().__init__()
        self.start_urls = f'https://www.jumia.com.eg/ar/catalog/?q={self.product_name}'

    def scrape(self):
        pass
