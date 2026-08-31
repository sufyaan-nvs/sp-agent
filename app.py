import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

components.html(
    """
    <iframe
        src="https://copilotstudio.microsoft.com/environments/a32fc343-9406-e5c7-8c34-8f2bf7608657/bots/cr075_untitledagent_fRHMcV/webchat?__version__=2&enableFileAttachment=false&cliAgent=true"
        width="100%"
        height="900"
        frameborder="0">
    </iframe>
    """,
    height=900,
)
