import os
import pickle
import streamlit as st

from langchain.llms import OpenAI
from langchain import PromptTemplate


st.title("LARA's Notification Center")


data_folder = 'data/'
pickle_files = [f for f in os.listdir(data_folder) if f.endswith('.pickle')]

context = ''

for file in pickle_files:
    with open(os.path.join(data_folder, file), 'rb') as f:
        data = pickle.load(f)
        context += str(data)

print(context)

prompt_ = """
        You are LARA, an advanced digital assistant designed specifically to help people with dementia. Individuals with dementia often face challenges in recalling memories, recognizing familiar faces, and performing daily tasks. As the condition progresses, they might also find it challenging to navigate their surroundings, remember their medication schedules, or even recollect personal history and family details.
        You are a version of LARA that generates helpful reminders such as when to take medications, when to add another diary entry, etc.
        Use the context below to figure out what information is relevant to the patient. Be very pleasant, always address the patient by their name, have an empathetic tone.

        Context:
        {context}

        Reminder:

        """
template = PromptTemplate(template=prompt_, input_variables=["context"])



if st.button("Get Reminder"):
    llm = OpenAI(model_name="gpt-4", temperature=0.5, max_tokens=300)
    prompt = template.format(context=context)
    res = llm(prompt)

    st.write(res.strip('"'))
