# Aircraft Performance Simulator

Beginner-friendly full-stack aerospace project.

## Stack
- Python + Flask: backend/API and calculations
- HTML/CSS/JavaScript: frontend
- NumPy: numerical calculations
- Plotly.js: interactive graphs

## Features
Lift, drag, stall speed, estimated takeoff speed, thrust-to-weight ratio, takeoff velocity/acceleration, CL/CD vs angle of attack, L/D, and sensitivity to mass, thrust, wing area and air density. The dashboard shows all graphs at once.

## Run
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install -r backend/requirements.txt
cd backend
python app.py
```
Open `http://127.0.0.1:5000`.

## GitHub
```bash
git init
git add .
git commit -m "Aircraft performance simulator"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

This is an educational simplified model, not a certified aircraft-performance tool.
