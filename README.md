# Explainit Crew

Welcome to the Explainit Crew project, powered by [crewAI](https://crewai.com). A basic CrewAI app that tries to explain given topics in simple terms.


## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `Llama` details into the `.env` file**

- Modify `src/explainit/config/agents.yaml` to define your agents
- Modify `src/explainit/config/tasks.yaml` to define your tasks
- Modify `src/explainit/crew.py` to add your own logic, tools and specific args
- Modify `src/explainit/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the explainIt Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.
