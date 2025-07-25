# 🤖 Scrapetron

Scrapetron is an automated web scraping tool designed to extract data from dynamic websites on a scheduled basis. Built using Selenium, BeautifulSoup, Celery, and SQLite, it enables reliable data collection and periodic scraping for real-time insights.

## 🚀 Features
- Dynamic web scraping using Selenium
- BeautifulSoup-based content parsing
- Task scheduling with Celery + Redis
- Data storage in SQLite and export to CSV
- Modular and extensible codebase

## 🛠️ Tech Stack
- **Python**, **Selenium**, **BeautifulSoup**
- **Celery**, **Redis**, **SQLite**, **CSV**
- Optional: Flask UI or API endpoint

## 📦 Use Cases
- Price monitoring
- Job listings aggregation
- News scraping
- Product updates tracking

## 📂 Repository Structure
- `scraper/` - Core scraping logic
- `scheduler/` - Celery task definitions
- `database/` - DB and CSV handlers
- `app.py` - Entry script for manual scraping
- `celery_config.py` - Celery settings

## 🧠 How it Works
1. Celery schedules scraping jobs periodically.
2. Scrapetron loads dynamic content with Selenium.
3. BeautifulSoup parses relevant data.
4. Data is saved to SQLite and/or exported as CSV.

## 🧪 Run Locally
```bash
# 1. Start Redis
redis-server

# 2. Launch Celery worker
celery -A scheduler.tasks worker --loglevel=info

# 3. Run manual scrape
python app.py
