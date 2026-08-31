import streamlit as st
import streamlit.components.v1 as components

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Channel Strategy SP Agent",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# STYLING
# --------------------------------------------------
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp {
    background: linear-gradient(
        135deg,
        #f4f7fb 0%,
        #eef5ff 50%,
        #f8fafc 100%
    );
}

.block-container {
    padding-top: 1rem;
    max-width: 100%;
}

.agent-header {
    background: white;
    border-radius: 20px;
    padding: 20px 30px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    border: 1px solid #e5e7eb;
    margin-bottom: 15px;
}

.agent-title {
    font-size: 32px;
    font-weight: 700;
    color: #0f172a;
}

.agent-subtitle {
    color: #64748b;
    font-size: 15px;
    margin-top: 5px;
}

.status {
    display:inline-block;
    margin-top:12px;
    background:#dcfce7;
    color:#166534;
    padding:6px 12px;
    border-radius:999px;
    font-size:12px;
    font-weight:600;
}

.footer {
    text-align:center;
    color:#94a3b8;
    margin-top:10px;
    font-size:12px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("""
<div class="agent-header">
    <div class="agent-title">
        Channel Strategy SP Agent
    </div>

    <div class="agent-subtitle">
        AI-powered Specialty Pharmacy and HUB Analytics Assistant
    </div>

    <div class="status">
        Online
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# OPTIONAL KPI ROW
# --------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Status", "Online")

with col2:
    st.metric("Source", "Power BI")

with col3:
    st.metric("Domain", "SP & HUB")

with col4:
    st.metric("Environment", "Production")

# --------------------------------------------------
# EMBED COPILOT STUDIO
# --------------------------------------------------
components.html(
    """
    <iframe
        src="https://copilotstudio.microsoft.com/environments/a32fc343-9406-e5c7-8c34-8f2bf7608657/bots/cr075_untitledagent_fRHMcV/webchat?__version__=2&enableFileAttachment=false&cliAgent=true"
        width="100%"
        height="900"
        frameborder="0"
        style="border:none;border-radius:20px;background:white;">
    </iframe>
    """,
    height=ter">
    Powered by Microsoft Copilot Studio | Specialty Pharmacy Analytics
</div>
""", unsafe_allow_html=True)
