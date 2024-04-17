from crewai import Task
from textwrap import dedent
from datetime import date


class ResearchTasks():
  def __tip_section(self):
    return "If you do your BEST WORK, I'll tip you $100!"
  
  def technical_writer_task(self, agent):
    return Task(description=dedent(f"""
        Task: 
          Synthesize research findings into a comprehensive report on realistic avatars for online streaming.
        Description: 
          1. Collaborate with the other roles to gather and synthesize all research findings into a cohesive report.
          2. Clearly present all the information from other roles in an organized and engaging manner.
          3. Provide a clear conclusion and recommendation for the most promising development path based on the 
            research findings.
        Notes:
          {self.__tip_section()}
        """),
        expected_output=dedent(f"""
          1. A well-structured and informative consolidation of all the information from Visionary Director, Technical Architect, 
            and Audience Advocate roles
          2. The report should including ALL information from the Visionary Director, Technical Architect, and Audience
            Advocate roles, put them in organized way. DO NOT ignore any information in the reports of other agents.
          3. The report should give recommandation on most promising technical approach, addressing potential challenges,
            and providing a roadmap for future development.
        """),
        agent=agent)
  
  def vision_director_task(self, agent):
    return Task(description=dedent(f"""
        Task: 
          Research emerging technologies of reslistic avatar creation for online streaming.           
        Description:                       
          1. Research existing and emerging technologies for realistic avatar creation, including:
            1.1 Facial animation: 3D modeling, motion capture, facial rigging, expression transfer.
            1.2 Voice synthesis: Text-to-speech, voice cloning, emotional speech generation.
            1.3 Body movement and gesture recognition: Motion capture, pose estimation, full-body tracking.
            1.4 Machine learning and AI algorithms for avatar generation.
            1.5 Real-time rendering engines and streaming protocols.
          2. Identify leading opensource project on github, topics on reddit, or companies and research 
            institutions working in these areas.
          3. Analyze the capabilities and limitations of current technical approaches.
            3.1 Uncanny valley effects and realism thresholds.
            3.2 Performance and scalability issues for real-time rendering.
            3.3 Legal and ethical considerations for avatar use and representation.
          4. Explore the potential applications of realistic avatars in online streaming, including:
            4.1 Interactive live streams and virtual events.
            5.2 Personalized content creation and storytelling.
            6.3 Virtual influencers and digital celebrities.
        Notes: 
          {self.__tip_section()}
        """),
        expected_output=dedent(f"""
          1. A comprehensive report outlining the state-of-the-art in realistic avatar creation.
          2. Insights into the future possibilities and potential impact of this technology. 
        """),
        agent=agent)

  def technical_architect_task(self, agent):
    return Task(description=dedent(f"""
        Task: 
          Research implementation approaches for realistic avatar creation for the streaming purpose.                       
        Description: 
          1. Search and investigate throughly from github and reddit for the existing framework and projects.
          2. Evaluate different technical approaches for creating realistic avatars for live streaming, 
            including:
            2.1 realistic model-based avatars: Analyze rigging complexity, animation techniques, and 
                real-time rendering requirements.
            2.2 Deep learning-based avatars: Explore generative adversarial networks (GANs) and other 
                deep learning models for avatar generation and animation.
            2.3 Hybrid approaches: Investigate combining 3D models with deep learning for enhanced 
                realism and flexibility.
            2.4 Integration of voice synthesis and speech recognition.
          3. Assess hardware and software needs for each approach, including processing power, GPUs, and 
            specialized software tools.
          4. Investigate cloud-based solutions and potential infrastructure costs.
          5. Identify potential technical challenges and limitations of implementing realistic avatars for 
            live streaming. Propose solutions or workarounds for addressing these challenges.
        Notes:
          {self.__tip_section()}
        """),
        expected_output=dedent(f"""
          1. A technical feasibility report comparing different approaches, outlining their pros and cons, 
            resource requirements, and potential challenges, DO LIST the similar project on github for each 
            of the approaches.
          2. Recommendations for the most viable technical approach based on project goals and constraints.
        """),
        agent=agent)

  def audience_advocate_task(self, agent):
    return Task(description=dedent(f"""
        Task: 
          Research the user experience and ethical implications of realistic avatars for online streaming.
        Description: 
          1. Conduct audience research through surveys, interviews, and focus groups to understand:
            1.1 Perceptions and expectations of realistic avatars in online streaming.
            1.2 Desired levels of interactivity and engagement.
            1.3 Potential concerns regarding privacy, authenticity, and the uncanny valley effect.
          2. Investigate ethical considerations surrounding the use of realistic avatars, such as potential for 
            misuse, deepfakes, and bias.
          3. Analyze existing online communities and virtual influencers to understand audience engagement dynamics.
        Notes:
          {self.__tip_section()}
        """),
        expected_output=dedent(f"""
          1. A comprehensive report summarizing audience research findings and identifying key considerations for 
            developing engaging and ethical realistic avatar experiences.
          2. Recommendations for responsible development and deployment of the technology to ensure audience trust 
            and acceptance.
        """),
        agent=agent)
