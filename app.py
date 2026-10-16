
import streamlit as st

st.set_page_config(
    page_title="Smart City Cyber Risk",
    page_icon="🛡️",
    layout="wide"
)


st.markdown("""
<div style="
    background: linear-gradient(120deg, #0b1728, #173b60);
    padding: 28px;
    border-radius: 16px;
    border-left: 5px solid #38bdf8;
">
    <h1 style="color: white; margin: 0;">
        🛡️ SMART CITY SECURITY CENTER
    </h1>
    <p style="color: #7dd3fc; font-size: 18px;">
        AI-Based Cyber Risk Assessment & Investment Planning
    </p>
</div>
""", unsafe_allow_html=True)

st.warning(
    "Educational prototype using sample scoring rules, "
    "not a validated AI prediction model."
)

st.sidebar.header("Asset Details")

asset = st.sidebar.selectbox(
    "Select City Asset",
    [
        "Water Monitoring System",
        "Traffic Control System",
        "Smart Street Lights",
        "Public Wi-Fi Network"
    ]
)

vulnerabilities = st.sidebar.slider(
    "Known Vulnerabilities", 0, 50, 5
)
incidents = st.sidebar.slider(
    "Recent Security Incidents", 0, 20, 2
)
traffic = st.sidebar.slider(
    "Suspicious Network Traffic (%)", 0, 100, 30
)

score = min(
    100,
    vulnerabilities + incidents * 3 + traffic * 0.5
)

if score < 35:
    level = "Low"
elif score < 65:
    level = "Medium"
else:
    level = "High"

col1, col2, col3 = st.columns(3)

col1.metric("Selected Asset", asset)
col2.metric("Illustrative Risk Score", f"{score:.1f}/100")
col3.metric("Risk Category", level)

st.progress(int(score))

st.subheader("Security Recommendations")

if level == "High":
    st.error("Review vulnerabilities and investigate incidents urgently.")
elif level == "Medium":
    st.warning("Patch vulnerabilities and monitor network traffic.")
else:
    st.success("Continue routine security monitoring.")

st.subheader("Security Investment Planner")

budget = st.number_input(
    "Available Budget (₹)",
    min_value=1000,
    max_value=1000000,
    value=50000,
    step=1000
)

measures = {
    "Vulnerability Patching": 15000,
    "Network Monitoring": 20000,
    "IoT Device Protection": 25000,
    "Security Awareness Training": 10000
}

selected = st.multiselect(
    "Select Security Measures",
    list(measures.keys()),
    default=["Vulnerability Patching", "Network Monitoring"]
)

cost = sum(measures[item] for item in selected)

st.write(f"Estimated Cost: ₹{cost:,}")
st.write(f"Remaining Budget: ₹{budget - cost:,}")

if cost > budget:
    st.error("Selected measures exceed the available budget.")
else:
    st.success("Selected measures fit within the budget.")

st.caption(
    "All scores and costs are illustrative. "
    "Real-world use requires testing with validated datasets."
)




