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


# Streamlit app title
st.header ("Publication")
st.write ("Effectiveness of high-intensity interval training and moderate-intensity continuous training on cardiometabolic health in university labourers")
# Input field for the file URL
url = st.text_input("https://doi.org/10.18772/26180197.2024.v6n1a4")


if st.button("Download paper"):
    if not url.strip():
        st.error("Please enter a valid URL.")
    else:
       try:
            # Download the file
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise error for bad status codes

            # Extract filename from URL
            filename = url.split("/")[-1] or "downloaded_file"

            # Create a BytesIO object for download
            file_data = BytesIO(response.content)

            # Show download button
            st.success(f"File '{filename}' fetched successfully!")
            st.download_button(
                label="Download File",
                data=file_data,
                file_name=filename,
                mime="application/octet-stream"
            )

# Add a contact section
st.header ("Contact Information")
email = "david.khumalo@gmail.com"
LinkedIn= "www.linkedin.com/in/david-vusumuzi-khumalo-1924a424"

st.write(f"You can reach {name} at {email} or {LinkedIn}.")

































