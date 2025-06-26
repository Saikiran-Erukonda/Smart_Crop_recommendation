import streamlit as st
import joblib
import pandas as pd

# Load your model and preprocessing objects
model = joblib.load('crop_recommender.pkl')
preprocessor = joblib.load('preprocessor.pkl')

# Set page config
st.set_page_config(page_title="Crop Recommendation System", layout="wide")

# Add title and description
st.title("🌱 Smart Crop Recommendation System")
st.markdown("""
This tool recommends the most suitable crops based on soil conditions, climate factors, 
and other agricultural parameters. Adjust the sliders to get recommendations.
""")

# Create input widgets in a sidebar
st.sidebar.header("Input Parameters")

# Example input fields (adjust based on your features)
n = st.sidebar.slider('Nitrogen (N)', 0, 100, 50)
p = st.sidebar.slider('Phosphorus (P)', 0, 100, 30)
k = st.sidebar.slider('Potassium (K)', 0, 100, 20)
temperature = st.sidebar.slider('Temperature (°C)', 0.0, 50.0, 25.0)
humidity = st.sidebar.slider('Humidity (%)', 0.0, 100.0, 60.0)
ph = st.sidebar.slider('pH', 0.0, 14.0, 6.5)
rainfall = st.sidebar.slider('Rainfall (mm)', 0.0, 500.0, 150.0)

# Create a dictionary of inputs
input_data = {
    'N': n,
    'P': p,
    'K': k,
    'temperature': temperature,
    'humidity': humidity,
    'ph': ph,
    'rainfall': rainfall
}

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Add prediction button
if st.sidebar.button('Recommend Crop'):
    # Preprocess inputs
    processed_input = preprocessor.transform(input_df)
    
    # Make prediction
    prediction = model.predict(processed_input)
    probabilities = model.predict_proba(processed_input)
    
    # Display results
    st.success(f"Recommended Crop: **{prediction[0]}**")
    
    # Show probabilities (if classifier)
    st.subheader("Crop Probabilities")
    prob_df = pd.DataFrame({
        'Crop': model.classes_,
        'Probability': probabilities[0]
    }).sort_values('Probability', ascending=False)
    
    st.bar_chart(prob_df.set_index('Crop'))
    
    # Add some visual appeal
    st.balloons()
