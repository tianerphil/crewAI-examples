from crewai import Task
from textwrap import dedent
from datetime import date


class TravelTasks():
  def __tip_section(self):
    return "If you do your BEST WORK, I'll tip you $100!"

  def plan_itinerary(self, agent, origin, cities, date_range, interests):
    return Task(description=dedent(f"""
        **Task**: Develop a 7-day Travel Itinerary
        **Description**: Expand guide into a a full 7-day travel 
        itinerary with detailed per-day plans, including weather 
        forecasts, places to eat, packing suggestions, and a budget
        breakdown. You MUST suggest actual places to visit, actual
        hotels to stay and actual restaurants to go to. This itinerary
        should cover all aspects of the trip, from arrival to departure,
        integrating the city guide information with practical travel
        logistics. 
        
        **Parameters**:
        Travelling from: {origin}
        Travelling to: {cities}
        Trip Date: {date_range}
        Traveler Interests: {interests}

        **Notes**:{self.__tip_section()}
        """),
        expected_output=dedent(f"""
        Your final answer must be a detailed 7-day travel itinerary,
        formatted as markdown, with detailed per-day plans and each day's time tables for acitivities, 
        the itinerary should also include factors such as
        weather forecasts, places to eat, packing suggestions, and a
        budget breakdown. Be sure to suggest actual places to visit,
        actual hotels to stay, and actual restaurants to go to. The
        itinerary should cover all aspects of the trip, from arrival to
        departure, integrating the city guide information with practical
        travel logistics. 
        """),
        agent=agent)

  def identify_cities(self, agent, origin, cities, interests, date_range):
    return Task(description=dedent(f"""
        **Task**: Analyze and Select the Best City for the Trip 
          
        **Description**: Analyze and select the best city for the trip based on 
        specific criteria such as weather patterns, seasonal events, and travel costs.
        This task involves comparing multiple cities, considering factors like current
        weather conditions, upcoming cultural or seasonal events, and overall travel expenses.
        
        **Parameters**:
        Travelling from: {origin}
        Travelling to: {cities}
        Trip Date: {date_range}
        Traveler Interests: {interests}

        **Notes**:{self.__tip_section()}
        """),

        expected_output=dedent(f"""
        Your final answer must be a detailed analysis of the best city
        to visit, based on specific criteria such as weather patterns,
        seasonal events, and travel costs. Be sure to compare multiple
        cities, considering factors like current weather conditions,
        upcoming cultural or seasonal events, and overall travel expenses.
        """),
        agent=agent)

  def gether_city_info(self, agent, origin, interests, date_range):
    return Task(description=dedent(f"""
        **Task**: Gather Information for a City Guide
          
        **Description**: Compile an in-depth guide for someone traveling to the selected city
        and wanting to have THE BEST trip ever! Gather information about key attractions, local customs,
        special events, and daily activity recommendations. Find the best spots to go to, the kind of place only a
        local would know. This guide should provide a thorough overview of what the city has to offer, including hidden
        gems, cultural hotspots, must-visit landmarks, weather forecasts, and high level costs.
        
        **Parameters**:
        Travelling from: {origin}
        Trip Date: {date_range}
        Traveler Interests: {interests}

        **Notes**:{self.__tip_section()}
        """),
        expected_output=dedent(f"""
        Your final answer must be a detailed city guide,
        formatted as markdown, providing a comprehensive overview 
        of the city, including key attractions, local customs, special
        events, and daily activity recommendations. Be sure to include
        weather forecasts, high level costs, and any other relevant 
        information that would be useful to a traveler.
        """),
        agent=agent)



