import os
import pickle
import streamlit as st

from langchain.llms import OpenAI
from langchain import PromptTemplate


st.title("LARA's Notification Center")


def load_memory():
    data_folder = 'data/'
    pickle_files = [f for f in os.listdir(data_folder) if f.endswith('.pickle')]

    context = ''

    for file in pickle_files:
        with open(os.path.join(data_folder, file), 'rb') as f:
            data = pickle.load(f)
            context += str(data)

    print(context)
    return context

def querry_llm(context, user_input):
    prompt_ = """
            You are LARA, an advanced digital assistant designed specifically to help people with dementia. Individuals with dementia often face challenges in recalling memories, recognizing familiar faces, and performing daily tasks. As the condition progresses, they might also find it challenging to navigate their surroundings, remember their medication schedules, or even recollect personal history and family details.
            You are a version of LARA that helps dementia patients regain memory by replying to their questions.
            Use the Context below to answer the Question with relevant response. If you cannot find a relevant response, you can say "I don't know" in a pleasant way.
            

            Question:
            {user_input}
            
            Context:
            {context}

            Be very pleasant, always address the patient by their name, have an empathetic tone.
            
            ###
            
            Output the Question response:

            """
            
    template = PromptTemplate(template=prompt_, input_variables=["user_input" ,"context"])
    
    llm = OpenAI(model_name="gpt-4", temperature=0.5, max_tokens=300)
    prompt = template.format(context=context, user_input=user_input)
    res = llm(prompt)

    return res
    

####### RUNNING FROM HERE
context = load_memory()

st.subheader('Chat Interface')
user_input = st.text_input("How can LARA assist you today?", "")
if user_input:
    response = querry_llm(context, user_input)
    st.write(response.strip('"'))

    
