import streamlit as st
import pickle
import time

# Set the title of the app
st.title('Onboarding Questionnaire')

# Check for the submission state
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Specify the file path to save the pickle file
file_path = 'data/onboarding_outputs.pickle'

def save_onboarding_outputs(outputs):
    with open(file_path, 'wb') as file:
        pickle.dump(outputs, file)

def display_onboarding_form():
    # Name
    name = st.text_input('Name')
    
    # Address
    address = st.text_input('Address')
    apartment_info = st.text_area('Apartment Details', placeholder='Describe the apartment, how the building looks, where the entrance is, and more details.')

    # Date of Birth and Place of Birth
    dob = st.date_input('Date of Birth')
    pob = st.text_input('Place of Birth')

    # Personal History
    history = st.text_area('Personal History', placeholder='Please provide a brief personal history.')
    cv_upload = st.file_uploader("Or, upload a PDF with supplementary information", type=["pdf", "docx"])

    # Family/Close People Information
    family_members = st.text_area('Family Members', placeholder='List names and relationships.')

    # Health Information
    medication_info = st.text_area('Medication Details', placeholder='List down the medications and their dosing.')
    medical_conditions = st.text_area('Medical Conditions', placeholder='Describe the conditions and their implications.')

    # Areas of Assistance
    areas_of_assistance = st.multiselect('Select Needed Areas of Assistance', ['Groceries', 'Doctors', 'Relatives', 'Appointments', 'Navigation', 'Introduction'])

    # Memory Triggers
    memory_triggers = st.text_area('Memory Triggers', placeholder='List down triggers or cues that help in recalling memories.')

    # Emergency Contacts and Procedures
    emergency_contacts = st.text_area('Emergency Contacts', placeholder='List down names and phone numbers.')
    emergency_procedures = st.text_area('Emergency Procedures', placeholder='Describe any specific procedures to follow in emergencies.')

    # Other Information
    legal_docs_location = st.text_input('Location of Legal Documents')
    dietary_preferences = st.text_area('Dietary Preferences / Restrictions')

    # Submit Button
    if st.button('Submit Onboarding Information'):
        outputs = {
            'name': name,
            'address': address,
            'apartment_info': apartment_info,
            'dob': dob,
            'pob': pob,
            'history': history,
            'cv_upload': cv_upload,
            'family_members': family_members,
            'medication_info': medication_info,
            'medical_conditions': medical_conditions,
            'areas_of_assistance': areas_of_assistance,
            'memory_triggers': memory_triggers,
            'emergency_contacts': emergency_contacts,
            'emergency_procedures': emergency_procedures,
            'legal_docs_location': legal_docs_location,
            'dietary_preferences': dietary_preferences
        }
        save_onboarding_outputs(outputs)
        st.session_state.submitted = True
        loading_animation()

def loading_animation():
    st.title("AI Assistant Lara - Loading...")
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f"Processing onboarding information... {i+1}%")
        bar.progress(i + 1)
        time.sleep(0.05)  # Simulate loading time

    st.success("AI Assistant Lara has been generated!")
    st.balloons()

    st.subheader('Thank you for providing the onboarding information!')
    with open(file_path, 'rb') as file:
        outputs = pickle.load(file)
    for k, v in outputs.items():
        st.write(f"**{k.capitalize().replace('_', ' ')}:** {v}")

if st.session_state.submitted:
    st.subheader('Thank you for providing the onboarding information!')
    with open(file_path, 'rb') as file:
        outputs = pickle.load(file)
    for k, v in outputs.items():
        st.write(f"**{k.capitalize().replace('_', ' ')}:** {v}")
else:
    display_onboarding_form()
