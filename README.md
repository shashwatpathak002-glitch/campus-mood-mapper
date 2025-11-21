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

**⭐ If you find this project useful, please consider giving it a star!**
