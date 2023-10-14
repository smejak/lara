import streamlit as st
from datetime import datetime
import pickle
import openai
from langchain.llms import OpenAI
from langchain import PromptTemplate

def eval_res(question, user_response):
    prompt_ = """
            You are LARA, an advanced digital assistant designed specifically to help people with dementia. Individuals with dementia often face challenges in recalling memories, recognizing familiar faces, and performing daily tasks. As the condition progresses, they might also find it challenging to navigate their surroundings, remember their medication schedules, or even recollect personal history and family details.
            Determine whether the user's answer to the following question makes sense, return OK or REPEAT depending on whether you think the user should have included more information.
            
            Example 1:

            Question: List down the activities you engaged in today
            User Response: Hello
            Verdict: REPEAT

            Example 2:
            Question: What were the highlight of your day? Mention any interactions with family, friends, or caregivers. What are the other important information I should be aware of?
            User Response: I went shopping today to Trader Joe's, this was at 11am. Then I met my daughter Claire for lunch at 1pm. Now I am in my house cooking pasta for dinner. I am looking forward to watching TV later.
            Verdict: OK
            
            Question:
            {question}

            User Response:
            {user_response}

            Be very pleasant, always address the patient by their name, have an empathetic tone.
            
            ###
            
            Output the Question response:

            """
            
    template = PromptTemplate(template=prompt_, input_variables=["question" ,"user_response"])
    
    llm = OpenAI(model_name="gpt-4", temperature=0.5, max_tokens=300)
    prompt = template.format(question=question, user_response=user_response)
    res = llm(prompt)

    return res

# Set the title of the app
st.title('Daily Diary')

# Check for the submission state
if 'daily_submitted' not in st.session_state:
    st.session_state.daily_submitted = False

if 'current_question' not in st.session_state:
    st.session_state.current_question = 1

if 'responses' not in st.session_state:
    st.session_state.responses = {}

# Automatically fetch the current date and time
current_datetime = datetime.now().strftime('%Y-%m-%d')

# Specify the file path where you want to save the pickle file
daily_file_path = f'data/daily_outputs_{current_datetime}.pickle'

def save_daily_outputs(daily_outputs):
    """Save data into json"""
    with open(daily_file_path, 'wb') as file:
        pickle.dump(daily_outputs, file)

def display_question(question, key):
    """Shows the next questions"""
    response = st.text_area(question)
    button_key = f"next_button_{st.session_state.current_question}"
    classified_res = eval_res(question, response)
    if st.button('Next', key=button_key):
        if response and (classified_res=="OK"):
            st.session_state.responses[key] = response
            st.session_state.current_question += 1
        else:
            st.warning('Please fill in the field before proceeding.')

def display_daily_form():
    # Mood and Emotions
    if st.session_state.current_question == 1:
        st.subheader('Mood and Emotions')
        st.write("Select your mood using emojis:")
        response = st.radio("", ['😄 Happy', '😊 Content', '😐 Neutral', '😞 Sad', '😢 Very Sad'], key='mood_radio')
        button_key = f"next_button_{st.session_state.current_question}"
        if st.button('Next', key=button_key):
            if response:
                st.session_state.responses['Day Mood'] = response
                st.session_state.current_question += 1
            else:
                st.warning('Please select a mood before proceeding.')

    # Activities
    elif st.session_state.current_question == 2:
        display_question('List down the activities you engaged in today.', 'Day Activities')

    # Daily Questions
    elif st.session_state.current_question == 3:
        display_question('What were the highlight of your day? Mention any interactions with family, friends, or caregivers. What are the other important information I should be aware of?', 'Day Highlight')

    # Privacy and Security
    elif st.session_state.current_question == 4:
        st.subheader('Privacy and Security')
        st.write("Your diary entries are stored securely. You do not have to worry!")
        button_key = f"submit_button_{st.session_state.current_question}"
        if st.button('Submit Diary Entry', key=button_key):
            st.session_state.responses['Record Datetime'] = current_datetime
            save_daily_outputs(st.session_state.responses)
            st.session_state.daily_submitted = True

if st.session_state.daily_submitted:
    st.subheader('Thank you for providing today\'s diary entry!')
    with open(daily_file_path, 'rb') as file:
        daily_outputs = pickle.load(file)
    for k, v in daily_outputs.items():
        st.write(f"**{k.capitalize().replace('_', ' ')}:** {v}")
else:
    display_daily_form()
