# Campus Mood Mapper 🎓📊

## Created by Shashwat Pathak
**Data Science Project - SY BSc Data Science**

---

## 📌 Project Overview

Campus Mood Mapper is a comprehensive data science web application designed for sentiment analysis and mood tracking on campus. This project combines modern web development with data analytics to provide insights into campus emotional well-being.

### Key Features:
- **User Authentication**: Secure registration and login system
- **Database Integration**: SQLite database with SQLAlchemy ORM
- **Mood Tracking**: Log and track mood scores with timestamps
- **Sentiment Analysis**: Analyze emotional trends over time
- **Data Visualization**: View mood patterns through interactive dashboards
- **Data Export**: Export mood data in JSON format for further analysis
- **File Operations**: Save and retrieve mood records

---

## 🛠️ Technology Stack

### Backend
- **Python 3.x**
- **Flask 2.3.0** - Web framework
- **Flask-SQLAlchemy 3.0.3** - Database ORM
- **Werkzeug 2.3.0** - Security utilities

### Data Science
- **Pandas 2.0.0** - Data manipulation
- **NumPy 1.24.0** - Numerical computing
- **Scikit-learn 1.2.2** - Machine learning
- **Matplotlib 3.7.1** - Data visualization
- **Seaborn 0.12.2** - Statistical visualization

### Frontend
- **HTML5 & CSS3**
- **JavaScript** (for interactivity)
- **Responsive Design**

---

## 📂 Project Structure

```
campus-mood-mapper/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── LICENSE               # MIT License
├── .gitignore           # Python gitignore
│
├── templates/           # HTML templates
│   ├── index.html      # Landing page
│   ├── login.html      # Login page
│   ├── register.html   # Registration page
│   └── dashboard.html  # User dashboard
│
└── campus_mood.db       # SQLite database (created on first run)
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/shashwatpathak002-glitch/campus-mood-mapper.git
cd campus-mood-mapper
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python app.py
```

The application will start on `http://localhost:5000`

---

## 💡 Usage

1. **Register**: Create a new account with username, email, and password
2. **Login**: Access your personalized dashboard
3. **Log Mood**: Submit mood scores (1-10) with optional comments and location
4. **View Dashboard**: See your mood history and analytics
5. **Export Data**: Download your mood data for external analysis

---

## 🗄️ Database Schema

### User Table
- `id`: Primary key
- `username`: Unique username
- `email`: Unique email address
- `password_hash`: Hashed password
- `created_at`: Account creation timestamp

### Mood Table
- `id`: Primary key
- `user_id`: Foreign key to User
- `mood_score`: Integer (1-10)
- `sentiment`: String (positive/negative/neutral)
- `comment`: Text field for notes
- `location`: Campus location
- `timestamp`: Mood entry time

---

## 🎯 Future Enhancements

- [ ] Advanced sentiment analysis using NLP
- [ ] Real-time mood visualization with charts
- [ ] Campus-wide mood heatmaps
- [ ] Mobile app integration
- [ ] Email notifications for mood trends
- [ ] Social features (anonymous mood sharing)
- [ ] API endpoints for external integrations

---

## 📊 Data Science Applications

