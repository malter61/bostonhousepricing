import pandas as pd
import numpy as np
import pickle
import streamlit as st

from PIL import Image

regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar=pickle.load(open('scaling.pkl', 'rb'))


def predict_price(CRIM,ZN,INDUS,CHAS,NDX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT):
    prediction=regmodel.predict([[CRIM,ZN,INDUS,CHAS,NDX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]])
    print(prediction)
    return prediction

def main():
    st.title("Boston Housing Predictions")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit House Price Predictor </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    CRIM = st.text_input("CRIM","Type here")
    ZN = st.text_input("ZN","Type here")
    INDUS = st.text_input("INDUS","Type here")
    CHAS = st.text_input("CHAS","Type here")
    NOX = st.text_input("NOX","Type here")
    RM = st.text_input("RM","Type here")
    AGE = st.text_input("AGE","Type here")
    DIS = st.text_input("DIS","Type here")
    RAD = st.text_input("RAD","Type here")
    TAX = st.text_input("TAX","Type here")
    PTRATIO = st.text_input("PTRATIO","Type here")
    B = st.text_input("B","Type here")
    LSTAT = st.text_input("LSTAT","Type here")
    result=""
    if st.button("Predict"):
        result=predict_price(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
    st.success("The predicted price is " + str(result))
    if st.button("About"):
        st.text('Lets learn')
        st.text('Built with streamlit')


if __name__ == '__main__':
    main()