"""\nAI-Driven Mood Analysis Module\nSentiment analysis, emotion detection, and psychological insights\n"""

import re
from typing import Dict, Tuple, List
from textblob import TextBlob
from collections import defaultdict
import json

class MoodAnalyzer:
    """Analyze mood through text sentiment and emotion detection."""
    
    def __init__(self):
        # Define emotion triggers and keywords
        self.emotion_keywords = {
            'anxiety': ['anxious', 'worried', 'nervous', 'stressed', 'panic', 'overwhelmed'],
            'sadness': ['sad', 'depressed', 'unhappy', 'down', 'lonely', 'miserable'],
            'anger': ['angry', 'furious', 'frustrated', 'annoyed', 'mad', 'upset'],
            'joy': ['happy', 'excited', 'joyful', 'cheerful', 'delighted', 'ecstatic'],
            'calm': ['peaceful', 'relaxed', 'calm', 'serene', 'tranquil', 'content'],
            'exhaustion': ['tired', 'exhausted', 'drained', 'fatigued', 'burnt out'],
            'loneliness': ['lonely', 'isolated', 'alone', 'disconnected', 'outcast'],
            'motivation': ['motivated', 'focused', 'determined', 'driven', 'inspired'],
        }
        
        # Severity indicators for crisis detection
        self.crisis_keywords = [
            'suicide', 'self-harm', 'kill myself', 'hurt myself', 
            'hopeless', 'worthless', 'nothing matters', 'give up'
        ]
    
    def analyze_sentiment(self, text: str) -> Dict[str, float]:
        """Analyze sentiment polarity and subjectivity."""
        blob = TextBlob(text.lower())
        polarity = blob.sentiment.polarity  # -1 to 1 (negative to positive)
        subjectivity = blob.sentiment.subjectivity  # 0 to 1
        
        return {
            'polarity': round(polarity, 3),
            'subjectivity': round(subjectivity, 3),
            'sentiment_label': self._get_sentiment_label(polarity)
        }
    
    def _get_sentiment_label(self, polarity: float) -> str:
        """Convert polarity to sentiment label."""
        if polarity >= 0.5:
            return 'Very Positive'
        elif polarity >= 0.1:
            return 'Positive'
        elif polarity > -0.1:
            return 'Neutral'
        elif polarity >= -0.5:
            return 'Negative'
        else:
            return 'Very Negative'
    
    def detect_emotions(self, text: str) -> Dict[str, float]:
        """Detect multiple emotions in text."""
        text_lower = text.lower()
        emotion_scores = {}
        
        for emotion, keywords in self.emotion_keywords.items():
            # Count emotion keyword occurrences
            matches = sum(1 for keyword in keywords if keyword in text_lower)
            emotion_scores[emotion] = min(matches / max(1, len(keywords)), 1.0)
        
        # Normalize scores
        max_score = max(emotion_scores.values()) if emotion_scores else 1
        normalized_emotions = {
            emotion: round((score / max_score), 2) 
            for emotion, score in emotion_scores.items()
        }
        
        return normalized_emotions
    
    def detect_crisis_signals(self, text: str) -> Tuple[bool, float]:
        """Detect potential crisis indicators requiring escalation."""
        text_lower = text.lower()
        crisis_score = 0.0
        
        for keyword in self.crisis_keywords:
            if keyword in text_lower:
                crisis_score += 1.0
        
        # Normalize to 0-1 scale
        crisis_score = min(crisis_score / len(self.crisis_keywords), 1.0)
        is_crisis = crisis_score > 0.3
        
        return is_crisis, round(crisis_score, 3)
    
    def analyze_mood_entry(self, text: str, mood_score: int) -> Dict:
        """Comprehensive mood analysis combining text and numeric input."""
        sentiment = self.analyze_sentiment(text)
        emotions = self.detect_emotions(text)
        is_crisis, crisis_score = self.detect_crisis_signals(text)
        
        # Calculate overall mood index (combination of numeric and sentiment)
        sentiment_adjusted_score = ((sentiment['polarity'] + 1) * 5)  # Convert -1 to 1 → 0 to 10
        combined_mood_score = (mood_score * 0.6 + sentiment_adjusted_score * 0.4)
        
        return {
            'mood_score': mood_score,
            'sentiment': sentiment,
            'emotions': emotions,
            'combined_mood_score': round(combined_mood_score, 2),
            'primary_emotion': max(emotions, key=emotions.get) if emotions else 'neutral',
            'is_crisis': is_crisis,
            'crisis_score': crisis_score
        }


