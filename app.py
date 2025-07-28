from scraper.scraper import scrape_site
from database.db import save_to_db

if __name__ == "__main__":
    url = "https://example.com" 
    data = scrape_site(url)
    save_to_db(data)
    print("✅ Scraping and saving complete.")
