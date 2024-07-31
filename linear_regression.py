# -- coding: utf-8 --
"""
Created on Sun Jul 28 13:18:01 2024

@author: PMYLS
"""

import streamlit as st
import pandas as pd
import pickle
import base64

# Load the trained model
model_filename = 'C:/Users/PMLS/Downloads/tip prediction system by using linear regression model/Model/linear_regression_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Function to load the image and convert it to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Path to the uploaded image
image_path = 'C:/Users/PMLS/Downloads/tip prediction system by using linear regression model/2.jpg'
base64_image = get_base64_image(image_path)

# Streamlit app configuration
st.set_page_config(page_title="Tip Prediction App", page_icon="💸", layout="centered")

# Add custom CSS for styling
st.markdown(f"""
    <style>
        .header {{
            background: url(data:image/png;base64,{base64_image});
            background-size: cover;
            padding: 20px 0;
            border-radius: 10px;
            text-align: center;
            margin: -10px -10px 10px -10px;
            max-width: 1200px;
            margin-left: auto;
            margin-right: auto;
        }}
        .header:hover {{
            background: url(data:image/png;base64,{base64_image});
            background-size: cover;
            opacity: 0.8;
        }}
        .title {{
            color: #FFFFFF;
            font-size: 48px;
            font-weight: bold;
            padding: 10px 20px;
            background-color: rgba(0, 128, 128, 0.8);
            border-radius: 10px;
            display: inline-block;
        }}
        .subheader {{
            color: #FFFFFF;
            font-size: 16px;
            font-weight: bold;
            padding: 3px 180px;
            background-color: rgba(0, 128, 128, 0.8);
            border-radius: 10px;
            display: inline-block;
            text-align: center;
            margin: -10px -10px 10px -10px;
            max-width: 1200px;
            margin-left: auto;
            margin-right: auto;
        }}
        .stButton>button {{
            background-color: #008080;
            color: white;
            border-radius: 10px;
            font-size: 20px;
            padding: 10px;
            border: none;
            cursor: pointer;
        }}
        .stButton>button:hover {{
            background-color: #FFFFFF;
            color:#008080;
            border: 2px solid #008080;
        }}
        .stNumberInput>div>div>input {{
            background-color: #FFFFFF;
            color: #333;
            border: 5px solid #008080;
            border-radius: 20px;
            font-size: 30px;
            padding: 10px;
        }}
        .footer {{
            color: #2c3e50;
            text-align: center;
            margin-top: 50px;
        }}
        .footer:hover {{
            color: #FFFFFF;
            font-size: 24px;
            font-weight: bold;
            padding: 3px 180px;
            background-color: rgba(0, 128, 128, 0.8);
            border-radius: 10px;
            display: inline-block;
            text-align: center;
            margin-top: 50px;
        }}
    </style>
""", unsafe_allow_html=True)
# App header
st.markdown('<div class="header"><h1 class="title">Tip Prediction App</h1></div>', unsafe_allow_html=True)
st.markdown('<h2 class="subheader">Predict The Tip Amount Based On The Total Bill</h2>', unsafe_allow_html=True)

# Split the page into two columns
col1, col2 = st.columns(2)

with col1:
    # Description
    st.write("""
    ### How to use:
    1. Enter the total bill amount in the input box below.
    2. Click the Predict button to see the estimated tip amount.
    """)

    # Input from user
    total_bill = st.number_input(
        'Enter the total bill amount:',
        min_value=0.0,
        value=0.0,
        step=0.01,
        format="%.2f"
    )

    # Prediction
    if st.button('Predict'):
        input_data = {'total_bill': [total_bill]}
        input_df = pd.DataFrame(input_data)
        prediction = model.predict(input_df)
        st.write(f'### The predicted tip for a total bill of ${total_bill:.2f} is: ${prediction[0]:.2f}')

with col2:
    st.image('C:/Users/PMLS/Downloads/tip prediction system by using linear regression model/3.jpg', caption='', use_column_width=True)

# Footer
st.markdown('<div class="footer">Developed by Talal Hassan Khan</div>', unsafe_allow_html=True)