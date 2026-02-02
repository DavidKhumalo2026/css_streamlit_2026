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
st.title("Publication")

# Input field for the file URL
url = st.text_input("https://doi.org/10.18772/26180197.2024.v6n1a4")

if st.button("Fetch File"):
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

        except requests.exceptions.MissingSchema:
            st.error("Invalid URL format. Please include http:// or https://")
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching file: {e}")







# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add STEM Data Section
st.header("Explore STEM Data")

# Generate dummy data
physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# Tabbed view for STEM data
st.subheader("STEM Data Viewer")
data_option = st.selectbox(
    "Choose a dataset to explore", 
    ["Physics Experiments", "Astronomy Observations", "Weather Data"]
)

if data_option == "Physics Experiments":
    st.write("### Physics Experiment Data")
    st.dataframe(physics_data)
    # Add widget to filter by Energy levels
    energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
    filtered_physics = physics_data[
        physics_data["Energy (MeV)"].between(energy_filter[0], energy_filter[1])
    ]
    st.write(f"Filtered Results for Energy Range {energy_filter}:")
    st.dataframe(filtered_physics)

elif data_option == "Astronomy Observations":
    st.write("### Astronomy Observation Data")
    st.dataframe(astronomy_data)
    # Add widget to filter by Brightness
    brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
    filtered_astronomy = astronomy_data[
        astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
    ]
    st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
    st.dataframe(filtered_astronomy)

elif data_option == "Weather Data":
    st.write("### Weather Data")
    st.dataframe(weather_data)
    # Add widgets to filter by temperature and humidity
    temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
    humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
    filtered_weather = weather_data[
        weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
        weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
    ]
    st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
    st.dataframe(filtered_weather)

# Add a contact section
st.header("Contact Information")
email = "david.khumalo@gmail.com"
LinkedIn= "www.linkedin.com/in/david-vusumuzi-khumalo-1924a424"

st.write(f"You can reach {name} at {email}{LinkedIn}.")























