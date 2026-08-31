import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Channel Strategy SP Agent",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default UI
st.markdown("""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container{
    padding-top:1rem;
    padding-bottom:0rem;
    max-width:100%;
}

.main {
    background: linear-gradient(
        135deg,
        #f8fafc 0%,
        #eef4ff 50%,
        #f8fafc 100%
    );
}

.agent-header {
    background: white;
    border-radius: 20px;
    padding: 18px 24px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
    border: 1px solid #e5e7eb;
    margin-bottom: 15px;
}

.agent-title {
    font-size: 30px;
    font-weight: 700;
    color: #1e3a8a;
    margin-bottom: 4px;
}

.agent-subtitle {
    color: #64748b;
    font-size: 15px;
}

.status-badge {
    display:inline-block;
    background:#dcfce7;
    color:#166534;
    padding:6px 12px;
    border-radius:999px;
    font-size:12px;
    font-weight:600;
    margin-top:10px;
}

.chat-container {
    background:white;
    border-radius:20px;
    overflow:hidden;
    box-shadow:0 10px 40px rgba(0,0,0,0.08);
    border:1px solid #e5e7eb;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="agent-header">
    <div class="agent-title">
        Channel Strategy SP Agent
    </div>
    <div class="agent-subtitle">
        AI-powered Specialty Pharmacy & HUB Analytics Assistant
    </div>
    <div class="status-badge">
        ● Online
    </div>
</div>
""", unsafe_allow_html=True)

# Embedded Copilot Studio Agent
components.html(
    """
    <div class="chat-container">
        <iframe
            src="https://copilotstudio.microsoft.com/environments/a32fc343-9406-e5c7-8c34-8f2bf7608657/bots/cr075_untitledagent_fRHMcV/webchat?__version__=2&enableFileAttachment=false&cliAgent=true"
            width="100%"
            height="900"
            frameborder="0"
            allowfullscreen>
        </iframe>
    </div>
    """,
    height=920,
)
Powered by Microsoft Copilot Studio | Specialty Pharmacy Analytics

</div>
""", unsafe_allow_html=True)
