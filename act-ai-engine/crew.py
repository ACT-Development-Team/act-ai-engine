from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq
import tools.coingecko_tool
import tools.yahoo_finance_tool

@CrewBase
class ACTAIEngine():
    """ACT AI Engine Crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        self.groq_llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")


#Agents 
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config = self.agents_config['researcher'],
            llm = self.groq_llm, #this will be changed to ChatGPT 
            tools = [tools.coingecko_tool(), tools.yahoo_finance_tool()] #not test yet
        )
    
    @agent
    def accountant(self) -> Agent:
        return Agent(
            config = self.agents_config['accountant'],
            llm = self.groq_llm
        )
    
    @agent
    def recommender(self) -> Agent:
        return Agent(
            config = self.agents_config['recommender'],
            llm = self.groq_llm #this will be local ollama / tbd
        )
    
    @agent
    def blogger(self) -> Agent:
        return Agent(
            config = self.agents_config['blogger'],
            llm = self.groq_llm #this will be local ollama / mistral
        )
    
#Tasks 

    @task
    def research_stock_task(self) -> Task:
        return Task(
            config = self.tasks_config['research_stock_task'],
            agent = self.researcher()
        )
    
    @task
    def accounting_task(self) -> Task:
        return Task(
            config = self.tasks_config['accounting_task'],
            agent = self.accountant()
        )
    
    @task
    def recommendation_task(self) -> Task:
        return Task(
            config = self.tasks_config['recommendation_task'],
            agent = self.recommender()
        )
    
    @task
    def blogging_task(self) -> Task:
        return Task(
            config = self.tasks_config['blogging_task'],
            agent = self.blogger()
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = [self.researcher(),self.accountant(),self.recommender(),self.blogger()],
            tasks = [self.research_stock_task(),self.accounting_task(),self.recommendation_task(),self.blogging_task()],
            process = Process.sequential,
            verbose = True
        )

