import streamlit as st

st.set_page_config(page_title="Hint: Markdown", page_icon="📝")

st.title("Hint: Markdown Formatting (st.markdown)")

st.write("`st.markdown()` allows you to render formatted text, headers, lists, code snippets, and dividers using standard Markdown syntax.")

st.subheader("Example Code:")
st.code("""
st.markdown("# Heading 1")
st.markdown("## Heading 2")
st.markdown("**Bold Text** and *Italic Text*")
st.markdown("- Bullet point 1\\n- Bullet point 2")
st.markdown("---") # Horizontal line divider
""", language="python")

st.subheader("Rendered Output:")
st.markdown("# Heading 1")
st.markdown("## Heading 2")
st.markdown("**Bold Text** and *Italic Text*")
st.markdown("- Bullet point 1\n- Bullet point 2")
st.markdown("---")
st.markdown("This is text after a horizontal line divider.")
