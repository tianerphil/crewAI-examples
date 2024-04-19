from crewai import Task, Agent
from textwrap import dedent

class ResearchTasks():
  #def __tip_section(self):
  #  return "If you do your BEST WORK, I'll tip you $100!"

  def topic_investigator_task(
      self, 
      agent : Agent, 
      TOPIC : str, 
      PRIMARY_GOAL : str | None = None
      ) -> Task:
      return Task(description=dedent(f"""
          1.Initial Topic Exploration (Considering TOPIC and PRIMARY_GOAL): Conduct a thorough 
          exploration of the provided topic: {TOPIC}, taking into account the research primary 
          goal: {PRIMARY_GOAL}. Utilize diverse online resources, academic databases, and relevant 
          news articles to gather comprehensive background information.
          2.Identify Key Research Questions: Analyze the initial exploration summary and formulate
          specific research questions aligned with the identified areas for deeper investigation 
          and {PRIMARY_GOAL}.
          """),
          expected_output=dedent(f"""
          1.A structured summary that defines the topic, outlines key subtopics, identifies relevant 
          statistics and controversies, and highlights areas for deeper investigation based on the
          goal: {PRIMARY_GOAL}. This summary will directly inform the subsequent research questions.
          2.A list of 3-5 clear and focused research questions directly derived from the findings of 
          the initial exploration and aligned with the topic and primary goal. These questions will 
          guide the Evidence Gatherer in their search for relevant sources.
          """),
          agent=agent)

  def evidence_getherer_task(
      self, 
      agent : Agent
      ) -> Task :
      return Task(description=dedent(f"""
          1.Source Acquisition: Utilize the research questions provided by Dr. Petrova to search for and 
          retrieve relevant sources such as academic papers, industry reports, and statistical datasets. Focus on 
          acquiring credible and diverse sources that address each research question from multiple perspectives.
          2.Data Extraction & Analysis: Analyze the gathered sources, extracting key findings and data 
          points that directly address the research questions. Employ appropriate data analysis techniques and 
          statistical methods to identify patterns, trends, and insights.
          """),
          expected_output=dedent(f"""
          1.A collection of annotated sources directly related to the EACH OF the research questions, NO NOT miss
          any research questions. Each source will have a brief description explaining how it addresses the 
          corresponding question.
          2.A structured summary of findings organized by each of the research questions. Each question will have a 
          dedicated section with key data points, relevant statistics, charts, and quotes from sources, 
          all clearly linked to the research question they address. DO NOT MISS any of the research questions.
          """),
          agent=agent)

  def data_analyst_task(
      self, 
      agent : Agent
      ) -> Task:
      return Task(description=dedent(f"""
          Data Interpretation: visit all the links provided by Dr. Chen one by one, do not miss any. 
          read, understand and analyze all of the content. extract all contents in relation to
          the research questions. identify key point, patterns, trends, correlations, and potential causations 
          to support answering research questions.
          """),
          expected_output=dedent(f"""
          A long, detailed narrative serve as a database, including all contents related to the research questions, 
          all data analysis evidences, findings, insights, visualizations (charts, graphs), identified trends, 
          and statistically significant observations you have found in the content which can help to answer the rearch questions. 
          This report will used to compose the final answer to the research report. This output will serve as a 
          crucial input and information pool for the Report Synthesizer.
          """),
          agent=agent)
  
  def report_synthesizer_task(
      self, 
      agent : Agent
      ) -> Task:
      return Task(description=dedent(f"""
          1.Insight Synthesis: Based on the Data Analyst (Dr. David Kim) output, synthesize all contents, key 
          insights and conclusions that directly address the research questions. give a clear, solid, exhausitive answer 
          to all of the research questions with data evidences. All research questions SHALL be answered DO NOT 
          ignore any of the research questions. 
          2.Report Drafting: considering all the output from Topic Investigator (Dr. Anya Petrova), and 
          Data Analyst (Dr. David Kim), generate the outline for the report. Write the research report following the 
          outline items. Integrate all the context information, data analysis findings and their implications into a 
          compelling narrative, finally addresses each research questions and guides the reader towards a comprehensive 
          understanding of the topic. 
          """),
          expected_output=dedent(f"""
          1.A refined draft of the detailed narrative to directly address each of research question one by one.
          all the research questions SHALL be answered in clear, solid, exhausitive manner with data and evidence.
          DO NOT miss any of the questions.
          2.A complete research report with all sections and sub-sections of the outline being explained thoughly 
          with data, information and findings insights revealed in the previous research process, all research 
          questions should be highlighted and answered thoughly, clearly with data and evidence. make the report 
          exausitive, convincing and engaging.
          """),
          agent=agent)
  