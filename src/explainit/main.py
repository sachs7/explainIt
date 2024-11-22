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


"""
Instead of dealing with the CLI, if you want to interact with the app
via browser, then:

1. comment above code block
2. install "streamlit" using: `uv pip install streamlit`
3. enable the following code block
"""


# #!/usr/bin/env python
# import sys
# import warnings
# import streamlit as st
# from explainit.crew import Explainit

# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# def process_topic(topic):
#     """
#     Process the input topic using Explainit.
#     """
#     inputs = {'topic': topic}
#     response = Explainit().crew().kickoff(inputs=inputs)
#     return response

# def run():
#     """
#     Run the Streamlit application.
#     """
#     st.title("ExplainIt")
#     st.write("Enter a topic below and click 'Run' to see the response.")

#     # Input field for the topic
#     topic_input = st.text_input("Topic", "")

#     # Button to run the processing
#     if st.button("Run"):
#         if topic_input:
#             # Call the processing function and display the result
#             response = process_topic(topic_input)
#             st.markdown(f"### Response:\n{response}")
#         else:
#             st.warning("Please enter a topic before clicking 'Run'.")

# if __name__ == "__main__":
#     run()
