import streamlit as st

st.set_page_config(page_title="Hint: Tabs", page_icon="🗂️")

st.title("Hint: Tabs (st.tabs)")

st.write("`st.tabs()` splits your page content into clean, clickable tab sections without requiring page reloads.")

st.subheader("Example Code:")
st.code("""
tab1, tab2 = st.tabs(["Overview", "Settings"])

with tab1:
    st.write("This is the main overview tab.")

with tab2:
    st.write("Here are your settings options.")
""", language="python")

st.subheader("Rendered Output:")

tab1, tab2, tab3 = st.tabs(["Overview", "Output", "Settings"])

with tab1:
    st.markdown("### Overview")
    st.write("Welcome to the tab view! Tabs help keep complex interfaces organized.")

with tab2:
    st.markdown("### Output")
    st.success("This section displays generated AI results or analysis.")

with tab3:
    st.markdown("### Settings")
    st.slider("Model Temperature", 0.0, 1.0, 0.7)
