# ACEest Fitness & Gym — DevOps Assignment

A minimal Flask API demonstrating core DevOps practices: Git/GitHub, unit tests with Pytest, containerization with Docker, and CI/CD using GitHub Actions.

## Features
- **Flask API** with health check and a BMI calculator (`/bmi`).
- **Pytest** unit tests.
- **Docker** image with app + tests bundled.
- **GitHub Actions** pipeline builds the image and **executes tests inside the container** on every push/PR.

---

## Local Setup (Python)
```bash
# Python 3.12+ recommended
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run the API
python app.py
# or
flask --app app run --debug
```

Open: http://localhost:5000/health

### Sample usage
```bash
curl -X POST http://localhost:5000/bmi \      -H "Content-Type: application/json" \      -d '{"weight_kg": 80, "height_cm": 180}'
```

---

## Run Tests Locally
```bash
pytest -q
```

---

## Docker (Build & Run)
```bash
docker build -t aceest-fitness:local .
# Run API
docker run --rm -p 5000:5000 aceest-fitness:local
# Run tests *inside the image*
docker run --rm aceest-fitness:local pytest -q
```

---

## CI/CD with GitHub Actions
On every **push** or **pull request**, the workflow:
1. Checks out the repo
2. Builds the Docker image
3. Runs `pytest` inside the built image

See: `.github/workflows/ci.yml`

---

## Git & GitHub Quickstart
```bash
git init
git add .
git commit -m "Initial commit: Flask app, tests, Docker, CI"
# Create a new repo on GitHub (via web UI) and copy its URL, then:
git remote add origin https://github.com/<your-username>/aceest-fitness-gym.git
git branch -M main
git push -u origin main
```

Ensure the repository is **public** so reviewers can see the code and Actions runs.

---

## Endpoints
- `GET /health` → `{"status":"ok"}`
- `POST /bmi` (JSON: `weight_kg`, `height_cm`) → BMI + category

---

## Notes
- Default container command runs the API with Gunicorn.
- Tests are included in the image so CI can execute them by overriding the container command to `pytest`.
- If you already have a starter Flask file, you can swap it into `app.py` (ensure the WSGI object is named `app`).
