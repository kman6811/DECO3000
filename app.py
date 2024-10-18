import streamlit as st
from datetime import datetime

# Create a form
form = st.form("my_form")

location = form.text_input("Enter your location address")

# Date input widgets inside the form
start_date = form.date_input("Start Date")
end_date = form.date_input("End Date")

# Add a submit button to the form
submitted = form.form_submit_button("Submit")

# Perform calculations after form submission
if submitted:
    # Calculate the number of days between the dates, including the final day
    if start_date and end_date:
        delta_days = (end_date - start_date).days + 1
        st.write(f"The number of days for the trip is: {delta_days}")
    else:
        st.write("Please select both start and end dates.")
    
    # Display additional information
    st.write(f"Trip duration: {days} days")
    st.write(f"Address: {location}")