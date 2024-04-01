import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout= "wide")

df = pd.read_csv("india.csv")
list_of_state = list(df["State"].unique())
list_of_state.insert(0, "Overall India")

list_of_primary_parameter = sorted(df.columns[5:])

st.sidebar.title("Indian Census Visualization")

selected_state = st.sidebar.selectbox("Select State", list_of_state)
primary = st.sidebar.selectbox("Select Primary Parameter", list_of_primary_parameter)
secondary = st.sidebar.selectbox("Select Secondary Parameter", list_of_primary_parameter)

plot = st.sidebar.button("Plot Graph")

if plot:
    st.text("Size of Bubble ----> Primary Parameter")
    st.text("Color Represents ----> Secondary Parameter")
    if selected_state == "Overall India":
        # Plot for India
        fig = px.scatter_mapbox(df, lat= "Latitude", lon= "Longitude", size= primary, color= secondary, zoom= 5,
                                mapbox_style= "carto-positron", width= 800, height= 800, hover_name= "District")
        st.plotly_chart(fig, use_container_width= True)

    else:
        # Plot for state
        state_df = df[df["State"] == selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=5,
                                mapbox_style="carto-positron", width=800, height=800, hover_name= "District")
        st.plotly_chart(fig, use_container_width=True)