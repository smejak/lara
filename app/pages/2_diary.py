import streamlit as st
from datetime import datetime
import pickle

# Set the title of the app
st.title('Daily Diary')

# Check for the submission state
if 'daily_submitted' not in st.session_state:
    st.session_state.daily_submitted = False

# Automatically fetch the current date and time
current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if not st.session_state.daily_submitted:
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
    other_info = st.text_area('What are the other important information I should be aware of?')

    # Privacy and Security
    st.subheader('Privacy and Security')
    st.write("Your diary entries are stored securely. You do not have to worry!")

    # Submit Button
    if st.button('Submit Diary Entry'):
        # Create a dictionary to store the daily diary outputs
        daily_outputs = {
            'current_datetime': current_datetime,
            'selected_mood': selected_mood,
            'activities': activities,
            'highlight': highlight,
            'interactions': interactions,
            'other_info': other_info
        }

        # Specify the file path where you want to save the pickle file
        daily_file_path = 'daily_outputs.pickle'

        # Open the file in binary mode and write the dictionary to the file
        with open(daily_file_path, 'wb') as file:
            pickle.dump(daily_outputs, file)

        # Close the file
        file.close()
        st.session_state.daily_submitted = True

else:
    st.subheader('Thank you for providing today\'s diary entry!')
    with open(f'daily_outputs_{current_datetime}.pickle', 'rb') as file:
        daily_outputs = pickle.load(file)
    for k, v in daily_outputs.items():
        st.write(f"**{k.capitalize().replace('_', ' ')}:** {v}")
