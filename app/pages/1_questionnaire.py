import streamlit as st
import time
import json
from llama_hub.file.pymu_pdf.base import PyMuPDFReader
import datetime


def date_serializer(obj):
    """Custom serializer for date objects"""
    import datetime
    
    # Handle datetime objects
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    
    # Handle date objects
    if isinstance(obj, datetime.date):
        return obj.isoformat()

    raise TypeError("Type not serializable")


### SUPPORTING CODE ###
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
    with open(file_path, 'r') as file:
        outputs = json.load(file)
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
    with open(file_path, 'r') as file:
        outputs = json.load(file)
    for k, v in outputs.items():
        st.write(f"**{k.capitalize().replace('_', ' ')}:** {v}")


def save_onboarding_outputs(outputs, medicine):
    """Write the onboarding info into the file path"""
    with open(file_path, 'w') as file:
        print(outputs)
        json.dump(outputs, file, default=date_serializer)
    with open('data/onboarding_outputs.txt', 'w') as file:
        for k, v in outputs.items():
            file.write(f"{k.capitalize().replace('_', ' ')}: {v}\n")
    
    ## Save medicine info into a separate structured file for deterministic retrieval## 
    with open('data/medicine_info.json', 'w') as file:
        json.dump(medicine, file, default=date_serializer)
        

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


def display_medication_row(index):
    """
    Function to display medication input row.
    """
    if index != 0:  # To avoid placing a separator before the first entry
        st.markdown("---")
        
    med_name = st.text_input('Medicication Name', key=f'med_name_{index}')
    med_time = st.time_input('Time to take medicine', key=f'med_time_{index}')
    med_dosing = st.number_input('Dosing - Tablets', min_value=1, max_value=20, key=f'med_dosing_{index}')
    med_notes = st.text_input('Additional Notes', key=f'med_notes_{index}')
    
    return {
        'medication_name': med_name,
        'medicaction_time': med_time,
        'dosing_tablets': med_dosing,
        'additional_notes': med_notes,
    }


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
    if cv_upload is not None:
        with open(f'datapdf/{cv_upload.name}', "wb") as file:
            file.write(cv_upload.getvalue())


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
    st.subheader('Medication Details')
    medications_info = []
    
    if 'med_rows' not in st.session_state:
        st.session_state['med_rows'] = 0

    for i in range(st.session_state['med_rows']):
        med = display_medication_row(i)
        medications_info.append(med)

    add_med_button = st.button('Add Medicine Entry')
    remove_med_button = st.button('Remove Medicine Entry')

    if add_med_button:
        st.session_state['med_rows'] += 1

    if remove_med_button and st.session_state['med_rows'] > 0:
        st.session_state['med_rows'] -= 1

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
            'Medication Information': medications_info,
            'Medical Conditions': medical_conditions,
            'Key Areas of Assistance': areas_of_assistance,
            'Memmory Restore Triggers': memory_triggers,
            'Emergency Contacts': emergency_contacts,
            'Emergency Procedures': emergency_procedures,
            'Legal Documents Location': legal_docs_location,
            'Dietary Preferences': dietary_preferences
        }
        save_onboarding_outputs(outputs, medications_info)
        st.session_state.submitted = True


### MAIN PROGRAM ###
# Set the title of the app
st.title('Onboarding Questionnaire')

# Check for the submission state
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Specify the file path to save the json file
# TODO - this will change
file_path = 'data/onboarding_outputs.json'

if st.session_state.submitted:
    retrieval_animation()

else:
    display_onboarding_form()
