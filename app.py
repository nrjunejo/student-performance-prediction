import streamlit as st
import numpy as np
import joblib
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Load the pre-trained student performance prediction model
model = joblib.load('best_student_performance_model.pkl')

# Streamlit app title
st.title('Student Performance Prediction')

# --- User Input Section ---
# Collect relevant features from the user via sliders and selectbox
study_hours = st.slider(
    'Study Hours per Day',
    min_value=0.0, max_value=24.0, value=2.0,
    help="Average number of hours spent studying each day"
)
attendance = st.slider(
    'Attendance Percentage',
    min_value=0.0, max_value=100.0, value=80.0,
    help="Percentage of classes attended"
)
mental_health = st.slider(
    'Mental Health Score (1-10)',
    min_value=1, max_value=10, value=5,
    help="Self-assessed mental health score"
)
sleep_hours = st.slider(
    'Sleep Hours per Night',
    min_value=0.0, max_value=12.0, value=7.0,
    help="Average hours of sleep per night"
)
part_time_job = st.selectbox(
    'Part-time Job',
    ['Yes', 'No'],
    help="Does the student have a part-time job?"
)
# Convert categorical input to numerical
part_time_job = 1 if part_time_job == 'Yes' else 0

# --- Prediction Section ---
if st.button('Predict Performance'):
    # Prepare input data for the model
    input_data = np.array([[study_hours, attendance, mental_health, sleep_hours, part_time_job]])
    # Make prediction
    prediction = model.predict(input_data)[0]
    # Ensure prediction is within 0-100 range
    prediction = np.clip(prediction, 0, 100)
    st.write(f'Predicted Performance Score: {prediction:.2f}')

    # --- Feedback Section ---
    # Provide feedback based on predicted score
    if prediction >= 90:
        st.success('Outstanding Performance')
        st.info(
            'Predicted in the top 10% (90-100). Exceptional achievement! '
            'Maintain your effective study habits and well-being.'
        )
    elif prediction >= 80:
        st.success('Excellent Performance')
        st.info(
            'Predicted score: 80-89. This is a distinction or A grade. '
            'Keep up the strong work and aim for consistency.'
        )
    elif prediction >= 70:
        st.info('Good Performance')
        st.info(
            'Predicted score: 70-79. Above average (B grade). '
            'With focused effort, you can reach even higher.'
        )
    elif prediction >= 60:
        st.warning('Satisfactory Performance')
        st.info(
            'Predicted score: 60-69. Average (C grade). '
            'Consider improving study habits and addressing weaker areas.'
        )
    elif prediction >= 50:
        st.warning('Needs Improvement')
        st.info(
            'Predicted score: 50-59. Below average (D grade). '
            'Seek academic support and review your study routines.'
        )
    elif prediction >= 40:
        st.error('At Risk')
        st.info(
            'Predicted score: 40-49. Marginal or failing grade. '
            'Immediate intervention and support are recommended.'
        )
    else:
        st.error('Critical Risk')
        st.info(
            'Predicted score: below 40. High risk of academic failure. '
            'Seek guidance from teachers, counselors, and support systems.'
        )