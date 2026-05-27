import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model and dataframe
pipe = joblib.load('ML/pipe.joblib')
df = joblib.load('ML/df.joblib')

st.set_page_config(page_title="Laptop Price Predictor")

st.title("💻 Laptop Price Predictor")

# Brand
company = st.selectbox('Brand', df['Company'].unique())

# Laptop type
type_name = st.selectbox('Type', df['TypeName'].unique())

# RAM
ram = st.selectbox('RAM (GB)', [2,4,6,8,12,16,24,32,64])

# Weight
weight = st.number_input('Weight of Laptop (kg)', min_value=0.5)

# Touchscreen
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

# IPS
ips = st.selectbox('IPS Display', ['No', 'Yes'])

# Screen size
screen_size = st.slider('Screen Size (Inches)', 10.0, 18.0, 13.0)

# Resolution
resolution = st.selectbox(
    'Screen Resolution',
    [
        '1920x1080',
        '1366x768',
        '1600x900',
        '3840x2160',
        '3200x1800',
        '2880x1800',
        '2560x1600',
        '2560x1440',
        '2304x1440'
    ]
)

# CPU
cpu = st.selectbox('CPU Brand', df['Cpu brand'].unique())

# HDD
hdd = st.selectbox('HDD Storage (GB)', [0,128,256,512,1024,2048])

# SSD
ssd = st.selectbox('SSD Storage (GB)', [0,8,128,256,512,1024])

# GPU
gpu = st.selectbox('GPU Brand', df['Gpu brand'].unique())

# Operating System
os = st.selectbox('Operating System', df['os'].unique())

# Prediction button
if st.button('Predict Price'):

    # Convert categorical binary values
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    # Calculate PPI
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])

    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    # Final query
    query = pd.DataFrame([{
        'Company': company,
        'TypeName': type_name,
        'Ram': ram,
        'Weight': weight,
        'Touchscreen': touchscreen,
        'Ips': ips,
        'ppi': ppi,
        'Cpu brand': cpu,
        'HDD': hdd,
        'SSD': ssd,
        'Gpu brand': gpu,
        'os': os
    }])

    # Prediction
    prediction = int(np.exp(pipe.predict(query)[0]))
    
    st.subheader(f"💰 Predicted Laptop Price: ₹ {prediction:,}")

