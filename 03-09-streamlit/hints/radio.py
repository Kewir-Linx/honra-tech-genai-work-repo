import streamlit as st

st.set_page_config(page_title="Hint: Radio Buttons", page_icon="🔘")

st.title("Hint: Radio Buttons (st.radio)")

st.write("`st.radio()` displays a set of single-select radio buttons. You can use it in the main page or in `st.sidebar.radio()` for navigation.")

st.subheader("Example Code:")
st.code("""
choice = st.radio(
    "Select an option:",
    ["Option A", "Option B", "Option C"],
    horizontal=True # Optional: lays buttons out side-by-side
)

st.write(f"You selected: **{choice}**")
""", language="python")

st.subheader("Rendered Output:")

choice = st.radio(
    "Select your favorite AI topic:",
    ["Natural Language Processing", "Computer Vision", "Reinforcement Learning"],
    horizontal=True
)

st.info(f"Selected Topic: **{choice}**")
