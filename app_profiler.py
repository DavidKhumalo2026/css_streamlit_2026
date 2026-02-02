import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile Page with STEM Data")

# Collect basic information
name = "David Vusumuzi Khumalo"
field = "Sport and Exercise Science"
institution = "University of the Witwatersrand"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://lorush.com/wp-content/uploads/2023/05/sport1.png",
    caption="Optimising performance (Lorush)"
)

# Researcher qualifications, interest, and affiliation
Qualifications = "BSc(Hons),MBA,MSc(Med)"
Interest = "Physical activity epidemiology,Exerkines,Metabolic syndrome"
Affiliation = "South Africa Sports Medicine Association (SASMA)"
ORCiD= "https://orcid.org/0000-0003-2846-3907"

# Display basic profile information
st.header("Researcher Qualification, Interest, and Affiliation")
st.write(f"**Qualifications:** {Qualifications}")
st.write(f"**Interest:** {Interest}")
st.write(f"**Affiliation:** {Affiliation}")
st.write(f"**ORCiD:** {ORCiD}")

# Add a contact section
st.header("Contact Information")
email = "david.khumalo@gmail.com"
st.write(f"You can reach {name} at {email}.")








































