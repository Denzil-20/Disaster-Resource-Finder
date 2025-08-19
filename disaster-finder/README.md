# 🌍 Disaster Resource Finder

A Flask + Leaflet.js + OpenStreetMap project that helps users find disaster resources (shelters, hospitals, relief camps, etc.) on an interactive map.

## 🚀 Features
- Interactive map with OpenStreetMap
- Resource search (e.g., "hospital", "shelter")
- SQLite database for storing resources
- Flask API backend

## 📂 Project Structure
- `app.py` → Flask app
- `instance/resources.db` → SQLite database
- `templates/resources.html` → Frontend HTML
- `static/css/style.css` → Styles
- `static/js/map.js` → Map logic

## ⚙️ Setup Instructions
```bash
git clone https://github.com/your-username/disaster-finder.git
cd disaster-finder
python -m venv .venv
.venv\Scripts\activate   # (Windows)
pip install -r requirements.txt
python app.py
```

Now visit 👉 `http://127.0.0.1:5000/`
