#!/usr/bin/env python3
"""
Campus Mood Mapper - Streamlit Version
Created by: Shashwat Pathak
Data Science Project for Sentiment Analysis and Mood Tracking
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json

# Page configuration
st.set_page_config(
    page_title="Campus Mood Mapper | Shashwat Pathak",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for storing mood data
if 'moods' not in st.session_state:
    st.session_state.moods = []

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'username' not in st.session_state:
    st.session_state.username = ""

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .mood-card {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin: 1rem 0;
    }
    .stat-card {
        padding: 1rem;
        border-radius: 8px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">🎓 Campus Mood Mapper 📊</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Created by Shashwat Pathak</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/150?text=Campus+Mood", use_column_width=True)
    st.title("Navigation")
    
    if not st.session_state.logged_in:
        page = st.radio("Go to", ["Home", "Login", "Register"])
    else:
        st.success(f"Welcome, {st.session_state.username}!")
        page = st.radio("Go to", ["Dashboard", "Add Mood", "Analytics", "Export Data"])
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.rerun()

# Home Page
if page == "Home":
    st.write("")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stat-card">
            <h3>😊 Track Moods</h3>
            <p>Monitor your daily emotional state</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <h3>📈 Analyze Trends</h3>
            <p>Discover patterns in your mood</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <h3>🎯 Set Goals</h3>
            <p>Improve your well-being</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    st.subheader("About Campus Mood Mapper")
    st.info("""
    Campus Mood Mapper is a data science project designed to track and analyze mood patterns
    on campus. Built with Streamlit, it provides an interactive dashboard for sentiment analysis
    and mood tracking.
    
    **Features:**
    - 🔐 User authentication
    - 📊 Interactive mood tracking
    - 📈 Data visualization
    - 💾 Data export capabilities
    - 🎨 Beautiful UI/UX
    
    **Created by:** Shashwat Pathak
    **Project Type:** SY BSc Data Science Project
    """)

# Register Page
elif page == "Register":
    st.subheader("Create New Account")
    
    with st.form("register_form"):
        st.caption("Fields marked with a red asterisk (*) are required.")
        new_username = st.text_input("Username *")
        new_email = st.text_input("Email *")
        new_password = st.text_input("Password *", type="password")
        confirm_password = st.text_input("Confirm Password *", type="password")
        
        submit_button = st.form_submit_button("Register")
        
        if submit_button:
            if not new_username or not new_email or not new_password or not confirm_password:
                st.error("Please fill in all required fields.")
            elif new_password != confirm_password:
                st.error("Passwords do not match.")
            else:
                st.success(f"Account created for {new_username}! Please login.")
                st.balloons()

# Login Page
elif page == "Login":
    st.subheader("Login to Your Account")
    
    with st.form("login_form"):
        st.caption("Fields marked with a red asterisk (*) are required.")
        username = st.text_input("Username *")
        password = st.text_input("Password *", type="password")
        
        login_button = st.form_submit_button("Login")
        
        if login_button:
            if username and password:
                # Simple demo authentication
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Please fill in all required fields.")

# Dashboard Page
elif page == "Dashboard":
    st.subheader(f"📊 Your Mood Dashboard")
    
    if len(st.session_state.moods) == 0:
        st.info("No mood entries yet. Start tracking your mood!")
        st.image("https://via.placeholder.com/800x400?text=Start+Tracking+Your+Mood", use_column_width=True)
    else:
        df = pd.DataFrame(st.session_state.moods)
        
        # Statistics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Entries", len(df))
        with col2:
            st.metric("Average Mood", f"{df['mood_score'].mean():.1f}/10")
        with col3:
            st.metric("Best Mood", f"{df['mood_score'].max()}/10")
        with col4:
            st.metric("Lowest Mood", f"{df['mood_score'].min()}/10")
        
        st.write("")
        
        # Mood trend chart
        fig = px.line(df, x='timestamp', y='mood_score', 
                     title='Mood Trend Over Time',
                     labels={'mood_score': 'Mood Score', 'timestamp': 'Date/Time'})
        fig.update_traces(line_color='#667eea', line_width=3)
        st.plotly_chart(fig, use_container_width=True)
        
        # Recent entries
        st.subheader("Recent Mood Entries")
        recent = df.tail(5).sort_values('timestamp', ascending=False)
        for _, row in recent.iterrows():
            with st.expander(f"🕐 {row['timestamp']} - Score: {row['mood_score']}/10"):
                st.write(f"**Sentiment:** {row['sentiment']}")
                st.write(f"**Comment:** {row['comment']}")
                st.write(f"**Location:** {row['location']}")

# Add Mood Page
elif page == "Add Mood":
    st.subheader("Record Your Current Mood")
    
    with st.form("mood_form"):
        st.caption("Fields marked with a red asterisk (*) are required.")
        col1, col2 = st.columns(2)
        
        with col1:
            mood_score = st.slider("How are you feeling? (1-10) *", 1, 10, 5)
            sentiment = st.selectbox("Overall Sentiment *",
                                    ["Very Negative", "Negative", "Neutral", "Positive", "Very Positive"])
        
        with col2:
            location = st.text_input("Location (e.g., Library, Cafeteria) *")
            comment = st.text_area("Additional Comments (optional)")
        
        submit = st.form_submit_button("Submit Mood Entry")
        
        if submit:
            if not location:
                st.error("Please fill in all required fields.")
            else:
                mood_entry = {
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'mood_score': mood_score,
                    'sentiment': sentiment,
                    'comment': comment if comment else "No comment",
                    'location': location
                }
                st.session_state.moods.append(mood_entry)
                st.success("Mood entry recorded successfully! 🎉")
                st.balloons()

# Analytics Page
elif page == "Analytics":
    st.subheader("📈 Mood Analytics")
    
    if len(st.session_state.moods) == 0:
        st.warning("No data available for analytics. Start tracking your mood first!")
    else:
        df = pd.DataFrame(st.session_state.moods)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Sentiment distribution
            sentiment_counts = df['sentiment'].value_counts()
            fig1 = px.pie(values=sentiment_counts.values, 
                         names=sentiment_counts.index,
                         title='Sentiment Distribution',
                         color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            # Mood score distribution
            fig2 = px.histogram(df, x='mood_score', 
                              title='Mood Score Distribution',
                              labels={'mood_score': 'Mood Score'},
                              color_discrete_sequence=['#667eea'])
            st.plotly_chart(fig2, use_container_width=True)
        
        # Location analysis
        if df['location'].nunique() > 1:
            st.subheader("Mood by Location")
            location_mood = df.groupby('location')['mood_score'].mean().sort_values(ascending=False)
            fig3 = px.bar(x=location_mood.index, y=location_mood.values,
                         title='Average Mood Score by Location',
                         labels={'x': 'Location', 'y': 'Average Mood Score'},
                         color=location_mood.values,
                         color_continuous_scale='Viridis')
            st.plotly_chart(fig3, use_container_width=True)

# Export Data Page
elif page == "Export Data":
    st.subheader("💾 Export Your Data")
    
    if len(st.session_state.moods) == 0:
        st.warning("No data to export")
    else:
        df = pd.DataFrame(st.session_state.moods)
        
        st.write(f"Total entries: {len(df)}")
        st.write("")
        
        # Preview data
        st.subheader("Data Preview")
        st.dataframe(df, use_container_width=True)
        
        st.write("")
        
        # Export options
        col1, col2 = st.columns(2)
        
        with col1:
            csv = df.to_csv(index=False)
            st.download_button(
                label="📥 Download as CSV",
                data=csv,
                file_name=f"mood_data_{st.session_state.username}_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
        
        with col2:
            json_data = df.to_json(orient='records', indent=2)
            st.download_button(
                label="📥 Download as JSON",
                data=json_data,
                file_name=f"mood_data_{st.session_state.username}_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json"
            )

# Footer
st.write("")
st.write("")
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Campus Mood Mapper | Created by <strong>Shashwat Pathak</strong></p>
    <p>SY BSc Data Science Project | 2025</p>
</div>
""", unsafe_allow_html=True)
