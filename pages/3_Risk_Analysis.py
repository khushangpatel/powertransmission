import streamlit as st
from risk_engine import calculate_risk
from recommendation_engine import recommend_project

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first.")
    st.stop()

st.title("Risk Analysis")

weather = st.selectbox("Weather Risk", ["Low", "Medium", "High"])
terrain = st.selectbox("Terrain", ["Plain", "Hilly", "Forest", "Desert"])

experience = st.slider("Contractor Experience (years)", 1, 20, 10)
labor = st.slider("Labor Availability (%)", 50, 100, 80)

if st.button("Analyze Risk"):

    risk_score = calculate_risk(weather, terrain, experience, labor)

    st.write(f"Risk Score: {risk_score}/100")

    if risk_score > 60:
        st.error("High Risk")
    elif risk_score > 30:
        st.warning("Moderate Risk")
    else:
        st.success("Low Risk")

    decision = recommend_project(risk_score, 50000000)
    st.subheader(f"Decision: {decision}")