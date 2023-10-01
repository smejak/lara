import streamlit as st
from datetime import datetime

# Set the title of the app
st.title('Daily Diary')

# Automatically fetch the current date and time
current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Date and Time Stamp (Automatically fetched)
st.subheader('Date and Time')
st.write(current_datetime)

# Mood and Emotions
st.subheader('Mood and Emotions')
st.write("Select your mood using emojis:")
selected_mood = st.radio("", ['😄 Happy', '😊 Content', '😐 Neutral', '😞 Sad', '😢 Very Sad'])

# Activities
st.subheader('Activities')
activities = st.text_area('List down the activities you engaged in today.')

# Daily Questions
st.subheader('Daily Questions')
highlight = st.text_area('What were the highlight of your day?')

# Family and Friends
interactions = st.text_area('Mention any interactions with family, friends, or caregivers.')

# Other Important information
interactions = st.text_area('What are the other important information I should be aware of?')


# Privacy and Security
st.subheader('Privacy and Security')
st.write("Your diary entries are stored securely. You do not have to worry!")