class InterventionEngine:
    """Generate evidence-based psychological interventions."""
    
    def __init__(self):
        self.interventions_db = {
            'anxiety': {
                'understand': 'Anxiety is your body\'s natural response to stress. It\'s temporary and manageable.',
                'do_now': [
                    '4-7-8 Breathing: Inhale for 4 counts, hold for 7, exhale for 8',
                    'Ground yourself: 5 things you see, 4 you feel, 3 you hear, 2 you smell, 1 you taste',
                    'Write down your worries and challenge each one logically'
                ],
                'connect': 'Consider speaking with campus counseling services for personalized support'
            },
            'sadness': {
                'understand': 'Sadness is a normal emotion. Persistent low mood may benefit from professional support.',
                'do_now': [
                    'Engage in a physical activity you enjoy',
                    'Connect with someone who cares about you',
                    'Write about what\'s troubling you, then identify one small positive action'
                ],
                'connect': 'Campus mental health services offer confidential support'
            },
            'anger': {
                'understand': 'Anger signals that something matters to you. Channel it constructively.',
                'do_now': [
                    'Physical activity: go for a walk, run, or workout',
                    'Creative outlet: journaling, art, music',
                    'Take 3 deep breaths and identify what you can control'
                ],
                'connect': 'Reach out to friends or mentors for perspective'
            },
            'exhaustion': {
                'understand': 'Burnout requires rest and boundaries. You deserve self-care.',
                'do_now': [
                    'Schedule 15-min break right now',
                    'Practice a relaxation exercise: progressive muscle relaxation or guided meditation',
                    'Identify one task you can delegate or postpone'
                ],
                'connect': 'Discuss workload with advisors or campus wellness programs'
            },
            'loneliness': {
                'understand': 'Connection is essential. Loneliness is treatable through gradual social engagement.',
                'do_now': [
                    'Text or call one person you trust',
                    'Attend a campus event or join a club',
                    'Volunteer or help someone—giving creates connection'
                ],
                'connect': 'Join peer support groups or campus social activities'
            }
        }
    
    def get_intervention(self, primary_emotion: str, mood_score: int) -> Dict:
        """Generate personalized intervention based on emotion and mood score."""
        
        # Default intervention if emotion not in DB
        if primary_emotion not in self.interventions_db:
            primary_emotion = 'sadness'  # Fallback
        
        intervention = self.interventions_db[primary_emotion]
        
        return {
            'emotion': primary_emotion,
            'understand': intervention['understand'],
            'do_now': intervention['do_now'],
            'connect': intervention['connect'],
            'urgency': 'high' if mood_score < 3 else 'medium' if mood_score < 6 else 'low'
        }
    
    def get_coping_strategies(self, emotions: Dict[str, float], mood_score: int) -> List[str]:
        """Generate adaptive coping strategies."""
        strategies = []
        
        if mood_score < 4:
            strategies.extend([
                '✓ Gentle movement: stretching or slow walking',
                '✓ Reach out to a trusted friend or family member',
                '✓ Practice self-compassion: talk to yourself like a good friend would'
            ])
        
        if emotions.get('anxiety', 0) > 0.5:
            strategies.append('✓ Try the 5-4-3-2-1 grounding technique')
        
        if emotions.get('exhaustion', 0) > 0.5:
            strategies.append('✓ Take a proper break and set boundaries')
        
        if emotions.get('loneliness', 0) > 0.5:
            strategies.append('✓ Reach out and connect with your community')
        
        return strategies if strategies else ['✓ Continue self-care and monitor your mood']
