# Scrapetron 🕷️📦

A powerful and scalable web scraping microservice built with FastAPI, Celery, Redis, and SQLite. Automate and schedule scraping tasks with ease, and store the results directly into a lightweight database.

---

## 🚀 Features

- 🔧 Scrapes data from websites via FastAPI endpoints  
- 🧠 Background scraping with Celery  
- 🧊 Redis broker for task queue  
- 🗃️ SQLite database for data persistence  
- 📅 Scheduled scraping support  
- ⚡ Hot reload during development  

---

## 🛠️ Tech Stack

- Python 🐍  
- FastAPI ⚡  
- Celery 🎡  
- Redis 🟥  
- SQLite 🗂️  

---

## 📂 Project Structure

```
Scrapetron/
│
├── database/
│   └── db.py             # Handles database operations
│
├── scraper/
│   └── scraper.py        # Website scraping logic
│
├── tasks/
│   └── tasks.py          # Celery tasks
│
├── server.py             # FastAPI server setup
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/vikingmanas/Scrapetron.git
cd Scrapetron
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start Redis server

Open a new terminal and run:
```bash
redis-server
```

If you face an error about bind or ports, use this instead:
```bash
redis-server.exe
```

### 4. Start the FastAPI server
```bash
uvicorn server:app --reload
```

Access: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 5. Start Celery worker
```bash
celery -A tasks.tasks worker --loglevel=info
```

---

## 🧪 Testing the API

Use any tool like Postman or your browser:

- `GET /` – Check if server is running  
- `GET /scrape` – Triggers a sample scrape and returns result

---

## 📌 To-Do

- [ ] Add logging  
- [ ] Add authentication  
- [ ] Deploy to cloud  
- [ ] Add scraping customization via parameters  

---

## 👤 Author

Made with ❤️ by [Manas Dubey](https://github.com/vikingmanas)  
Let's connect and grow together 🚀

---

## 📄 License

MIT License – do whatever you want but give credit!

