import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("model/placement_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Campus Placement Predictor",
    page_icon="🎓",
    layout="wide"
)

# Title
st.markdown(
    """
    # 🎓 Campus Placement Predictor

    ### Predict your placement chances using Machine Learning
    """
)
st.write("Enter your details below to predict your placement chances.")

# Sidebar
st.sidebar.title("🎓 Campus Placement Predictor")

st.sidebar.success("Machine Learning Project")

st.sidebar.markdown("---")

st.sidebar.write("Developed by")
st.sidebar.write("D V Shriram")

st.sidebar.markdown("---")

st.sidebar.info(
    "Predict placement chances using a trained Random Forest model."
)

# Input fields
col1, col2 = st.columns(2)

with col1:
    cgpa = st.number_input("CGPA", 0.0, 10.0, 7.5)
    communication = st.slider("Communication Skills", 0.0, 10.0, 5.0)
    resume = st.slider("Resume Score", 0.0, 10.0, 5.0)

with col2:
    coding = st.slider("Coding Score", 0.0, 10.0, 5.0)
    attendance = st.slider("Attendance (%)", 0.0, 100.0, 75.0)

# Predict button
if st.button("Predict Placement"):

    input_data = pd.DataFrame({
        "cgpa":[cgpa],
        "communication_skills":[communication],
        "resume_score":[resume],
        "coding_score":[coding],
        "attendance_placement":[attendance]
    })

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    if prediction == 1:
        st.success("🎉 High Chance of Placement")
    else:
        st.error("❌ Low Chance of Placement")

    st.metric("Placement Probability", f"{max(probability)*100:.2f}%")
    st.progress(int(max(probability) * 100))
    st.subheader("Suggestions")

if cgpa < 7:
    st.warning("📚 Improve your CGPA.")

if coding < 6:
    st.warning("💻 Practice Data Structures & Algorithms.")

if communication < 6:
    st.warning("🗣️ Improve communication skills.")

if resume < 6:
    st.warning("📄 Build a stronger resume.")

if attendance < 75:
    st.warning("🏫 Improve attendance.")
    with st.expander("About this Project"):
     st.write("""
    This project predicts whether a student is likely to be placed based on:

    - CGPA
    - Communication Skills
    - Resume Score
    - Coding Score
    - Attendance

    Machine Learning Model:
    Random Forest Classifier
    """)
     if prediction == 1:
         st.balloons()