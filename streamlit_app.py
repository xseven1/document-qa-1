import streamlit as st

st.set_page_config(
    page_title="My First Multi-Page Streamlit Application",
    page_icon=":material/edit:",
)

# Title in the sidebar
st.sidebar.title("💥 Multi-Page Navigation")

lab1 = st.Page("lab1.py", title="LAB 1", icon=":material/arrow_outward:")
lab2 = st.Page("lab2.py", title="LAB 2", icon=":material/arrow_outward:")

pg = st.navigation([lab1, lab2])
pg.run()
