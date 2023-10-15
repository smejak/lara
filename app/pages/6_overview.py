import os
import pickle
import streamlit as st
import openai
import json
from langchain.llms import OpenAI
from langchain import PromptTemplate
from llama_hub.file.pymu_pdf.base import PyMuPDFReader
# from llama_index import VectorStoreIndex, ServiceContext, LLMPredictor
from llama_index import download_loader

from scipy.io.wavfile import write

# This module is imported so that we can 
# play the converted audio
import os
from datetime import datetime


st.title("LARA Overview")


def load_memory():
    data_folder = 'data/'
    pickle_files = [f for f in os.listdir(data_folder) if f.endswith('.json')]

    context = ''

    for file in pickle_files:
        with open(os.path.join(data_folder, file), 'rb') as f:
            data = json.load(f)
            context += str(data)
            
    # pdf_folder = 'datapdf/'
    # pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

    # for file in pdf_files:
    #     reader = PyMuPDFReader()
    #     PDFReader = download_loader("PDFReader")
    #     loader = PDFReader()
    #     documents = loader.load_data(file=os.path.join(pdf_folder, file))
    #     # index = VectorStoreIndex.from_documents(documents)
    #     # index.storage_context.persist()
    #     context += documents[0].text

    context += f'/n {datetime.now()}'

    return context

def querry_llm(context):
    prompt_ = """
            You are LARA, an advanced digital assistant designed specifically to help people with dementia. Individuals with dementia often face challenges in recalling memories, recognizing familiar faces, and performing daily tasks. As the condition progresses, they might also find it challenging to navigate their surroundings, remember their medication schedules, or even recollect personal history and family details.
            You are a version of LARA that helps dementia patients regain memory by replying to their questions.
            Use the Context below to compile and output relevant user information in a Markdown table format. If you cannot find a relevant piece of information, you can indicate "Not Available" in the table. If the user seems confused or you don't understand the question, guide them through simple breathing exercises to help them calm down.

            Context:
            {context}

            Output the user information in the following Markdown table format, create multiple tables for different type of infomation. Include three tables: Daily Highlights, General Information Table, Medical Records Table:
            
            Daily Highlights
            | FILL_IN | FILL_IN          |
            |------------------|------------------|
            | ...              | ...              |

            General Information Table
            | Information Type | Details          |
            |------------------|------------------|
            | Name             | [User's Name]    |
            | ...              | ...              |

            Medical Records Table
            | FILL_IN | FILL_IN          |
            |------------------|------------------|
            | ...              | ...              |


            """
            
    template = PromptTemplate(template=prompt_, input_variables=["context"])
    
    llm = OpenAI(model_name="gpt-4", temperature=0.5, max_tokens=300)
    prompt = template.format(context=context)
    res = llm(prompt)

    return res

####### RUNNING FROM HERE
context = load_memory()
if 'context' not in st.session_state:
    st.session_state.context = context

res = querry_llm(context)
    
st.write(res)