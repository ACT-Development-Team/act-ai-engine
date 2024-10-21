import os
from dotenv import load_dotenv
from act_ai_engine.crew import ACTAIEngine

load_dotenv()

def run():
    inputs = {'asset_name':'Tesla'}
    
    ACTAIEngine().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()