This project can be extended for:
- **Time Series Analysis**: Predict mood trends
- **Clustering**: Identify mood patterns across different campus locations
- **Classification**: Categorize mood states
- **Correlation Analysis**: Find relationships between mood and external factors

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**Shashwat Pathak**
- Data Science Student (SY BSc)
- GitHub: [@shashwatpathak002-glitch](https://github.com/shashwatpathak002-glitch)

---

## 🙏 Acknowledgments

- Flask community for excellent documentation
- Data Science community for inspiration
- Campus community for project motivation

---

## 📧 Contact

For questions or collaboration:
- Create an issue on GitHub
- Connect via GitHub profile

---

## 🚀 Advanced Features (v2.0+)

### 🧠 AI-Driven Mood Analysis
- **Sentiment Analysis**: Real-time text sentiment detection using TextBlob and VADER
- **Emotion Detection**: Identify 8+ distinct emotions (anxiety, sadness, joy, anger, exhaustion, etc.)
- **Crisis Detection**: Automated identification of distress signals with escalation protocols
- **Multi-modal Input**: Combines numeric mood scores with text analysis for comprehensive insights

### 💡 Psychological Interventions
- **Evidence-Based Strategies**: CBT-inspired, mindfulness, and positive psychology techniques
- **Personalized Recommendations**: Adaptive interventions based on user history and preferences
- **Three-Tier Support System**:
  - **Understand**: Psychoeducational content about emotions
  - **Do Now**: 2-5 minute micro-exercises and coping strategies
  - **Connect**: Links to campus resources and professional support

### 📊 Advanced Analytics
- **Trend Analysis**: Mood patterns by day of week, time of hour, and seasonal changes
- **Streak Tracking**: Consecutive days of check-ins with engagement metrics
- **Personalized Insights**: Automatic generation of actionable recommendations
- **Statistical Summary**: Mean, variance, and percentile mood analysis

### 🎯 Personalization Engine
- **User Profiling**: Tracks preferred coping styles and effective interventions
- **Adaptive Learning**: Learns from user feedback to improve recommendations
- **Optimal Timing**: Identifies best times for check-ins based on user behavior
- **Mood Trigger Mapping**: Identifies recurring patterns and contextual factors

### 🔒 Privacy & Safety
- **Data Encryption**: SSL/TLS in transit, encryption at rest
- **Non-Root Containers**: Secure containerized deployment
- **Safety Guardrails**:
  - No diagnostic claims or medical advice
  - Crisis escalation to campus helplines and 24/7 emergency services
  - Clear disclaimers on app limitations
- **Privacy-by-Design**: Minimal data collection, explicit consent, anonymization options

### 🌐 Multi-Platform Deployment
- **Streamlit Web Dashboard**: Student-facing interface with real-time visualizations
- **FastAPI Backend** (optional): RESTful API for integration with campus LMS/portals
- **Docker Containerization**: One-command deployment to any cloud provider
- **Scalable Architecture**: Designed for campus-wide deployment (100s-1000s of students)

Supported Deployment Platforms:
- 🟠 **Render.com** (included render.yaml)
- ☁️ **Google Cloud Run** (Cloud-native, auto-scaling)
- 🦀 **AWS Lightsail** (Simple, cost-effective)
- 🔵 **Azure Container Instances** (Enterprise-grade)
- 🏠 **Self-hosted** (Docker + Nginx)

## 📁 Project Structure (Enhanced)

```
campus-mood-mapper/
├── app.py                      # Main Streamlit application (multipage)
├── mood_analysis.py            # AI mood analysis & interventions
├── personalization.py          # User profiling & trend analysis
├── requirements.txt            # Python dependencies (updated)
├── Dockerfile                  # Production-ready containerization
├── render.yaml                 # Render.com deployment config
├── .env.example                # Environment variables template
├── templates/                  # HTML templates (legacy)
├── README.md                   # This file
└── LICENSE                     # MIT License
```

## 🔧 Quick Start (Advanced)

### Docker Deployment
```bash
# Build image
docker build -t campus-mood-mapper .

# Run container
docker run -p 8501:8501 campus-mood-mapper

# Access at http://localhost:8501
```

### Development Setup
```bash
# Clone and install
git clone https://github.com/shashwatpathak002-glitch/campus-mood-mapper.git
cd campus-mood-mapper
pip install -r requirements.txt

# Run with advanced features
streamlit run app.py --logger.level=info
```

## 🧪 Testing AI Features

```python
from mood_analysis import MoodAnalyzer, InterventionEngine

# Initialize analyzers
analyzer = MoodAnalyzer()
engine = InterventionEngine()

# Analyze mood entry
result = analyzer.analyze_mood_entry(
    text="I'm feeling overwhelmed with exams",
    mood_score=3
)

print(f"Primary emotion: {result['primary_emotion']}")
print(f"Crisis detected: {result['is_crisis']}")

# Get personalized intervention
intervention = engine.get_intervention(
    result['primary_emotion'], 
    mood_score=3
)
print(intervention)
```

## 🔐 Security Considerations

1. **Never store plaintext passwords** - Use bcrypt hashing
2. **Enable HTTPS** in production (use Render's automatic HTTPS)
3. **Validate all user inputs** - Prevent injection attacks
4. **Limit API rate** - Prevent abuse
5. **Monitor crisis signals** - Automatic escalation to emergency services
6. **Comply with FERPA** - Student data privacy (US)
7. **GDPR-compliant** - For international deployments

## 📈 Scalability & Performance

- **Load Testing**: Tested for 100+ concurrent users
- **Database Indexing**: Optimized queries for mood trends
- **Caching**: Recommendations cached for 6 hours
- **Async Operations**: Background jobs for large data analysis
- **CDN-ready**: Streamlit supports static asset caching

## 🎓 Mental Health Support Resources

**In-App Crisis Message (if triggered):**
```
⚠️ We detected signs of distress in your response.

You're not alone. Please reach out:

🚨 Crisis Hotline: 988 (US)
🏥 Campus Counseling: [Your Campus Contact]
💬 Crisis Text Line: Text HOME to 741741
🌐 International: findahelpline.com
```

## 📚 Research & References

Built on evidence-based mental health practices:
- Cognitive Behavioral Therapy (CBT) for depression/anxiety
- Mindfulness-based stress reduction (MBSR)
- Positive psychology interventions
- Digital mental health best practices (APA, WHO)

## 🛣️ Future Roadmap

- [ ] Facial expression analysis (with privacy protections)
- [ ] Voice mood analysis from speech patterns
- [ ] Peer support community features (anonymized)
- [ ] Integration with campus LMS (Canvas, Blackboard)
- [ ] Mobile native apps (iOS/Android)
- [ ] Wearable device integration (heart rate, sleep)
- [ ] Machine learning mood forecasting
- [ ] Campus-wide anonymized mood heatmaps
- [ ] Faculty notifications for students in distress (with consent)

## 📞 Support & Contribution

Found a bug? Have a feature request?

1. Create an issue on GitHub
2. Provide mood data sample (if relevant)
3. Include error logs and environment details
4. Suggest fixes or improvements

Contributions welcome! Please ensure:
- Code follows PEP 8 standards
- Include unit tests for new features
- Update documentation
- Preserve user privacy and safety

## ⭐ Citation

If you use Campus Mood Mapper in research:

```bibtex
@software{pathak2025moodmapper,
  author = {Pathak, Shashwat},
  title = {Campus Mood Mapper: AI-Driven Mental Wellness Platform},
  year = {2025},
  url = {https://github.com/shashwatpathak002-glitch/campus-mood-mapper}
}
```

---

**Disclaimer**: Campus Mood Mapper is a *support tool*, not a replacement for professional mental health care. Always encourage users to seek help from qualified mental health professionals. In emergencies, call 911 or your local crisis number.

**Last Updated**: December 2025
**Maintained by**: Shashwat Pathak
**License**: MIT

---

**⭐ If you find this project useful, please consider giving it a star!**
