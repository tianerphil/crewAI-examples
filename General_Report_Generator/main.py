import os
from crewai import Crew, Process

from textwrap import dedent
from agents import ResearchAgents
from tasks import ResearchTasks

from dotenv import load_dotenv
load_dotenv()

# os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
# os.environ["OPENAI_ORGANIZATION"] = config("OPENAI_ORGANIZATION_ID")

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py

class ResearchCrew:
    def __init__(self):
        print("## Creating crew for Research")

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = ResearchAgents()
        tasks = ResearchTasks()

        # Define your custom agents and tasks here
        vision_director_agent = agents.vision_director()
        technical_architect_agent = agents.technical_architect()
        audience_advocate_agent = agents.audience_advocate()
        technical_writer_agent = agents.technical_writer()

        # Custom tasks include agent name and variables as input
        vision_director_task = tasks.vision_director_task(
            vision_director_agent)

        technical_architect_task= tasks.technical_architect_task(
            technical_architect_agent)

        audience_advocate_task = tasks.audience_advocate_task(
            audience_advocate_agent)
        technical_writer_task = tasks.technical_writer_task(
            technical_writer_agent)
        
        # Define your custom crew here
        crew = Crew(
            agents=[audience_advocate_agent,
                    vision_director_agent, 
                    technical_architect_agent, 
                    technical_writer_agent],
            tasks=[audience_advocate_task,
                   vision_director_task,
                   technical_architect_task, 
                   technical_writer_task],
            verbose=True,
            process=Process.sequential)

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Research Crew")
    print("-------------------------------")

    custom_crew = ResearchCrew()
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you Research Crew run result:")
    print("########################\n")
    print(result)
