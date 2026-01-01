# Flask CRUD Web Application

## Overview
This project is a simple **Flask web application** that demonstrates basic **CRUD operations** (Create, Read, Update, Delete) using **SQLite** as the database and **SQLAlchemy** as the ORM.  
The app manages a list of tasks with fields: `id`, `title`, and `description`.

---

## Features
- Create new tasks
- View all tasks
- Edit existing tasks
- Delete tasks
- REST API endpoints for programmatic access

---

## Project Structure
├── app.py                 # Main Flask application<br/>
├── requirements.txt       # Dependencies<br/>
├── tasks.db               # SQLite database (auto-created)<br/>
└── templates/             # HTML templates<br/>

├── base.html<br/>
├── index.html<br/>
├── create.html<br/>
└── edit.html<br/>


---

## Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/your-username/flask-crud-app.git
cd flask-crud-app

# 2. Create a virtual environment

python -m venv .venv

# 2. Activate it:
# Linux/MacOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

flask --app app.py --debug run
```

Visit: http://127.0.0.1:5000

#### Example Usage
#### Web Interface
- Navigate to / to view all tasks
```bash
curl http://127.0.0.1:5000/api/tasks
```

- Use /create to add a new task
```bash
curl -X POST http://127.0.0.1:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn Flask","description":"CRUD demo"}'
```

- Use /edit/<id> to update a task
```bash
curl -X PATCH http://127.0.0.1:5000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn Flask fast"}'
```

- Delete tasks directly from the list view
```bash
curl -X DELETE http://127.0.0.1:5000/api/tasks/1
```