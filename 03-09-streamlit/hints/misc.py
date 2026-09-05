import streamlit as st
import time

st.set_page_config(page_title="Hint: Utilities & Status Messages", page_icon="🎈")

st.title("Hint: Utility Functions (st.balloons, st.success, st.error, st.progress)")

st.write("Streamlit provides built-in status indicators and visual utilities to provide user feedback.")

st.subheader("Example Code:")
st.code("""
# Status messages
st.success("Operation completed successfully!")
st.error("An error occurred while processing.")

# Progress bar
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress_bar.progress(i + 1)

# Celebration balloons animation
st.balloons()
""", language="python")

st.subheader("Rendered Output Demo:")

if st.button("Run Utility Demo"):
    st.write("Simulating a background task with progress bar...")
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)

    st.success("Task completed successfully!")
    st.balloons()

st.write("---")
st.subheader("Static Status Message Examples:")
st.success("This is an example of st.success()")
st.error("This is an example of st.error()")
