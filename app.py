# Import streamlit for our interface
import streamlit as st

# We need these for the wordware POST request
import json
import requests 

# We need these to get our API_KEY
import os
from dotenv import load_dotenv

###############################################################################################################################

# '''
# A GENERAL WORDWARE INTERFACE FUNCTION THAT HANDLES OUR POST REQUEST AND RESPONSE
# This is based on the example from last week.
# '''

def wordware(inputs, prompt_id, api_key):

    response = requests.post(
        f"https://app.wordware.ai/api/released-app/{prompt_id}/run",
        json={"inputs": inputs},
        headers={"Authorization": f"Bearer {api_key}"},
        stream=True,
    )

    if response.status_code != 200:
        print("Request failed with status code", response.status_code)
    else:
        # Successful api call
        for line in response.iter_lines():
            if line:
                content = json.loads(line.decode("utf-8"))
                value = content["value"]
                # We can print values as they're generated
                if value["type"] == "generation":
                    if value["state"] == "start":
                        print("\nNEW GENERATION -", value["label"])
                    else:
                        print("\nEND GENERATION -", value["label"])
                elif value["type"] == "chunk":
                    print(value["value"], end="")
                elif value["type"] == "outputs":
                    # Or we can read from the outputs at the end
                    # Currently we include everything by ID and by label - this will likely change in future in a breaking
                    # change but with ample warning
                    print("\nFINAL OUTPUTS:")
                    print(json.dumps(value, indent=4))

###############################################################################################################################

# Use streamlit to give us text and number inputs
subject = st.text_input(
    "Enter your location address",
)


days = st.number_input(
    "Trip Duration (Days)", step=1, min_value=1, max_value=12
)



# Create a form
form = st.form("my_form")

# Add a number input inside the form
days = form.number_input(
    "Trip Duration (Days)", step=1, min_value=1, max_value=12
)

# Add a submit button to the form
submitted = form.form_submit_button("Submit")

# Check if the form has been submitted
if submitted:
    st.write(f"Trip duration: {days} days")
