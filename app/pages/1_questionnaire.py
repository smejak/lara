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


def display_input_row(index):
    fm_name = st.text_input('Family Member Name', key=f'name_{index}')
    fm_rel = st.radio(f'What is your relationship to {fm_name}?', ['Mother', 'Father', 'Sister', 'Brother', 'Cousin', 'Son', 'Daughter', 'Grandson', 'Grand daughter', 'Niece', 'Nephew', 'Aunt', 'Uncle', 'Friend', 'Other'], key=f'rel_{index}')
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
    st.subheader('Family Members and Friends')
    family_members = []
    
    if 'rows' not in st.session_state:
        st.session_state['rows'] = 0

    def increase_rows():
        st.session_state['rows'] += 1

    for i in range(st.session_state['rows']):
        fm = display_input_row(i)
        family_members.append(fm)

    st.button('Add person', on_click=increase_rows)
    

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
            'Name': name,
            'Current Address': address,
            'Apartment Info': apartment_info,
            'Data of Birth': dob,
            'Place of Birth': pob,
            'Key Personal History Information': history,
            'cv_upload': cv_upload,
            'Family Members Information': family_members,
            'Medication Information': medication_info,
            'Medical Conditions': medical_conditions,
            'Key Areas of Assistance': areas_of_assistance,
            'Memmory Restore Triggers': memory_triggers,
            'Emergency Contacts': emergency_contacts,
            'Emergency Procedures': emergency_procedures,
            'Legal Documents Location': legal_docs_location,
            'Dietary Preferences': dietary_preferences
        }
        save_onboarding_outputs(outputs)
        st.session_state.submitted = True

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
        
def retrieval_animation():
    st.title("AI Assistant Lara - Loading...")
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f"Retrieving onboarding information... {i+1}%")
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
    retrieval_animation()

else:
    display_onboarding_form()
