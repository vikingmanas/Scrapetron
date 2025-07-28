from celery import Celery

app = Celery("scrapetron", broker="redis://localhost:6379/0")
