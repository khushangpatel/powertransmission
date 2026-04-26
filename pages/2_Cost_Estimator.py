import streamlit as st
from cost_engine import calculate_cost

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first.")
    st.stop()

st.title("Cost Estimator")

length = st.number_input("Length (km)", 10, 500, 100)
voltage = st.selectbox("Voltage (kV)", [132, 220, 400, 765])
terrain = st.selectbox("Terrain", ["Plain", "Hilly", "Forest", "Desert"])

experience = st.slider("Contractor Experience (years)", 1, 20, 10)
material_index = st.slider("Material Cost Index", 1.0, 1.5, 1.2)
labor = st.slider("Labor Availability (%)", 50, 100, 80)

if st.button("Estimate Cost"):
    cost = calculate_cost(length, voltage, terrain, experience, material_index, labor)
    st.success(f"Estimated Cost: ₹ {cost:,.0f}")