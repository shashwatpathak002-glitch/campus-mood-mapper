"""\nPersonalization and User Preference Engine\nAdapts interventions and suggestions based on user history and preferences\n"""

from typing import Dict, List
from datetime import datetime, timedelta
import json

class PersonalizationEngine:
    """Track user preferences and adapt interventions accordingly."""
    
    def __init__(self):
        self.user_preferences = {}
        self.feedback_history = {}
        self.coping_style_weights = {}
    
    def create_user_profile(self, user_id: str) -> Dict:
        """Initialize a user profile for personalization."""
        return {
            'user_id': user_id,
            'preferred_coping_styles': {},  # e.g., physical_activity, journaling, meditation
            'skipped_interventions': [],  # Track what user ignores
            'effective_interventions': [],  # Track what resonates
            'mood_triggers': [],  # Recurring patterns
            'response_times': {},  # Time of day user engages best
            'created_at': datetime.now().isoformat()
        }
    
    def update_intervention_feedback(self, user_id: str, intervention_type: str, 
                                   was_helpful: bool, completion_time: int = None) -> None:
        """Record user feedback on interventions."""
        if user_id not in self.feedback_history:
            self.feedback_history[user_id] = []
        
        feedback = {
            'intervention': intervention_type,
            'helpful': was_helpful,
            'completion_time': completion_time,
            'timestamp': datetime.now().isoformat()
        }
        self.feedback_history[user_id].append(feedback)
    
    def get_preferred_interventions(self, user_id: str, top_n: int = 3) -> List[str]:
        """Recommend interventions based on user's history."""
        if user_id not in self.feedback_history:
            return ['breathing_exercise', 'journaling', 'physical_activity']  # Default
        
        # Count helpful interventions
        helpful_count = {}
        for feedback in self.feedback_history[user_id]:
            if feedback['helpful']:
                intervention = feedback['intervention']
                helpful_count[intervention] = helpful_count.get(intervention, 0) + 1
        
        # Return top helpful interventions
        sorted_interventions = sorted(helpful_count.items(), key=lambda x: x[1], reverse=True)
        return [intervention for intervention, _ in sorted_interventions[:top_n]]
    
    def analyze_mood_patterns(self, user_id: str, mood_entries: List[Dict]) -> Dict:
        """Identify recurring mood patterns and triggers."""
        if not mood_entries:
            return {}
        
        patterns = {
            'avg_mood_by_day': {},
            'avg_mood_by_hour': {},
            'lowest_mood_days': [],
            'highest_mood_days': [],
            'mood_trend': 'stable'
        }
        
        # Analyze by day of week
        day_moods = {}
        hour_moods = {}
        
        for entry in mood_entries:
            timestamp = datetime.fromisoformat(entry['timestamp'])
            day_name = timestamp.strftime('%A')
            hour = timestamp.hour
            mood = entry['mood_score']
            
            # Track by day
            if day_name not in day_moods:
                day_moods[day_name] = []
            day_moods[day_name].append(mood)
            
            # Track by hour
            if hour not in hour_moods:
                hour_moods[hour] = []
            hour_moods[hour].append(mood)
        
        # Calculate averages
        patterns['avg_mood_by_day'] = {
            day: round(sum(moods) / len(moods), 2) 
            for day, moods in day_moods.items()
        }
        patterns['avg_mood_by_hour'] = {
            str(hour): round(sum(moods) / len(moods), 2) 
            for hour, moods in hour_moods.items()
        }
        
        # Identify best/worst days
        if patterns['avg_mood_by_day']:
            sorted_days = sorted(patterns['avg_mood_by_day'].items(), key=lambda x: x[1])
            patterns['lowest_mood_days'] = [day for day, _ in sorted_days[:2]]
            patterns['highest_mood_days'] = [day for day, _ in sorted_days[-2:]]
        
        # Determine trend (simplified)
        recent_moods = [e['mood_score'] for e in mood_entries[-7:]]
        if len(recent_moods) > 1:
            trend = (recent_moods[-1] - recent_moods[0]) / len(recent_moods)
            if trend > 0.5:
                patterns['mood_trend'] = 'improving'
            elif trend < -0.5:
                patterns['mood_trend'] = 'declining'
        
        return patterns
    
    def get_personalized_recommendations(self, user_id: str, current_mood: int, 
                                         emotions: Dict[str, float]) -> Dict:
        """Generate personalized recommendations based on user history."""
        preferred_interventions = self.get_preferred_interventions(user_id)
        
        recommendations = {
            'primary_suggestion': preferred_interventions[0] if preferred_interventions else 'meditation',
            'alternatives': preferred_interventions[1:] if len(preferred_interventions) > 1 else [],
            'timing': self._get_optimal_timing(user_id),
            'personalized_message': self._generate_personal_message(user_id, current_mood)
        }
        
        return recommendations
    
    def _get_optimal_timing(self, user_id: str) -> str:
        """Determine best time of day to check in."""
        # Could be enhanced with user's historical response patterns
        return "morning"  # Default recommendation
    
    def _generate_personal_message(self, user_id: str, mood_score: int) -> str:
        """Create a personalized message for the user."""
        if mood_score >= 7:
            return "Great to see you doing well! Keep up the positive momentum."
        elif mood_score >= 5:
            return "You're managing well. These small steps matter."
        elif mood_score >= 3:
            return "Tough day? Remember: you've gotten through difficult times before."
        else:
            return "Reach out to someone. You don't have to go through this alone."


