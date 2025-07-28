from fastapi import FastAPI
from scheduler.tasks import start_scraping_task

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Scrapetron is alive!"}

@app.get("/scrape")
def trigger_scrape(url: str):
    task = start_scraping_task.delay(url)
    return {"status": "Scraping started", "task_id": task.id}
