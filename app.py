#!/usr/bin/env python3
"""
Campus Mood Mapper
Created by: Shashwat Pathak
Data Science Project for Sentiment Analysis and Mood Tracking
"""

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import pandas as pd
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campus_mood.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    moods = db.relationship('Mood', backref='user', lazy=True)

class Mood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mood_score = db.Column(db.Integer, nullable=False)
    sentiment = db.Column(db.String(50))
    comment = db.Column(db.Text)
    location = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Routes
@app.route('/')
def index():
    return render_template('index.html', creator='Shashwat Pathak')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return 'Error creating user'
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid credentials'
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_moods = Mood.query.filter_by(user_id=session['user_id']).all()
    return render_template('dashboard.html', moods=user_moods, username=session['username'])

@app.route('/add_mood', methods=['POST'])
def add_mood():
    if 'user_id' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    
    data = request.get_json()
    new_mood = Mood(
        user_id=session['user_id'],
        mood_score=data['mood_score'],
        sentiment=data.get('sentiment', ''),
        comment=data.get('comment', ''),
        location=data.get('location', '')
    )
    
    db.session.add(new_mood)
    db.session.commit()
    
    return jsonify({'success': True, 'id': new_mood.id})

@app.route('/export_data')
def export_data():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_moods = Mood.query.filter_by(user_id=session['user_id']).all()
    data = [{
        'timestamp': mood.timestamp,
        'mood_score': mood.mood_score,
        'sentiment': mood.sentiment,
        'comment': mood.comment,
        'location': mood.location
    } for mood in user_moods]
    
    df = pd.DataFrame(data)
    return df.to_json(orient='records')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
