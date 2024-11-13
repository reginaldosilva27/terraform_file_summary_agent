from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import DirectoryReadTool
from crewai_tools import FileReadTool
from crewai_tools import FileWriterTool

@CrewBase
class TerraformFileSummaryAgentCrew():
    """TerraformFileSummaryAgent crew"""

    @agent
    def terraform_reader(self) -> Agent:
        return Agent(
            config=self.agents_config['terraform_reader'],
            
        )
    
    @agent
    def databricks_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['databricks_specialist'],
        )

    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['report_generator'],
            
        )


    @task
    def read_terraform_files_task(self) -> Task:
        return Task(
            config=self.tasks_config['read_terraform_files_task'],
            tools=[DirectoryReadTool(), FileReadTool()],
        )
    
    @task
    def databricks_assessment(self) -> Task:
        return Task(
            config=self.tasks_config['databricks_assessment'],
        )

    @task
    def generate_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_report_task'],
            tools=[FileWriterTool()],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the TerraformFileSummaryAgent crew"""
        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
            track_usage=True
        )
