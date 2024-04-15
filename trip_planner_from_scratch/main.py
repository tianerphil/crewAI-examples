import os
from crewai import Crew

from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks

from dotenv import load_dotenv
load_dotenv()

# os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
# os.environ["OPENAI_ORGANIZATION"] = config("OPENAI_ORGANIZATION_ID")

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py

class TripCrew:
    def __init__(self, origin, cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()

        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.origin,
            self.cities,
            self.date_range,
            self.interests
        )

        identify_cities= tasks.identify_cities(
            city_selection_expert,
            self.origin,
            self.cities,
            self.interests,
            self.date_range
        )

        gether_city_info = tasks.gether_city_info(
            local_tour_guide,
            self.origin,
            self.interests,
            self.date_range
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_travel_agent, 
                    city_selection_expert, 
                    local_tour_guide],
            tasks=[plan_itinerary,
                   identify_cities, 
                   gether_city_info],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    origin = input(dedent("""Enter Origiin: """))
    cities = input(dedent("""Enter Cities: """))
    date_range = input(dedent("""Enter Date_range: """))
    interests = input(dedent("""Interestes: """))

    custom_crew = TripCrew(origin, cities, date_range, interests)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
