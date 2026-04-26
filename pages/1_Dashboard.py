import streamlit as st
import matplotlib.pyplot as plt
from data_loader import load_data

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first.")
    st.stop()

st.title("📊 Project Dashboard")

df = load_data()

st.subheader("📁 All Projects Data")
st.dataframe(df, use_container_width=True)

st.subheader("🌍 Projects by Terrain")

terrain_counts = df["Terrain"].value_counts()

fig1, ax1 = plt.subplots()
ax1.bar(terrain_counts.index, terrain_counts.values)
ax1.set_xlabel("Terrain")
ax1.set_ylabel("Number of Projects")
ax1.set_title("Projects by Terrain")

st.pyplot(fig1)

st.subheader("⛅ Projects by Weather Risk")

weather_counts = df["Weather_Risk"].value_counts()

fig2, ax2 = plt.subplots()
ax2.bar(weather_counts.index, weather_counts.values)
ax2.set_xlabel("Weather Risk")
ax2.set_ylabel("Number of Projects")
ax2.set_title("Weather Risk Distribution")

st.pyplot(fig2)


st.subheader("💰 Estimated vs Actual Cost")

fig3, ax3 = plt.subplots()
ax3.scatter(df["Estimated_Cost"], df["Actual_Cost"])
ax3.set_xlabel("Estimated Cost")
ax3.set_ylabel("Actual Cost")
ax3.set_title("Estimated vs Actual Cost")

st.pyplot(fig3)

st.subheader("⏱ Planned vs Actual Duration")

fig4, ax4 = plt.subplots()
ax4.scatter(df["Planned_Duration"], df["Actual_Duration"])
ax4.set_xlabel("Planned Duration")
ax4.set_ylabel("Actual Duration")
ax4.set_title("Planned vs Actual Duration")

st.pyplot(fig4)

st.subheader("⚡ Voltage Distribution")

fig5, ax5 = plt.subplots()
ax5.hist(df["Voltage_kV"], bins=10)
ax5.set_xlabel("Voltage (kV)")
ax5.set_ylabel("Frequency")
ax5.set_title("Voltage Distribution")

st.pyplot(fig5)