class MoodTrendAnalyzer:
    """Analyze trends and provide insights to the user."""
    
    def __init__(self):
        self.trends_db = {}
    
    def calculate_mood_statistics(self, mood_entries: List[Dict]) -> Dict:
        """Calculate statistics from mood entries."""
        if not mood_entries:
            return {}
        
        moods = [e['mood_score'] for e in mood_entries]
        recent_moods = moods[-7:] if len(moods) > 7 else moods
        
        return {
            'avg_mood_all_time': round(sum(moods) / len(moods), 2),
            'avg_mood_last_7_days': round(sum(recent_moods) / len(recent_moods), 2),
            'best_mood': max(moods),
            'worst_mood': min(moods),
            'mood_variance': round(
                sum((m - (sum(moods)/len(moods)))**2 for m in moods) / len(moods), 2
            ),
            'total_entries': len(moods),
            'streak_days': self._calculate_streak(mood_entries)
        }
    
    def _calculate_streak(self, mood_entries: List[Dict]) -> int:
        """Calculate consecutive days with mood entries."""
        if not mood_entries:
            return 0
        
        # Sort by timestamp
        sorted_entries = sorted(mood_entries, key=lambda x: x['timestamp'])
        streak = 1
        
        for i in range(1, len(sorted_entries)):
            curr_date = datetime.fromisoformat(sorted_entries[i]['timestamp']).date()
            prev_date = datetime.fromisoformat(sorted_entries[i-1]['timestamp']).date()
            
            if (curr_date - prev_date).days == 1:
                streak += 1
            elif (curr_date - prev_date).days > 1:
                streak = 1
        
        return streak
    
    def get_insights(self, mood_entries: List[Dict]) -> List[str]:
        """Generate text-based insights from mood data."""
        if not mood_entries:
            return []
        
        insights = []
        stats = self.calculate_mood_statistics(mood_entries)
        
        if stats.get('mood_trend') == 'improving':
            insights.append("📈 Your mood has been trending upward recently!")
        elif stats.get('mood_trend') == 'declining':
            insights.append("📉 Your mood has declined recently. Consider reaching out for support.")
        
        if stats['avg_mood_last_7_days'] > 6:
            insights.append("😊 You've been feeling good this week!")
        elif stats['avg_mood_last_7_days'] < 4:
            insights.append("💙 This has been a tough week. Be patient with yourself.")
        
        return insights
