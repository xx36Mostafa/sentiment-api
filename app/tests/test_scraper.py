from app.services import scraper

def test_scraper():
    scrape = scraper.Scraper('Golden Boy')
    assert scrape.scrape_all() == 200