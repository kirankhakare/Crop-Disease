import streamlit as st
from multiapp import MultiApp
from apps import tomato, pepper, potato, corn, cotton, apple, soybean # import your app modules here

app = MultiApp()

# Define the column layout
col1, col2 = st.columns([1, 4])

# Logo image in the first column
with col1:
    st.image("images23.png", width=150)

# Title in the second column
with col2:
    st.title("Crop Disease Classification and Treatment Recommendation System")

st.markdown("<h3>Objective:</h3> The goal of this project is to develop a robust crop disease classification system using machine learning techniques. The primary objective is to accurately identify and classify diseases affecting various crops, enabling early detection and timely intervention for crop protection.", unsafe_allow_html=True)

st.sidebar.markdown("<h4>Agriculture related information link</h4>", unsafe_allow_html=True)
st.sidebar.markdown("[Maharashtra Agriculture Department](https://krishi.maharashtra.gov.in/)")

st.sidebar.markdown("<h4>Weather forecast link</h4>", unsafe_allow_html=True)
st.sidebar.markdown("[OpenWeatherMap](https://openweathermap.org/)")

st.sidebar.markdown("<h4>Information about Crop Rate link</h4>", unsafe_allow_html=True)
st.sidebar.markdown("[Agmarknet](https://agmarknet.gov.in/)")

# Add all your application here
app.add_app("Tomato", tomato.app)
app.add_app("Pepper", pepper.app)
app.add_app("Potato", potato.app)
app.add_app("Corn", corn.app)
app.add_app("Cotton", cotton.app)
app.add_app("Apple", apple.app)
app.add_app("Soybean", soybean.app)
# The main app


app.run()
