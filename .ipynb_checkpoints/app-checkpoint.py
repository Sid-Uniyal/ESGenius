#pip install langchain
#pip install openai

import streamlit as st
import time
import subprocess

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.agents import create_csv_agent
import os
from langchain.utilities import SerpAPIWrapper
from langchain.agents import Tool
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.prompts import PromptTemplate
from htmlTemplates import css, user_template
import re

st.markdown(
    """
    <style>
    .stApp {
        background-image: url('ESGenius/esg-background.jpg');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the page title
st.title("Welcome to ESGenius")

# Add a heading
#st.header("Welcome to my app!")

# Function to simulate a long-running process
def simulate_processing():
    # Add a delay to simulate processing
    time.sleep(3)

    
    
def Gen_AI_Core_Engine():        
    llm=OpenAI(temperature=0.0)

    csv_agent_1=create_csv_agent(llm, 'genai_fact_3.csv', verbose=True)
    csv_agent_2=create_csv_agent(llm, 'carbon_levers_file.csv', verbose=True)

    #overall_chain = SimpleSequentialChain(chains=[csv_agent_1, csv_agent_2], verbose=True)
    #response = overall_chain.run("Find the most poluuting facility. Once we have the facility, pick the most polluting category for each Source Type. Finally, based on Categories found, recommend Actions that I should take.")
    response_1 = csv_agent_1.run("Just print the name most polluting facility based on carbon emissions and name its Source Type & all source categories")
    text = response_1
    
    facility_name = re.search(r'is the (.+?) office', text).group(1)
    # Extract source type
    source_type = re.search(r'Source Type of (.+?) and', text).group(1)
    # Extract source category
    source_category = re.search(r'Source Category of (.+?)\.', text).group(1)
    
    input_2 = "List actions to take to alleviate emissions from {} and find the action nearest to {}".format(source_type,source_category)
    response_2 = csv_agent_2.run(input_2)
    
    st.write('Facility with highest carbon emission:', facility_name)
    st.write('Source Category:', source_category)
    st.write('Actions to take:', response_2)
    simulate_processing()
    st.success("Processing completed")
    
    #return response

#def run_python_file(file_path):
#    result = subprocess.run(["python", file_path], capture_output=True, text=True)
#    output = result.stdout.strip()
#    return output
    
# Add some text
st.write("ESGenius app will give you the methods to control your organizations carbon emissions. Please click the Generate button below to proceed")

key = st.text_input("Please enter OpenAi key", type='password')
if st.button('Add Key'):
    os.environ['OPENAI_API_KEY'] = key
    st.success("Key Added!")

if st.button("Generate"):
    # Display a spinner while processing
    with st.spinner("Processing..."):
        #output = subprocess.run(["python", "ESGenius/genai_core_engine.py"], capture_output=True, text=True)
        #output=Gen_AI_Core_Engine()
        Gen_AI_Core_Engine()
        #simulate_processing()
        #st.success("Processing completed")
        #st.code(output, language="python")
        #st.write(output)
        #st.write(output) #user_template.replace("{{MSG}}", output), unsafe_allow_html=True)

# Add more content
#st.subheader("Here are some key points:")
#st.markdown("- Point 1")
#st.markdown("- Point 2")
#st.markdown("- Point 3")
#output="Output from LLM will come here"
#st.write(output)

# Display an image
#st.image("image.jpg", caption="Image Caption", use_column_width=True)

# Show a dataframe
#import pandas as pd
#data = {'Name': ['John', 'Alice', 'Bob'], 'Age': [25, 30, 35]}
#df = pd.DataFrame(data)
#st.dataframe(df)

# Render a plot
#import matplotlib.pyplot as plt
#plt.plot([1, 2, 3, 4, 5], [10, 20, 30, 40, 50])
#st.pyplot(plt)

# Add a footer
#st.footer("Thank you for using my app!")