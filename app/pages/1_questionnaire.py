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

def display_input_row(index):
    fm_name = st.text_input('Family Member Name', key=f'name_{index}')
    fm_rel = st.radio(f'What is your relationship to {fm_name}?', ['Mother', 'Father', 'Sister', 'Brother', 'Cousin', 'Son', 'Daughter', 'Grandson', 'Grand daughter', 'Niece', 'Nephew', 'Aunt', 'Uncle', 'Other'], key=f'rel_{index}')
    if fm_rel == 'Other':
        fm_rel = st.text_input('Relationship status', key=f'rel2_{index}')
    fm_info = st.text_area(f'Detailed Information about {fm_name}.', key=f'info_{index}')
    fm_status = st.radio(f'Is {fm_name} Alive?', ['Alive', 'Deceased'], key=f'status_{index}')
    if fm_status == 'Deceased':
        fm_d_date = st.date_input(f'Date of Passing for {fm_name}', key=f'date_{index}')
    if 'rows' not in st.session_state:
        st.session_state['rows'] = 0

    family_member = {
        'name': fm_name,
        'relationship': fm_rel,
        'detailed_information': fm_info,
        'alive_status': fm_status
    }
    return family_member

# display_input_row(0)

def increase_rows():
    st.session_state['rows'] += 1

st.button('Add person', on_click=increase_rows)

for i in range(st.session_state['rows']):
    display_input_row(i)

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





# Show the results
st.subheader('People')
for i in range(st.session_state['rows']):
    st.write(
        f'Person {i+1}:',
        st.session_state[f'first_{i}'],
        st.session_state[f'middle_{i}'],
        st.session_state[f'last_{i}']
    )
