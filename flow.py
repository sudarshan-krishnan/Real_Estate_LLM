import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_community.llms import Ollama

os.environ["SERPER_API_KEY"] = "6f4bf44cf236dc72d561b0fefa972774ef231752"

llm = Ollama(model="openhermes")

search_tool = SerperDevTool()

researcher = Agent(
    llm=llm,
    role="Senior Property Researcher",
    goal="Find promising investment properties.",
    backstory="You are a veteran property analyst. In this case you're looking for retail properties to invest in.",
    allow_delegation=False,
    tools=[search_tool],
    verbose=True,
)

