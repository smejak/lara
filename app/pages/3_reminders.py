import os
import pickle
import streamlit as st

st.title("LARA's Notification Center")


data_folder = 'data/'
pickle_files = [f for f in os.listdir(data_folder) if f.endswith('.pickle')]

for file in pickle_files:
    with open(os.path.join(data_folder, file), 'rb') as f:
        data = pickle.load(f)
        print(data)
