import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Rainfall Prediction App",layout="centered")

st.title("Rainfall Prediction App")
st.write("Predict whether it will rain or not using weather parameters-->")

def load_model():
    return pickle.load(open("rainfall_model.pkl","rb"))

model=load_model()
temperature=st.number_input("Temperature")
dew_point=st.number_input("Dew Point")
humidity=st.number_input("Humidity")
precipitation=st.number_input("Precipitation")
windspeed=st.number_input("Wind Speed")
winddir=st.number_input("Wind Direction")
sealevelpressure=st.number_input("Sea Level Pressure")
solarradiation=st.number_input("Solar Radiation")
day=st.number_input("Day",min_value=1,max_value=31)
month=st.number_input("Month",min_value=1,max_value=12)
year=st.number_input("Year",min_value=2000,max_value=2030)

if st.button("Predict"):
    input_df=pd.DataFrame([[temperature,dew_point,humidity,precipitation,windspeed,winddir,sealevelpressure,solarradiation,day,month,year]],
        columns=['temp','dew','humidity','precip','windspeed','winddir','sealevelpressure','solarradiation','day','month','year'])

    prediction=model.predict(input_df)[0]

    if prediction==1:
        st.success("It will rain")
    else:
        st.warning("No rain expected")