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
    def __init__(self, TOPIC, PRIMARY_GOAL):
        if TOPIC is None or not isinstance(TOPIC, str):
            raise ValueError("Please provide a valid TOPIC")
        else:
            self.TOPIC = TOPIC
            self.PRIMARY_GOAL = PRIMARY_GOAL
        print("## Creating crew for Research")


    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = ResearchAgents()
        tasks = ResearchTasks()

        # Define your custom agents and tasks here
        topic_investigator_agent = agents.topic_investigator()
        evidence_getherer_agent = agents.evidence_getherer()
        data_analyst_agent = agents.data_analyst()
        report_synthesizer_agent = agents.report_synthesizer()

        # Custom tasks include agent name and variables as input
        topic_investigator_task = tasks.topic_investigator_task(
            topic_investigator_agent, self.TOPIC, self.PRIMARY_GOAL)
        evidence_getherer_task= tasks.evidence_getherer_task(
            evidence_getherer_agent)
        data_analyst_task = tasks.data_analyst_task(
            data_analyst_agent)
        report_synthesizer_task = tasks.report_synthesizer_task(
            report_synthesizer_agent)
        
        evidence_getherer_task.context = [topic_investigator_task]
        data_analyst_task.context = [evidence_getherer_task]
        report_synthesizer_task.context = [data_analyst_task, topic_investigator_task]

        # Define your custom crew here
        crew = Crew(
            agents=[topic_investigator_agent,
                    evidence_getherer_agent, 
                    data_analyst_agent, 
                    report_synthesizer_agent],
            tasks=[topic_investigator_task,
                   evidence_getherer_task,
                   data_analyst_task, 
                   report_synthesizer_task],
            verbose=True,
            process=Process.sequential)

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Research Crew")
    print("-------------------------------")

    TOPIC = input(
        dedent("""
        Please tell me what topic come accross your dummy head today?
        """))
    PRIMARY_GOAL = input(
        dedent("""
        Please whisper me your primary goal for this research?
        """))
    
    custom_crew = ResearchCrew(TOPIC, PRIMARY_GOAL)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you Research Crew run result:")
    print("########################\n")
    print(result)
