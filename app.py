import streamlit as st
from modules.disaster_info import get_disaster_names, get_disaster_info
# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="Devbhoomi Suraksha",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.hero {
    padding: 35px;
    border-radius: 18px;
    background: linear-gradient(135deg, #17324d, #245b7a);
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 5px;
}

.hero p {
    font-size: 18px;
}

.card {
    padding: 22px;
    border-radius: 15px;
    background-color: white;
    border: 1px solid #e6e9ed;
    margin-bottom: 15px;
}

.warning {
    padding: 18px;
    border-radius: 12px;
    background-color: #fff3cd;
    border-left: 6px solid #ffb300;
}

.emergency {
    padding: 20px;
    border-radius: 15px;
    background-color: #ffe5e5;
    border-left: 6px solid #d32f2f;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🚨 Devbhoomi Suraksha")

st.sidebar.markdown(
    "### Disaster Safety Assistant\n"
    "Uttarakhand-focused information and emergency guidance."
)

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Dashboard",
        "⚠️ Disaster Information",
        "🛡️ Safety Guidelines",
        "🤖 AI Assistant",
        "📍 Location & Risk",
        "📞 Emergency Contacts"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Devbhoomi Suraksha • 2026")

# -----------------------------
# DASHBOARD
# -----------------------------
if page == "🏠 Dashboard":

    st.markdown("""
    <div class="hero">

    <h1>🚨 Devbhoomi Suraksha</h1>

    <p>
    AI-powered disaster information and safety assistant
    designed for Uttarakhand.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.subheader("Stay Informed. Stay Prepared. Stay Safe.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">

        ### 🌧️ Disaster Information

        Learn about floods, landslides, earthquakes,
        cloudbursts and other hazards.

        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">

        ### 🛡️ Safety Guidance

        Get practical steps to take before,
        during and after a disaster.

        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">

        ### 🤖 AI Assistant

        Ask questions about disaster preparedness
        and emergency safety.

        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("⚠️ Emergency Awareness")

    st.markdown("""
    <div class="warning">

    <b>Important:</b> During an actual emergency, always
    follow instructions from official authorities and
    emergency services.

    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# DISASTER INFORMATION
# -----------------------------
elif page == "⚠️ Disaster Information":

    st.title("⚠️ Disaster Information")

  disaster = st.selectbox(
    "Select a disaster",
    get_disaster_names()
)

info = get_disaster_info(disaster)

if info:
    st.subheader(f"⚠️ {info['disaster']}")

    st.write(info["description"])

    st.markdown("### 🚨 Warning Signs")
    st.write(info["warning_signs"])

    st.markdown("### 🟢 Before")
    st.write(info["before"])

    st.markdown("### 🔴 During")
    st.write(info["during"])

    st.markdown("### 🔵 After")
    st.write(info["after"])

    st.info(f"Risk Level: {info['risk_level']}")  
    st.info(
        f"Information and safety recommendations for: **{disaster}**"
    )

    st.subheader("What is it?")

    st.write(
        "Detailed information about this disaster will be "
        "provided here using our verified disaster-safety dataset."
    )

    st.subheader("⚠️ Warning Signs")

    st.write(
        "Warning signs and important indicators will be "
        "displayed here."
    )

    st.subheader("🛡️ What should you do?")

    st.write(
        "Step-by-step emergency guidance will be displayed here."
    )

# -----------------------------
# SAFETY GUIDELINES
# -----------------------------
elif page == "🛡️ Safety Guidelines":

    st.title("🛡️ Safety Guidelines")

    disaster = st.selectbox(
        "Choose a situation",
        [
            "Earthquake",
            "Flood",
            "Landslide",
            "Cloudburst",
            "Forest Fire"
        ]
    )

    st.subheader(f"Safety Guide: {disaster}")

    st.markdown("""
    **Before**
    - Keep an emergency kit ready.
    - Know your nearest safe location.
    - Save important emergency numbers.

    **During**
    - Stay calm.
    - Follow official instructions.
    - Move away from dangerous areas.

    **After**
    - Check for injuries.
    - Avoid damaged structures.
    - Wait for official clearance before returning.
    """)

# -----------------------------
# AI ASSISTANT
# -----------------------------
elif page == "🤖 AI Assistant":

    st.title("🤖 Devbhoomi AI Safety Assistant")

    st.write(
        "Ask a question about disaster preparedness or safety."
    )

    question = st.text_area(
        "Your question",
        placeholder="Example: What should I do during a landslide?"
    )

    if st.button("Get Safety Guidance"):

        if question.strip():

            st.success(
                "Your question has been received. "
                "The AI safety assistant will provide guidance here."
            )

        else:

            st.warning("Please enter a question first.")

# -----------------------------
# LOCATION & RISK
# -----------------------------
elif page == "📍 Location & Risk":

    st.title("📍 Location & Risk Assessment")

    location = st.text_input(
        "Enter your location",
        placeholder="Example: Haldwani"
    )

    if st.button("Check Risk"):

        if location.strip():

            st.info(
                f"Risk assessment for **{location}** "
                "will be generated using our disaster-risk data."
            )

        else:

            st.warning("Please enter your location.")

# -----------------------------
# EMERGENCY CONTACTS
# -----------------------------
elif page == "📞 Emergency Contacts":

    st.title("📞 Emergency Contacts")

    st.markdown("""
    <div class="emergency">

    ### 🚨 Emergency

    In a real emergency, contact the appropriate
    official emergency service immediately.

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Emergency", "112")
        st.metric("Fire", "101")

    with col2:
        st.metric("Police", "100")
        st.metric("Ambulance", "108")