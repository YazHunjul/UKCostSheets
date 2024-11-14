import streamlit as st
import base64


def get_base64_image(image_path):
	with open(image_path, "rb") as image_file:
		return base64.b64encode(image_file.read()).decode()


# Get the base64 string of the image
base64_logo = get_base64_image("Resources/Halton-Logo.png")


def title():
	st.markdown(
		f"""
	   <div style="text-align: center;">
	   <img src="data:image/png;base64,{base64_logo}" alt="Halton Logo" width="400">
	   <h1>Project Cost Sheet</h1>
	   </div>
	   """,
		unsafe_allow_html=True
	)


def genInfo():
	# General Info
	title()
	st.markdown("")
	col1, col2 = st.columns(2)
	with col1:
		jobNum = st.text_input(label='Job Number')
	with col2:
		projectName = st.text_input(label='Project Name')
	with col1:
		customer = st.text_input(label='customer')
	with col2:
		location = st.text_input(label='location')
	with col1:
		manager_inits = st.text_input(label='Sales Manager / Estimator Initials')
	with col2:
		date = st.date_input(label='Date')
	with col1:
		ref = st.text_input("Enter Reference Number (xxxxx/xx/xx)", key='ref')

	selections = st.multiselect("Select Cost Sheets to Report", ["AHU", "Contract", "Canopy"])

	geninfo = {
		'jobNum': jobNum,
		'customer': customer,
		'location': location,
		'manager_inits': manager_inits,
		'date': date,
		'selections': selections,
		'projectName': projectName,
	}
	return geninfo