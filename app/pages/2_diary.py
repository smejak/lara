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

# Set the title of the app
st.title('Daily Diary/Journal')

# Check if there's a list of entries already stored
if 'entries' not in st.session_state:
    st.session_state.entries = []

# Section to write a new diary/journal entry
st.subheader('Write a New Entry')
new_entry = st.text_area('Your Entry...')

if st.button('Submit Entry'):
    # Attach a timestamp to the entry
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    st.session_state.entries.append((timestamp, new_entry))
    
    # Store the updated list of entries in a pickle file
    with open('diary_entries.pickle', 'wb') as file:
        pickle.dump(st.session_state.entries, file)

    st.success('Entry saved!')

# Section to display all the entries for the specific date
current_date = datetime.now().strftime('%Y-%m-%d')
st.subheader(f'{current_date} Entries')

# Filter the entries to show only those from the current date
today_entries = [(time, entry) for timestamp, entry in st.session_state.entries if timestamp.startswith(current_date)]

if today_entries:
    for time, entry in today_entries:
        st.markdown(f"**{time.split(' ')[1]}**")  # Only displaying the time part of the timestamp
        st.write(entry)
        st.write('---')  # adds a separator line for better readability
else:
    st.write(f"No entries for {current_date} yet!")
