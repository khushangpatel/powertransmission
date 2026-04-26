import streamlit as st
import matplotlib.pyplot as plt
from data_loader import load_data

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first.")
    st.stop()

st.title("Trend Analysis")

df = load_data()

if df.empty:
    st.error("Dataset not found.")
    st.stop()

grouped = df.groupby("Voltage_kV").mean(numeric_only=True)

grouped["Actual_Cost_Cr"] = grouped["Actual_Cost"] / 1e7

st.subheader("Average Cost by Voltage (in Crores)")

fig, ax = plt.subplots()
ax.bar(grouped.index, grouped["Actual_Cost_Cr"])

ax.set_xlabel("Voltage (kV)")
ax.set_ylabel("Cost (₹ Crores)")
ax.set_title("Average Project Cost by Voltage")

st.pyplot(fig)