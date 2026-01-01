# Flask WebApp with SQLAlchemy

This project is a simple Flask web application using SQLAlchemy.  
Below are setup instructions and a consolidated troubleshooting guide — all in one page.

---

## 🚀 Setup Instructions

### 1. Install Python (Windows, 64‑bit x64)
- Download Python 3.12 (64‑bit installer) from [python.org](https://www.python.org/downloads/).
- Run installer:
  - ✅ Check **Add Python to PATH**
  - ✅ Choose **Install for all users**

Verify installation:
```powershell
python --version
# Expected: Python 3.12.x
```
#### 2. Create Virtual Environment
```powershell
python -m venv .venv
OR
> & "C:\Users\muthu\AppData\Local\Programs\Python\Python312\python.exe" -m venv .venv
> .\.venv\Scripts\Activate.ps1
```

#### 3. Install Dependencies
```powershell
pip install Flask Flask-SQLAlchemy SQLAlchemy
```

#### 4. Run the App
```powersheel
flask --app app.py --debug run
```

## 🛠️ Troubleshooting Guide

- IntelliJ Interpreter Setup
- Go to File → Settings → Project → Python Interpreter
- Add Interpreter → System Interpreter
`C:\Users\<user>\AppData\Local\Programs\Python\Python312\python.exe`
- Or choose Virtualenv Environment → New → based on Python 3.12.

## ✅ Summary
- Always use Python 3.12 (64‑bit) for compatibility.
- Activate venv with PowerShell’s Activate.ps1.
- Point IntelliJ to the correct interpreter.
