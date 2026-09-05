import streamlit as st

st.set_page_config(page_title="Hint: Forms", page_icon="📋")

st.title("Hint: Streamlit Forms (st.form)")

st.write(
    "A form (`st.form`) groups multiple input widgets together. "
    "Unlike standard Streamlit widgets that rerun the script on every keypress, "
    "inputs inside a form only submit when the user clicks the `st.form_submit_button`."
)

st.subheader("Example Code:")
st.code("""
with st.form(key="user_info_form"):
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")
    submitted = st.form_submit_button("Submit Form")

if submitted:
    st.success(f"Form submitted! Welcome, {name} ({email})")
""", language="python")

st.subheader("Rendered Output:")

with st.form(key="demo_form"):
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")
    submitted = st.form_submit_button("Submit Form")

if submitted:
    if name and email:
        st.success(f"Form submitted! Welcome, {name} ({email})")
    else:
        st.warning("Please fill in both fields before submitting.")
