!pip install langchain
!pip install openai


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

os.environ['OPENAI_API_KEY'] = "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"
llm=OpenAI(temperature=0.0)

csv_agent_1=create_csv_agent(llm, 'ESGenius/genai_fact_3.csv', verbose=True)
csv_agent_2=create_csv_agent(llm, 'ESGenius/carbon_levers_file.csv', verbose=True)

overall_chain = SimpleSequentialChain(chains=[csv_agent_1, csv_agent_2], verbose=True)
response = overall_chain.run("Find the most poluuting facility. Once we have the facility, pick the most polluting category for each Source Type. Finally, based on Categories found, recommend Actions that I should take.")

return response