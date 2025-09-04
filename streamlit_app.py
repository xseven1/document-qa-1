import streamlit as st
st.set_page_config(page_title="My First Multi-Page Streamlit Application", page_icon=":material/edit:")
st.title("💥Multi-Page Navigation")
st.sidebar.header("Lab Navigation")
lab2 = st.Page("lab2.py", title="LAB 2", icon=":material/arrow_outward:")
lab1 = st.Page("lab1.py", title="LAB 1", icon=":material/arrow_outward:")

pg = st.navigation([lab1, lab2])
pg.run()
