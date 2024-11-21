from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

import os


# Initialize the language model from OpenAI with the specified base URL and model
model = LLM(
            model=os.environ["MODEL"],
            base_url=os.environ["API_BASE"]
        )


@CrewBase
class Explainit:
    """Explainit crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            verbose=True,
            llm=model
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["reporting_analyst"],
            verbose=True,
            llm=model
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(config=self.tasks_config["reporting_task"], output_file="report.md")

    @crew
    def crew(self) -> Crew:
        """Creates the Explainit crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
