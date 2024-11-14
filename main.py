import streamlit as st

navigation = st.sidebar.selectbox('Navigation', ["Project Cost Sheet"])

if navigation == "Project Cost Sheet":
	from cost_sheets import cost_sheets
	cost_sheets()
