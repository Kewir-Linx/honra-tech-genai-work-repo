import streamlit as st

st.set_page_config(page_title="Hint: Sidebar Navigation", page_icon="🧭")

st.title("Hint: Page Navigation using st.sidebar.radio")

st.write("You can create multi-page navigation by placing a `radio()` button in the sidebar and checking its value using `if/elif` statements.")

st.subheader("Example Code:")
st.code("""
page = st.sidebar.radio("Navigation", ["Home", "Playground", "About"])

if page == "Home":
    st.header("Welcome Home!")
elif page == "Playground":
    st.header("Interactive Playground")
elif page == "About":
    st.header("About This App")
""", language="python")

st.subheader("Rendered Output:")

page = st.sidebar.radio("Navigate Pages", ["Home Dashboard", "AI Playground", "Documentation"])

if page == "Home Dashboard":
    st.header("Home Dashboard")
    st.write("Welcome to the home page view!")

elif page == "AI Playground":
    st.header("AI Playground")
    st.write("Welcome to the interactive playground page!")

elif page == "Documentation":
    st.header("Documentation")
    st.write("Welcome to the app documentation page!")
