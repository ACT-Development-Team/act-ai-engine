import os
from dotenv import load_dotenv
from act_ai_engine_crew.crew.crew import ACTAIEngine

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

def run():
    inputs = {'symbol':'Apple'}
    
    ACTAIEngine().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()