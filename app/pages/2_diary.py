import streamlit as st
import pickle
from datetime import datetime

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
today_entries = [entry for entry in st.session_state.entries if entry[0].startswith(current_date)]

if today_entries:
    for timestamp, entry in today_entries:
        time_submitted = timestamp.split(' ')[1]  # Extracting the time part of the timestamp
        st.markdown(f"**{time_submitted}**")  # Displaying the time
        st.write(entry)
        st.write('---')  # adds a separator line for better readability
else:
    st.write(f"No entries for {current_date} yet!")
