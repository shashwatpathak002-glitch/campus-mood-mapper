# Campus Mood Mapper - Implementation Guide

## 📖 Overview

This guide explains how to integrate and use the advanced AI-driven mood analysis features in Campus Mood Mapper. It covers the mood analysis engine, psychological interventions, and personalization system.

---

## 🔧 Module Reference

### 1. Mood Analysis Module (`mood_analysis.py`)

Handles real-time sentiment analysis, emotion detection, and crisis signal detection.

#### MoodAnalyzer Class

**Initialization:**
```python
from mood_analysis import MoodAnalyzer

analyzer = MoodAnalyzer()
```

**Sentiment Analysis:**
```python
# Analyze text sentiment
result = analyzer.analyze_sentiment("I'm feeling really stressed about exams")
print(result)
# Output: {'polarity': -0.6, 'subjectivity': 0.8, 'sentiment_label': 'Negative'}
```

**Emotion Detection:**
```python
# Detect emotions
emotions = analyzer.detect_emotions("I'm anxious and exhausted")
print(emotions)
# Output: {'anxiety': 0.8, 'exhaustion': 0.75, 'sadness': 0.2, ...}
```

**Crisis Detection:**
```python
is_crisis, score = analyzer.detect_crisis_signals("I can't go on")
if is_crisis:
    # Trigger emergency escalation
    send_crisis_alert()
```

**Comprehensive Analysis:**
```python
analysis = analyzer.analyze_mood_entry(
    text="Feeling overwhelmed and hopeless",
    mood_score=2  # 1-10 scale
)

print(analysis)
# Output: {
#   'mood_score': 2,
#   'sentiment': {...},
#   'emotions': {...},
#   'combined_mood_score': 3.5,
#   'primary_emotion': 'sadness',
#   'is_crisis': False,
#   'crisis_score': 0.15
# }
```

---

#### InterventionEngine Class

Generates evidence-based psychological support based on detected emotions.

**Get Personalized Intervention:**
```python
from mood_analysis import InterventionEngine

engine = InterventionEngine()

intervention = engine.get_intervention(
    primary_emotion='anxiety',
    mood_score=4
)

print(intervention)
# Output: {
#   'emotion': 'anxiety',
#   'understand': 'Anxiety is your body...',
#   'do_now': ['4-7-8 Breathing...', 'Ground yourself...'],
#   'connect': 'Campus counseling...',
#   'urgency': 'medium'
# }
```

**Get Coping Strategies:**
```python
strategies = engine.get_coping_strategies(
    emotions={'anxiety': 0.8, 'exhaustion': 0.6},
    mood_score=3
)

for strategy in strategies:
    print(strategy)
# Output:
# ✓ Gentle movement: stretching or slow walking
# ✓ Try the 5-4-3-2-1 grounding technique
# ✓ Take a proper break and set boundaries
```

---

### 2. Personalization Module (`personalization.py`)

Tracks user preferences and adapts recommendations over time.

#### PersonalizationEngine Class

**Create User Profile:**
```python
from personalization import PersonalizationEngine

engine = PersonalizationEngine()
profile = engine.create_user_profile(user_id="student_123")
```

**Record Intervention Feedback:**
```python
# Track if an intervention was helpful
engine.update_intervention_feedback(
    user_id="student_123",
    intervention_type="breathing_exercise",
    was_helpful=True,
    completion_time=5  # minutes
)
```

**Get Preferred Interventions:**
```python
# Get top 3 interventions for this user
preferred = engine.get_preferred_interventions(
    user_id="student_123",
    top_n=3
)
# Output: ['breathing_exercise', 'journaling', 'physical_activity']
```

**Analyze Mood Patterns:**
```python
mood_entries = [
    {'timestamp': '2025-01-01 09:00:00', 'mood_score': 5},
    {'timestamp': '2025-01-01 14:00:00', 'mood_score': 3},
    # ... more entries
]

patterns = engine.analyze_mood_patterns("student_123", mood_entries)
print(patterns)
# Output: {
#   'avg_mood_by_day': {'Monday': 4.2, 'Tuesday': 5.1, ...},
#   'lowest_mood_days': ['Monday', 'Wednesday'],
#   'highest_mood_days': ['Friday', 'Saturday'],
#   'mood_trend': 'improving'
# }
```

