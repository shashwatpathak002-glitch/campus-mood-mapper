# 🚀 Campus Mood Mapper - Multi-Platform Deployment Guide

## Overview

Campus Mood Mapper can be deployed on **multiple platforms** beyond Streamlit. This guide covers:

- **FastAPI Backend** - REST API for decoupled architecture
- **Render.com** - Modern cloud platform (Heroku replacement)
- **Railway.app** - Simple, developer-friendly deployment
- **PythonAnywhere** - Instant Python web hosting
- **Fly.io** - Global application distribution
- **AWS** - Scalable enterprise solution
- **Docker Compose** - Local orchestration

---

## 🔧 1. FASTAPI BACKEND (api.py)

### What is FastAPI?

FastAPI is a modern Python web framework for building APIs, compatible with all deployment platforms.

### Running Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
python api.py

# API will be available at: http://localhost:8000
# Auto-generated documentation: http://localhost:8000/docs
```

### API Endpoints

#### POST `/api/v1/mood/analyze`
Analyze a mood entry and get AI-driven interventions.

```bash
curl -X POST "http://localhost:8000/api/v1/mood/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "I'm feeling anxious about exams",
    "mood_score": 3,
    "user_id": "student_123",
    "location": "Library"
  }'
```

#### POST `/api/v1/mood/log`
Log a mood entry in the database.

```bash
curl -X POST "http://localhost:8000/api/v1/mood/log" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Had a good day today",
    "mood_score": 7,
    "user_id": "student_456",
    "location": "Cafe"
  }'
```

#### GET `/api/v1/moods/{user_id}`
Retrieve all mood entries for a user.

```bash
curl http://localhost:8000/api/v1/moods/student_123
```

#### GET `/api/v1/trends/{user_id}`
Get mood trends and analytics.

```bash
curl http://localhost:8000/api/v1/trends/student_123
```

#### GET `/api/v1/recommendations/{user_id}`
Get personalized recommendations.

```bash
curl http://localhost:8000/api/v1/recommendations/student_123
```

---

## ☁️ 2. RENDER.COM DEPLOYMENT

Render is a modern cloud platform perfect for replacing Heroku.

### Step 1: Prepare Your Repository

Make sure your repo has:
- `api.py` (Flask/FastAPI app)
- `requirements.txt`
- `Dockerfile` (optional, recommended)

### Step 2: Connect GitHub to Render

1. Go to [render.com](https://render.com)
2. Click **"New +" → "Web Service"**
3. Select **"Connect a repository"** → Choose your GitHub repo
4. Configure:
   - **Name**: `campus-mood-mapper`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python api.py`
   - **Port**: `8000`

### Step 3: Set Environment Variables

In Render Dashboard → Environment:
```
PLATFORM=render
PORT=8000
```

### Step 4: Deploy

Click **"Deploy"** - your app will be live in 2-3 minutes!

**Your URL**: `https://campus-mood-mapper.onrender.com`

### Monitoring

- View logs: Dashboard → **Logs**
- Health check: `https://campus-mood-mapper.onrender.com/health`

---

## 🚂 3. RAILWAY.APP DEPLOYMENT

Railway offers a simple Git-to-deploy experience.

### Step 1: Create Railway Project

1. Go to [railway.app](https://railway.app)
2. Click **"New Project" → "Deploy from GitHub"**
3. Authorize and select your repo
4. Railway auto-detects `requirements.txt`

### Step 2: Configure

Railway automatically configures:
- Python runtime detection
- Port mapping (Railway uses PORT env var)
- Health checks

### Step 3: Add Variables (if needed)

```
PLATFORM=railway
```

### Step 4: Deploy

Railway deploys automatically on push. View your URL in the Railway Dashboard.

**Your URL**: `https://*.railway.app`

---

## 📚 4. PYTHONANYWHERE DEPLOYMENT

PythonAnywhere is ideal for beginners and simple apps.

### Step 1: Create Account

Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)

### Step 2: Upload Files

1. Go to **Files**
2. Create folder `/mysite`
3. Upload:
   - `api.py`
   - `requirements.txt`
   - `mood_analysis.py`
   - `personalization.py`

### Step 3: Create Web App

1. Go to **Web**
2. Click **"Add a new web app"**
3. Select **"Python 3.x" → "Flask"**
4. Edit WSGI file:

```python
import sys
sys.path.insert(0, '/home/yourusername/mysite')
from api import app
application = app
```

