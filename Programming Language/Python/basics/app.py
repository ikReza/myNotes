import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px

DATA_URL = "crashes.csv"

st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a Streamlit dashboard that can be used to analyze motor vehicle collision in NYC 🚗")

@st.cache(persist=True)
def load_raw_data(nrows):
    df = pd.read_csv(DATA_URL, nrows=nrows)
    return df

raw_data = load_raw_data(1000)

if st.sidebar.checkbox("Show Summary", False):
    st.write("Showing summary", raw_data.describe())

if st.sidebar.checkbox("Show Raw Data", False):
    st.subheader("Raw Data")
    st.write(raw_data)
    st.write("Shape: ", raw_data.shape)
    if st.checkbox("Raw Data Columns: ", False):
        st.write("Columns: ", raw_data.columns)

@st.cache(persist=True)
def load_data(nrows):
    df = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[["CRASH_DATE", "CRASH_TIME"]])
    df.dropna(subset=["LATITUDE", "LONGITUDE"], inplace=True)
    lowercase = lambda x: str(x).lower()
    df.rename(lowercase, axis="columns", inplace=True)
    df.rename(columns={"crash_date_crash_time": "date/time"}, inplace=True)
    return df

data = load_data(10000)
        
st.header("Where are the most people injured in NYC?")
injured_people = st.sidebar.slider("Number of persons injured in vehicle collisions", 0, 19)
st.map(data.query("injured_persons >= @injured_people")[["latitude", "longitude"]].dropna(how="any"))

st.header("How many collisions occur during a given time of day?")
hour = st.sidebar.slider("Hour to look at", 0, 23)
data = data[data["date/time"].dt.hour == hour]

st.markdown("Vehicle collisions between %i:00 and %i:00" % (hour, (hour+1) % 24))

midpoint = (np.average(data["latitude"]), np.average(data["longitude"]))
st.write(pdk.Deck(
    map_style = "mapbox://styles/mapbox/light-v9",
    initial_view_state = {
        "latitude": midpoint[0],
        "longitude": midpoint[1],
        "zoom": 11,
        "pitch": 50
    },
    layers = [
        pdk.Layer(
            "HexagonLayer",
            data = data[["date/time", "latitude", "longitude"]],
            get_position = ["longitude", "latitude"],
            radius = 100,
            extruded = True,
            pickable = True,
            elevation_scale = 4,
            elevation_range = [0, 1000],           
        ),
    ],
))
    
st.subheader("Breakdown by minute between %i:00 %i:00" % (hour, (hour+1) % 24))
filtered = data[
    (data["date/time"].dt.hour >= hour) & (data["date/time"].dt.hour < (hour+1))
]
hist = np.histogram(filtered["date/time"].dt.minute, bins=60, range=(0,60))[0]
chart_data = pd.DataFrame({"minute": range(60), "crashes": hist})
fig = px.bar(chart_data, x="minute", y="crashes", hover_data=["minute", "crashes"], height=400)
st.write(fig)


if st.sidebar.checkbox("Show Modified Data", False):
    st.subheader("Modified Data")
    st.write(data)
    st.write("Shape: ", data.shape)
    if st.checkbox("Modified Data Columns: ", False):
        st.write("Columns: ", data.columns)