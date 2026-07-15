
import streamlit as st
import pickle
import json
import numpy as np
import pandas as pd

# Load model
with open('kanpur_house_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('localities.json', 'r') as f:
    localities = json.load(f)

with open('locality_mean.json', 'r') as f:
    locality_mean = json.load(f)

# Page config
st.set_page_config(
    page_title="Kanpur House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# Header
st.title("🏠 Kanpur House Price Predictor")
st.markdown("### Apne ghar ki estimated price janiye!")
st.markdown("---")

# Input fields
col1, col2 = st.columns(2)

with col1:
    bhk = st.selectbox("BHK", [1, 2, 3, 4, 5])
    
    # Kanpur ke real estate ke hisaab se sensible area range
    area_ranges = {
        1: (400, 750),
        2: (700, 1250),
        3: (1100, 1900),
        4: (1700, 3000),
        5: (2500, 5000)
    }
    min_area, max_area = area_ranges[bhk]
    default_area = (min_area + max_area) // 2
    
    area_sqft = st.number_input(
        "Area (sqft)", 
        min_value=min_area, 
        max_value=max_area, 
        value=default_area, 
        step=50
    )
with col2:
    locality = st.selectbox("Locality", localities)
    
st.markdown("---")

# Predict button
if st.button("🔮 Price Predict Karo", use_container_width=True):
    
    # Features calculate karo
    locality_enc = locality_mean.get(locality, np.mean(list(locality_mean.values())))
    area_per_bhk = area_sqft / bhk
    price_per_sqft = locality_enc * 100000 / area_sqft
    is_premium = 1 if locality_enc >= 100 else 0
    
    # BHK categories
    bhk_cat_small   = 1 if bhk <= 1 else 0
    bhk_cat_medium  = 1 if bhk == 2 else 0
    bhk_cat_large   = 1 if bhk == 3 else 0
    bhk_cat_luxury  = 1 if bhk >= 4 else 0

    features = np.array([[
    bhk, area_sqft,
    price_per_sqft, locality_enc, area_per_bhk, is_premium,
    bhk_cat_large, bhk_cat_luxury,
    bhk_cat_medium, bhk_cat_small
]])

    prediction = model.predict(features)[0]
    
    # Result display
    st.success(f"### 🏷️ Estimated Price: ₹{prediction:.2f} Lakhs")
    
    if prediction >= 100:
        st.info(f"💰 Yani lagbhag ₹{prediction/100:.2f} Crore")
    
    st.markdown("---")
    
    # Details
    col1, col2, col3 = st.columns(3)
    col1.metric("BHK", bhk)
    col2.metric("Area", f"{area_sqft} sqft")
    col3.metric("Locality", locality)
    
    price_per_sqft_result = (prediction * 100000) / area_sqft
    st.markdown(f"📊 **Price per sqft:** ₹{price_per_sqft_result:.0f}")

st.markdown("---")
st.caption("Made with ❤️ | Kanpur House Price Prediction Project")