**Get Personalized Recommendations:**
```python
recs = engine.get_personalized_recommendations(
    user_id="student_123",
    current_mood=4,
    emotions={'anxiety': 0.5, 'sadness': 0.3}
)
print(recs)
# Output: {
#   'primary_suggestion': 'breathing_exercise',
#   'alternatives': ['journaling', 'physical_activity'],
#   'timing': 'morning',
#   'personalized_message': 'You're managing well...'
# }
```

---

#### MoodTrendAnalyzer Class

**Calculate Statistics:**
```python
from personalization import MoodTrendAnalyzer

analyzer = MoodTrendAnalyzer()
stats = analyzer.calculate_mood_statistics(mood_entries)
print(stats)
# Output: {
#   'avg_mood_all_time': 5.2,
#   'avg_mood_last_7_days': 5.8,
#   'best_mood': 10,
#   'worst_mood': 1,
#   'mood_variance': 4.5,
#   'total_entries': 45,
#   'streak_days': 12
# }
```

**Get Insights:**
```python
insights = analyzer.get_insights(mood_entries)
for insight in insights:
    print(insight)
# Output:
# 📈 Your mood has been trending upward recently!
# 😊 You've been feeling good this week!
```

---

## 🎯 Integration Examples

### Example 1: Streamlit Integration

```python
import streamlit as st
from mood_analysis import MoodAnalyzer, InterventionEngine
from personalization import PersonalizationEngine

# Initialize
analyzer = MoodAnalyzer()
engine = InterventionEngine()
pers_engine = PersonalizationEngine()

# User input
st.subheader("How are you feeling?")
mood_score = st.slider("Mood (1-10)", 1, 10, 5)
text_input = st.text_area("Tell us what's on your mind...")

# Analyze
if st.button("Analyze & Get Support"):
    analysis = analyzer.analyze_mood_entry(text_input, mood_score)
    
    # Check for crisis
    if analysis['is_crisis']:
        st.error("⚠️ We're concerned about you. Please reach out immediately.")
        st.info("""
        Crisis Resources:
        - 988 Suicide & Crisis Lifeline
        - Campus Counseling: [contact]
        - Crisis Text Line: Text HOME to 741741
        """)
    
    # Get intervention
    intervention = engine.get_intervention(
        analysis['primary_emotion'],
        mood_score
    )
    
    st.info(f"### 💡 {intervention['emotion'].title()}")
    st.write(intervention['understand'])
    st.success("### ✅ Try This Now")
    for strategy in intervention['do_now']:
        st.write(f"• {strategy}")
    
    # Personalized recommendation
    recs = pers_engine.get_personalized_recommendations(
        st.session_state.user_id,
        mood_score,
        analysis['emotions']
    )
    st.info(f"🎯 {recs['personalized_message']}")
```

### Example 2: Fastapi Endpoint

```python
from fastapi import FastAPI
from mood_analysis import MoodAnalyzer

app = FastAPI()
analyzer = MoodAnalyzer()

@app.post("/api/analyze-mood")
async def analyze_mood(text: str, mood_score: int):
    result = analyzer.analyze_mood_entry(text, mood_score)
    return result

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}
```

---

## 🛡️ Error Handling

```python
try:
    analysis = analyzer.analyze_mood_entry(user_text, mood_score)
except ValueError as e:
    print(f"Invalid input: {e}")
except Exception as e:
    # Log to monitoring system
    logger.error(f"Analysis failed: {e}")
    # Return safe default
    return default_intervention()
```

---

## 📊 Testing

```python
import unittest
from mood_analysis import MoodAnalyzer

class TestMoodAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = MoodAnalyzer()
    
    def test_positive_sentiment(self):
        result = self.analyzer.analyze_sentiment("I'm so happy!")
        self.assertGreater(result['polarity'], 0.5)
    
    def test_crisis_detection(self):
        is_crisis, score = self.analyzer.detect_crisis_signals("suicide")
        self.assertTrue(is_crisis)

if __name__ == '__main__':
    unittest.main()
```

---

## 🚀 Best Practices

1. **Always check for crisis signals** before showing generic interventions
2. **Cache recommendations** for 6 hours to reduce computation
3. **Log all mood entries** with user consent for trend analysis
4. **Validate user input** before passing to analyzers
5. **Provide multiple coping options** - users have different preferences
6. **Update user profiles regularly** as they interact with the app
7. **Never make medical claims** - always recommend professional help

---

## 📞 Support

For questions or issues:
1. Check GitHub Issues
2. Review inline documentation
3. Reach out via email

---

**Last Updated**: December 2025
