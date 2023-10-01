import streamlit as st
import pickle
import time


# Set the title of the app
st.title('Onboarding Questionnaire')

# Onboarding Section
# submitted = False

if 'submitted' not in st.session_state:
    st.session_state.submitted = False


if not st.session_state.submitted:
    # Name
    name = st.text_input('Name')

    # Address
    address = st.text_input('Address')
    apartment_info = st.text_area('Apartment Details', 
                                placeholder='Describe the apartment, how the building looks, where the entrance is located, how to get to the entrance, and how to navigate from the entrance to the apartment.')

    # Date of Birth and Place of Birth
    dob = st.date_input('Date of Birth')
    pob = st.text_input('Place of Birth')

    # Personal History
    history = st.text_area('Personal History', placeholder='Please provide a brief personal history.')
    cv_upload = st.file_uploader("Or, upload a PDF with supplementary information", type=["pdf", "docx"])

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

    if 'rows' not in st.session_state:
        st.session_state['rows'] = 0

    def increase_rows():
        st.session_state['rows'] += 1


    for i in range(st.session_state['rows']):
        fm = display_input_row(i)
        family_members.append(fm)

    st.button('Add person', on_click=increase_rows)
    # Health Information
    st.subheader('Health Information')
    medication_info = st.text_area('Medication Details', placeholder='List down the medications and their dosing.')
    medical_conditions = st.text_area('Medical Conditions', placeholder='Describe the conditions and their implications for life, e.g., allergies.')

    # Areas of Assistance
    areas_of_assistance = st.multiselect('Select Needed Areas of Assistance', 
                                        ['Groceries', 'Doctors', 'Relatives', 'Appointments', 'Navigation', 'Introduction'])

    # Memory Triggers
    memory_triggers = st.text_area('Memory Triggers', placeholder='List down triggers or cues that help in recalling memories.')

    # Emergency Contacts and Procedures
    emergency_contacts = st.text_area('Emergency Contacts', placeholder='List down names and phone numbers of emergency contacts.')
    emergency_procedures = st.text_area('Emergency Procedures', placeholder='Describe any specific procedures to follow in emergencies.')

    # Other Information
    st.subheader('Other Information')
    legal_docs_location = st.text_input('Location of Legal Documents')
    dietary_preferences = st.text_area('Dietary Preferences / Restrictions')

    # Submit Button
    if st.button('Submit Onboarding Information'):
        st.write('Thank you for providing the information. We will process and store it securely.')
        # Create a dictionary to store the outputs
        outputs = {
            'name': name,
            'address': address,
            'apartment_info': apartment_info,
            'dob': dob,
            'pob': pob,
            'history': history,
            'PDF_upload': cv_upload,
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

        # Specify the file path where you want to save the pickle file
        file_path = 'data/outputs.pickle'

        # Open the file in binary mode and write the dictionary to the file
        with open(file_path, 'wb') as file:
            pickle.dump(outputs, file)

        # Close the file
        file.close()
        submitted = True
        st.session_state.submitted = True
else:
    def loading_animation():
        st.title("AI Assistant Lara - Loading...")
        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
            latest_iteration.text(f"Generating AI Assistant Lara... {i+1}%")
            bar.progress(i + 1)
            time.sleep(0.05)  # Simulate loading time

        st.success("AI Assistant Lara has been generated!")
        st.balloons()

    # Display the loading animation
    loading_animation()

    st.subheader('Thank you for providing the information!')
    with open('data/outputs.pickle', 'rb') as file:
        outputs = pickle.load(file)
    for k, v in outputs.items():
        st.write(f"**{k.capitalize().replace('_', ' ')}:** {v}")


# if submitted:
#     st.subheader('Your Provided Information')
#     for k, v in outputs.items():
#         st.write(f"**{k.capitalize().replace('_', ' ')}:** {v}")

