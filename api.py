"""\nCampus Mood Mapper - FastAPI Backend\nMulti-platform deployment ready\nSupports Render, Railway, PythonAnywhere, Fly.io, AWS, Heroku alternatives
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from mood_analysis import MoodAnalyzer, InterventionEngine
from personalization import PersonalizationEngine, MoodTrendAnalyzer
from datetime import datetime
import os

# Initialize FastAPI app
app = FastAPI(
    title="Campus Mood Mapper API",
    description="AI-driven mental wellness platform for students",
    version="2.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize AI engines
analyzer = MoodAnalyzer()
engine = InterventionEngine()
personalization = PersonalizationEngine()
trend_analyzer = MoodTrendAnalyzer()

# Database (in production, use PostgreSQL/MongoDB)
user_moods = {}  # {user_id: [mood_entries]}

# ============================================
# DATA MODELS
# ============================================

class MoodEntry(BaseModel):
    """Mood log entry from student"""
    text: str
    mood_score: int  # 1-10
    user_id: str
    location: str = "Campus"

class MoodAnalysisResponse(BaseModel):
    """Response from mood analysis"""
    mood_score: int
    sentiment: dict
    emotions: dict
    primary_emotion: str
    is_crisis: bool
    intervention: dict
    timestamp: str

# ============================================
# ENDPOINTS
# ============================================

@app.get("/")
async def root():
    """API root endpoint"""
    return {
        "app": "Campus Mood Mapper",
        "version": "2.0.0",
        "status": "operational",
        "endpoints": {
            "health": "/health",
            "analyze_mood": "/api/v1/mood/analyze",
            "log_mood": "/api/v1/mood/log",
            "get_user_moods": "/api/v1/moods/{user_id}",
            "get_trends": "/api/v1/trends/{user_id}",
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "platform": os.getenv("PLATFORM", "unknown")
    }

@app.post("/api/v1/mood/analyze")
async def analyze_mood(mood_entry: MoodEntry):
    """Analyze mood and return AI-driven interventions"""
    try:
        # Run mood analysis
        analysis = analyzer.analyze_mood_entry(
            mood_entry.text,
            mood_entry.mood_score
        )
        
        # Get personalized intervention
        intervention = engine.get_intervention(
            analysis['primary_emotion'],
            mood_entry.mood_score
        )
        
        # Check for crisis
        if analysis['is_crisis']:
            return {
                "status": "crisis_detected",
                "message": "⚠️ We're concerned about you. Please reach out immediately.",
                "emergency_resources": {
                    "crisis_hotline": "988 (US)",
                    "crisis_text": "Text HOME to 741741",
                    "campus_counseling": "[Your Campus Contact]"
                },
                "analysis": analysis,
                "intervention": intervention
            }
        
        return {
            "status": "success",
            "analysis": analysis,
            "intervention": intervention,
            "timestamp": analysis['timestamp']
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/mood/log")
async def log_mood(mood_entry: MoodEntry):
    """Log a mood entry for a user"""
    try:
        # Analyze the mood
        analysis = analyzer.analyze_mood_entry(
            mood_entry.text,
            mood_entry.mood_score
        )
        
        # Store in database
        if mood_entry.user_id not in user_moods:
            user_moods[mood_entry.user_id] = []
        
        mood_record = {
            "timestamp": datetime.now().isoformat(),
            "mood_score": mood_entry.mood_score,
            "text": mood_entry.text,
            "location": mood_entry.location,
            "analysis": analysis
        }
        
        user_moods[mood_entry.user_id].append(mood_record)
        
        # Update intervention feedback (if helpful)
        primary_emotion = analysis['primary_emotion']
        personalization.update_intervention_feedback(
            mood_entry.user_id,
            primary_emotion,
            was_helpful=True
        )
        
        return {
            "status": "logged",
            "user_id": mood_entry.user_id,
            "entry_count": len(user_moods[mood_entry.user_id]),
            "analysis": analysis
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/moods/{user_id}")
async def get_user_moods(user_id: str):
    """Get all mood entries for a user"""
    if user_id not in user_moods:
        return {
            "user_id": user_id,
            "moods": [],
            "message": "No mood entries found. Start tracking your mood!"
        }
    
    return {
        "user_id": user_id,
        "moods": user_moods[user_id],
        "total_entries": len(user_moods[user_id])
    }

@app.get("/api/v1/trends/{user_id}")
async def get_mood_trends(user_id: str):
    """Get mood trends and insights for a user"""
    if user_id not in user_moods or len(user_moods[user_id]) == 0:
        return {
            "user_id": user_id,
            "message": "No data available for trends"
        }
    
    # Extract mood entries
    entries = [
        {
            "timestamp": m["timestamp"],
            "mood_score": m["mood_score"]
        }
        for m in user_moods[user_id]
    ]
    
    # Calculate statistics
    stats = trend_analyzer.calculate_mood_statistics(entries)
    patterns = personalization.analyze_mood_patterns(user_id, entries)
    insights = trend_analyzer.get_insights(entries)
    
    return {
        "user_id": user_id,
        "statistics": stats,
        "patterns": patterns,
        "insights": insights
    }

@app.get("/api/v1/recommendations/{user_id}")
async def get_recommendations(user_id: str):
    """Get personalized recommendations"""
    if user_id not in user_moods or len(user_moods[user_id]) == 0:
        return {
            "recommendations": "Start logging your mood to get personalized recommendations"
        }
    
    latest_entry = user_moods[user_id][-1]
    current_mood = latest_entry["mood_score"]
    emotions = latest_entry["analysis"]["emotions"]
    
    recommendations = personalization.get_personalized_recommendations(
        user_id,
        current_mood,
        emotions
    )
    
    return recommendations

# ============================================
# ERROR HANDLERS
# ============================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Handle HTTP exceptions"""
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )

# ============================================
# FOR LOCAL TESTING
# ============================================

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
