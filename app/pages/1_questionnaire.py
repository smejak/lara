import streamlit as st


# Set the title of the app
st.title('Onboarding Questionnaire')

# Onboarding Section

# Name
name = st.text_input('Name')

# Address
address = st.text_input('Address')
apartment_info = st.text_area('Apartment Details', 
                              'Describe the apartment, how the building looks, where the entrance is located, how to get to the entrance, and how to navigate from the entrance to the apartment.')

# Date of Birth and Place of Birth
dob = st.date_input('Date of Birth')
pob = st.text_input('Place of Birth')

# Personal History
history = st.text_area('Personal History', 'Please provide a brief personal history.')
cv_upload = st.file_uploader("Or, upload your CV for faster onboarding", type=["pdf", "docx"])

# Family/Close People Information
st.subheader('Family Members')
family_members = []


fm_name = st.text_input('Family Member name')

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True
    st.session_state.family_members 

st.button('Click me', on_click=click_button)

if st.session_state.clicked:
    # The message and nested widget will remain on the page
    st.write('Button clicked!')
    st.slider('Select a value')


if st.button('Add Family Member'):
    family_members.append({})
    st.subheader(f'Family Member {fm_name}')
    fm_info = st.text_area(f'Detailed Information about {fm_name} {fm_name}')
    fm_status = st.radio(f'Is {fm_name} Alive? {fm_name}', ['Alive', 'Deceased'])
    if fm_status == 'Deceased':
        st.date_input(f'Date of Passing for {fm_name} {fm_name}')

# st.button('Add Family Member', add_fm)


# for idx, _ in enumerate(family_members):
#     st.subheader(f'Family Member {idx+1}')
#     fm_name = st.text_input(f'Name {idx+1}')
#     fm_info = st.text_area(f'Detailed Information about {fm_name} {idx+1}')
#     fm_status = st.radio(f'Is {fm_name} Alive? {idx+1}', ['Alive', 'Deceased'])
#     if fm_status == 'Deceased':
#         st.date_input(f'Date of Passing for {fm_name} {idx+1}')

# Health Information
st.subheader('Health Information')
medication_info = st.text_area('Medication Details', 'List down the medications and their dosing.')
medical_conditions = st.text_area('Medical Conditions', 'Describe the conditions and their implications for life, e.g., allergies.')

# Areas of Assistance
areas_of_assistance = st.multiselect('Select Needed Areas of Assistance', 
                                     ['Groceries', 'Doctors', 'Relatives', 'Appointments', 'Navigation', 'Introduction'])

# Memory Triggers
memory_triggers = st.text_area('Memory Triggers', 'List down triggers or cues that help in recalling memories.')

# Emergency Contacts and Procedures
emergency_contacts = st.text_area('Emergency Contacts', 'List down names and phone numbers of emergency contacts.')
emergency_procedures = st.text_area('Emergency Procedures', 'Describe any specific procedures to follow in emergencies.')

# Other Information
st.subheader('Other Information')
legal_docs_location = st.text_input('Location of Legal Documents')
dietary_preferences = st.text_area('Dietary Preferences / Restrictions')

# Submit Button
if st.button('Submit Onboarding Information'):
    st.write('Thank you for providing the information. We will process and store it securely.')

