from docx import Document
from docxtpl import DocxTemplate
import streamlit as st
from io import BytesIO


# Function to create the document and modify its content
def create_doc(canopy, info):
	# Load the existing Word document template
	doc = DocxTemplate("/Users/yazan/Desktop/HALTON WORK/UK Cost Sheets/Resources/Halton Quotation Feb 2024 (4).docx")

	canopyRow = []

	for k, v in canopy.items():
		i = 1
		num = f"1.0{k}"
		model = v['model']
		length= v['length']
		width = v['width']
		sections = v['sections']
		canopyRow.append({'itemNum' : num, 'model': model, 'length' : length, 'width' : width, 'sections': sections, 'lights' : v['lights']})

	# Prepare content for dynamic replacement
	content = {
		"date": info["date"],
		"client": info["customer"].title(),
		"project": info["projectName"].title(),
		"location": info["location"].title(),
		"halton_ref": "12345 / 12 / 12",
		"canopies" : canopyRow
	}
	print(content)

	# Render the template with the content
	doc.render(content)

	# Save to an in-memory buffer
	buffer = BytesIO()
	doc.save(buffer)
	buffer.seek(0)  # Set the pointer to the beginning of the buffer
	return buffer


# Streamlit function to download the document
def download_button(canopy, info):
	# Create the modified document in memory when the button is clicked
	if st.button('Download Quote'):
		doc_buffer = create_doc(canopy, info)

		# Streamlit download button
		st.download_button(
			label="Download Modified Document",
			data=doc_buffer,
			file_name="modified_file.docx",
			mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
		)
