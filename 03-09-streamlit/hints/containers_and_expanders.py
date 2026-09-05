import streamlit as st

st.set_page_config(page_title="Hint: Containers & Expanders", page_icon="📦")

st.title("Hint: Containers (st.container) & Expanders (st.expander)")

st.write("`st.container` groups visual elements together (optionally with a border), while `st.expander` creates collapsable content boxes.")

st.subheader("Example Code:")
st.code("""
# Bordered Container
with st.container(border=True):
    st.markdown("#### Bordered Box")
    st.write("Everything inside this container is visually grouped with a card border.")

# Collapsable Expander
with st.expander("Click to view Advanced Settings"):
    st.checkbox("Enable Debug Mode")
    st.number_input("Max Output Tokens", min_value=50, max_value=2000, value=250)
""", language="python")

st.subheader("Rendered Output:")

with st.container(border=True):
    st.markdown("#### Card Container")
    st.write("This content is grouped inside a clean, bordered box.")
    st.button("Click Me Inside Container")

st.write("") # Spacing

with st.expander("Click to Expand Details"):
    st.write("This hidden details section keeps the main UI tidy.")
    st.slider("Select value", 1, 10, 5)