### Step 4: Install Requirements

In PythonAnywhere console:
```bash
cd /home/yourusername/mysite
pip install --user -r requirements.txt
```

### Step 5: Reload Web App

Click **"Reload"** in Web tab.

**Your URL**: `https://yourusername.pythonanywhere.com`

---

## 🪰 5. FLY.IO DEPLOYMENT (Modern Alternative)

Fly.io distributes your app globally with auto-scaling.

### Step 1: Install Fly CLI

```bash
curl -L https://fly.io/install.sh | sh
```

### Step 2: Initialize Project

```bash
fly launch
```

Answer prompts:
- App name: `campus-mood-mapper`
- Region: Select closest to you
- Postgres: No (use in-memory for now)

### Step 3: Deploy

```bash
fly deploy
```

**Your URL**: `https://campus-mood-mapper.fly.dev`

### Monitoring

```bash
fly logs
fly status
```

---

## 🐳 6. DOCKER COMPOSE (Local/Self-Hosted)

### docker-compose.yml

```yaml
version: '3.8'
services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - PLATFORM=docker
    command: python api.py

  db:
    image: postgres:14
    environment:
      POSTGRES_DB: mood_mapper
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: secure_password
    ports:
      - "5432:5432"
```

### Run Locally

```bash
docker-compose up
```

---

## ⚡ 7. AWS DEPLOYMENT (Scalable)

### Option A: AWS App Runner

1. Go to **AWS Console → App Runner**
2. Click **"Create Service"**
3. Select **"Source code repository"** → GitHub
4. Choose your repo and branch
5. Configure:
   - **Runtime**: Python 3
   - **Build command**: `pip install -r requirements.txt`
   - **Run command**: `python api.py`
6. Click **"Create & Deploy"**

### Option B: AWS Elastic Beanstalk

```bash
# Install EB CLI
pip install awsebcli

# Initialize
eb init -p python-3.9 campus-mood-mapper

# Deploy
eb create production
eb deploy
```

---

## 🔄 COMPARING PLATFORMS

| Platform | Cost | Setup Time | Best For | Auto-scaling |
|----------|------|-----------|----------|---------------|
| **Streamlit Cloud** | Free | 2 min | Frontend only | Limited |
| **Render** | $7+/mo | 5 min | General apps | ✅ Yes |
| **Railway** | $5+/mo | 5 min | Simplicity | ✅ Yes |
| **PythonAnywhere** | $5+/mo | 10 min | Beginners | ✅ Yes |
| **Fly.io** | $3+/mo | 10 min | Global reach | ✅ Yes |
| **AWS** | Variable | 20+ min | Enterprise | ✅ Yes |
| **Docker** | Free | 15 min | Self-hosted | Manual |

---

## 🎯 QUICK START RECOMMENDATIONS

**For Beginners**:
→ **Render.com** or **Railway.app** (easiest, free tier available)

**For Learning**:
→ **PythonAnywhere** (great for tutorials)

**For Global Users**:
→ **Fly.io** (auto-scales, distributed)

**For Teams**:
→ **AWS Elastic Beanstalk** (professional, enterprise-ready)

**For Full Control**:
→ **Docker Compose** (self-hosted on your server)

---

## ✅ TESTING YOUR DEPLOYMENT

After deploying, test endpoints:

```bash
# Replace YOUR_URL with your deployed URL
YOUR_URL="https://campus-mood-mapper.onrender.com"

# Test health
curl $YOUR_URL/health

# Test API
curl -X POST "$YOUR_URL/api/v1/mood/analyze" \
  -H "Content-Type: application/json" \
  -d '{"text": "Testing deployment", "mood_score": 5, "user_id": "test"}'
```

---

## 🆘 TROUBLESHOOTING

### Common Issues

**Port Already in Use**
```bash
kill -9 $(lsof -t -i:8000)
```

**Dependencies Not Installing**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Module Not Found**
Ensure all files (`mood_analysis.py`, `personalization.py`, `api.py`) are in the same directory.

---

## 📝 NEXT STEPS

1. Choose a platform from this guide
2. Follow the deployment steps
3. Test your API endpoints
4. Create a React/Vue frontend (see FRONTEND_SETUP.md)
5. Connect frontend to your deployed API
6. Monitor and scale as needed

---

**Happy Deploying! 🚀**

For questions, check the platform's documentation or open a GitHub issue.
