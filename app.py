import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objects as go
import pickle
import numpy as np

def main():
    #print('Hello World, Streamlit app')
    st.set_page_config(
        page_title= "Cancer Predictor",
        page_icon=":female-doctor:",
        layout = "wide",
        initial_sidebar_state="expanded"
    )
    #st.write("Hello World")
 
    # with open("assets/style.css") as f:
    #     st.markdown("<stlye>{}</style>".format(f.read()), unsafe_allow_html=True)
 

    input_data = add_sidebar()
    #st.write(input_data) # just to test if it actually captures the data
 
    with st.container():
        st.title("Cancer Predictor")
        st.write("Connect this application to your simulation app to help diagnose the cancer form the tissue sample")
 
    col1, col2 = st.columns([4,1]) # sets the ratio of the columns
 
    with col1:
        #st.write("this is column 1")
        radar_chart = get_radar_chart(input_data)
        st.plotly_chart(radar_chart)
    with col2:
        #st.write("this is column 2")
        add_predictions(input_data)
 

if __name__ =='__main__':
    main()
