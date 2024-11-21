#!/usr/bin/env python
import sys
import warnings

from explainit.crew import Explainit

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Aliens'
    }
    Explainit().crew().kickoff(inputs=inputs)
