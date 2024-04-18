import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_community.llms import Ollama

os.environ["SERPER_API_KEY"] = "6f4bf44cf236dc72d561b0fefa972774ef231752"

llm = Ollama(model="openhermes")

search_tool = SerperDevTool()

