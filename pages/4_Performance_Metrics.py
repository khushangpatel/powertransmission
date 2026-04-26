import streamlit as st
import matplotlib.pyplot as plt
from data_loader import load_data
from performance_engine import calculate_variance

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first.")
    st.stop()

st.title("📊 Performance Metrics Dashboard")

df = load_data()

if df.empty:
    st.error("Dataset not found.")
    st.stop()

df = calculate_variance(df)

df["Cost_Variance_Cr"] = df["Cost_Variance"] / 1e7

st.subheader("📁 Project Performance Data")

st.dataframe(
    df[[
        "Project_ID",
        "Cost_Variance_Cr",
        "Schedule_Variance"
    ]].rename(columns={
        "Cost_Variance_Cr": "Cost Variance (₹ Cr)",
        "Schedule_Variance": "Schedule Variance (Months)"
    }),
    use_container_width=True
)

st.subheader("💰 Cost Variance (Top 20 Projects)")

fig1, ax1 = plt.subplots()
ax1.bar(df["Project_ID"].head(20), df["Cost_Variance_Cr"].head(20))
ax1.set_xlabel("Project ID")
ax1.set_ylabel("Cost Variance (₹ Crores)")
ax1.set_title("Cost Variance (Actual - Estimated)")
plt.xticks(rotation=45)

st.pyplot(fig1)

st.subheader("⏱ Schedule Variance (Top 20 Projects)")

fig2, ax2 = plt.subplots()
ax2.bar(df["Project_ID"].head(20), df["Schedule_Variance"].head(20))
ax2.set_xlabel("Project ID")
ax2.set_ylabel("Schedule Variance (Months)")
ax2.set_title("Schedule Variance (Actual - Planned)")
plt.xticks(rotation=45)

st.pyplot(fig2)

st.subheader("📈 Cost Variance Distribution")

fig3, ax3 = plt.subplots()
ax3.hist(df["Cost_Variance_Cr"], bins=20)
ax3.set_xlabel("Cost Variance (₹ Crores)")
ax3.set_ylabel("Frequency")
ax3.set_title("Distribution of Cost Variance")

st.pyplot(fig3)

st.subheader("📈 Schedule Variance Distribution")

fig4, ax4 = plt.subplots()
ax4.hist(df["Schedule_Variance"], bins=20)
ax4.set_xlabel("Schedule Variance (Months)")
ax4.set_ylabel("Frequency")
ax4.set_title("Distribution of Schedule Variance")

st.pyplot(fig4)

st.subheader("🔗 Cost vs Schedule Variance")

fig5, ax5 = plt.subplots()
ax5.scatter(df["Cost_Variance_Cr"], df["Schedule_Variance"])
ax5.set_xlabel("Cost Variance (₹ Crores)")
ax5.set_ylabel("Schedule Variance (Months)")
ax5.set_title("Cost vs Schedule Variance Relationship")

st.pyplot(fig5)