from celery import Celery
from scraper.scraper import scrape_site
from database.db import save_to_db

app = Celery("tasks", broker="redis://localhost:6379/0")

@app.task
def scheduled_scrape():
    url = "https://example.com"  # Replace with real site
    data = scrape_site(url)
    save_to_db(data)
