import requests
import json

class SiteBase:
    def __init__(self, product_name, session):
        self.product_name = product_name
        self.session = session

class Scraper:
    def __init__(self, product_name):
        self.product_name = product_name
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

        self.sites = [
            Amazon(product_name, self.session),
            Noon(product_name, self.session),
            Jumia(product_name, self.session)
        ]

    def scrape_all(self):
        results = {}
        for site in self.sites:
            print(f"Scraping {site.__class__.__name__}")
            site_name = site.__class__.__name__.lower()
            try:
                reviews = site.scrape()
                results[site_name] = reviews
            except Exception as e:
                results[site_name] = f"Error: {str(e)}"
        return 200

class Amazon(SiteBase):
    def __init__(self, product_name, session):
        super().__init__(product_name, session)
        self.start_url = f'https://www.amazon.com/s?k={self.product_name}'

    def scrape(self):
        return 200

class Noon(SiteBase):
    def __init__(self, product_name, session):
        super().__init__(product_name, session)
        self.start_url = f'https://www.noon.com/egypt-ar/search/?q={self.product_name}'

    def scrape(self):
        return 200

class Jumia(SiteBase):
    def __init__(self, product_name, session):
        super().__init__(product_name, session)
        self.start_url = f'https://www.jumia.com.eg/ar/catalog/?q={self.product_name}'

    def scrape(self):
        return 200
