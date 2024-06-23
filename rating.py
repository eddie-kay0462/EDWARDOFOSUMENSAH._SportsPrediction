import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

# Load the trained model
@st.cache_resource
def load_model():
    with open("C:/Users/Edward Ofosu Mensah/Downloads/regression1.pkl", 'rb') as file:
        return pickle.load(file)

regressor = load_model()
print(regressor)

def main():
    # Set up the Streamlit app
    st.title('FIFA Player Rating Predictor')
    html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Player Rating App</h2></div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write("""
    This app predicts the overall rating of a FIFA player based on their attributes.
    Please input the player's attributes below:
    """)

    # Create input fields for each feature
    movement_reactions = st.number_input('Movement Reactions', 0, 100, 50)
    mentality_composure = st.number_input('Mentality Composure', 0, 100, 50)
    passing = st.number_input('Passing', 0, 100, 50)
    cm = st.number_input('CM', 0, 300, 100)
    lcm = st.number_input('LCM', 0, 300, 100)
    rcm = st.number_input('RCM', 0, 300, 100)
    potential = st.number_input('Potential', 0, 100, 50)
    rm = st.number_input('RM', 0, 300, 100)
    lm = st.number_input('LM', 0, 300, 100)
    ram = st.number_input('RAM', 0, 300, 100)
    cam = st.number_input('CAM', 0, 300, 100)
    lam = st.number_input('LAM', 0, 300, 100)
    dribbling = st.number_input('Dribbling', 0, 100, 50)
    lf = st.number_input('LF', 0, 300, 100)
    cf = st.number_input('CF', 0, 300, 100)

    # Create a dataframe from the input
    input_data = pd.DataFrame({
        'movement_reactions': [movement_reactions],
        'mentality_composure': [mentality_composure],
        'passing': [passing],
        'cm': [cm],
        'lcm': [lcm],
        'rcm': [rcm],
        'potential': [potential],
        'rm': [rm],
        'lm': [lm],
        'ram': [ram],
        'cam': [cam],
        'lam': [lam],
        'dribbling': [dribbling],
        'lf': [lf],
        'cf': [cf]
    })
    
    # Make prediction when the user clicks the button
    if st.button('Predict Rating'):
        # Make prediction using the loaded model
        prediction = regressor.predict(input_data)[0]
        st.success(f'The predicted overall rating is: {prediction:.2f}')

if __name__ == '__main__':
    main()
