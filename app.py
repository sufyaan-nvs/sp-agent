import streamlit as st
import streamlit.components.v1 as components

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Channel Strategy SP Agent",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------
st.markdown("""
<style>

/* Hide Streamlit UI */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.block-container {
    padding-top: 1rem;
    padding-bottom: 0rem;
    padding-left: 2rem;
    padding-right: 2rem;
    max-width: 100%;
}

.stApp {
    background: linear-gradient(
        135deg,
        #f4f7fb 0%,
        #eef5ff 50%,
        #f8fafc 100%
    );
}

/* Header Card */
.agent-header {
    background: white;
    border-radius: 22px;
    padding: 20px 28px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    border: 1px solid #e5e7eb;
    margin-bottom: 18px;
}

.agent-title {
    font-size: 32px;
    font-weight: 700;
    color: #0f172a;
    line-height: 1.2;
}

.agent-subtitle {
    color: #64748b;
    font-size: 15px;
    margin-top: 6px;
}

.status-pill {
    display: inline-block;
    margin-top: 12px;
    background: #dcfce7;
    color: #166534;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 600;
}

/* Chat Frame */
.chat-frame {
    background: white;
    border-radius: 24px;
    overflow: hidden;
    border: 1px solid #e5e7eb;
    box-shadow: 0 15px 40px rgba(0,0,0,0.08);
}

/* Footer */
.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 12px;
    margin-top: 12px;
    margin-bottom: 12px;
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
        AI-powered Specialty Pharmacy & HUB Analytics Assistant
    </div>

    <div class="status-pill">
        Online
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# COPILOT STUDIO AGENT
# --------------------------------------------------
components.html(
    """
    <iframe
        src="https://copilotstudio.microsoft.com/environments/a32fc343-9406-e5c7-8c34-8f2bf7608657/bots/cr075_untitledagent_fRHMcV/webchat?__version__=2&enableFileAttachment=false&cliAgent=true"
        width="100%"
        height="100%"
        frameborder="0"
        style="
            border:none;
           ---------------
st.markdown("""
<div class="footer">
    Powered by Microsoft Copilot Studio | Specialty Pharmacy Analytics
</div>
""", unsafe_allow_html=True)
