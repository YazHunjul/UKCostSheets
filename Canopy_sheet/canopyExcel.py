from openpyxl import load_workbook
import streamlit as st
from io import BytesIO

# Function to create the canopy cost sheet
def create_canopy_sheet(canopy_info, gen_info):
    file_path = ('/Users/yazan/Desktop/HALTON WORK/Halton Cost Sheets/Projects/CanopyCostSheet/Cost Sheet R18.5 Sep '
                 '2024 (7).xlsx')

    # Load the existing workbook
    workbook = load_workbook('Resources/Cost Sheet R18.5 Sep 2024 (7).xlsx')

    # Select the worksheet by name (you can also use workbook.active to get the first sheet)
    sheet = workbook['CANOPY']  # Replace 'CANOPY' with your actual sheet name

    # Example of adding canopy data (for example, entering model data)
    # Base Costs
    config = 14
    lights = 15
    fire_suppression = 16
    spec1 = 17
    spec2 = 18
    cladding = 19
    infill = 20
    crating = 21
    filter = 22
    psu = 23
    # Model
    model = 14
    crating = 21
    item = 12
    itemNum = 1
    sheet['C3'] = gen_info['jobNum'].title()
    sheet['C5'] = gen_info['customer'].title()
    sheet['C7'] = gen_info['manager_inits'].title()
    sheet['G3'] = gen_info['projectName'].title()
    sheet['G5'] = gen_info['location'].title()
    sheet['G7'] = gen_info['date']

    for key in canopy_info:
        sheet[f'C{item}'] = itemNum
        if canopy_info[key]['model'] in ['KVI', 'KVX','KVF']:
            sheet[f'D{model}'] = canopy_info[key]['model']
            sheet[f'C{config}'] = canopy_info[key]['configuration']
            sheet[f'C{lights}'] = canopy_info[key]['lights']
            sheet[f'C{spec1}'] = canopy_info[key]['special_works']
            sheet[f'C{cladding}'] = canopy_info[key]['cladding']
            sheet[f'C{infill}'] = canopy_info[key]['infill_pannel']
            sheet[f'C{filter}'] = canopy_info[key]['grease_filters']
            sheet[f'C{crating}'] = canopy_info[key]['crating']
            sheet[f'C{psu}'] = canopy_info[key]['junction_box']
            sheet[f'E{model}'] = canopy_info[key]['width']
            sheet[f'F{model}'] = canopy_info[key]['length']
            sheet[f'G{model}'] = canopy_info[key]['height']
            sheet[f'H{model}'] = canopy_info[key]['sections']
            sheet[f'I{model}'] = canopy_info[key]['flowrate']
        config+=17
        lights+=17
        fire_suppression+=17
        spec1+=17
        spec2+=17
        cladding+=17
        infill+=17
        crating+=17
        filter+=17
        psu+=17
        model+=17
        crating+=17
        item+=17
        itemNum+=1
        print(crating)
    st.write("Canopy Saved ✅")


    # Save the workbook to a BytesIO object (in memory)
    buffer = BytesIO()
    workbook.save(buffer)
    buffer.seek(0)  # Move the buffer's cursor to the beginning

    return buffer

# Function to download the canopy cost sheet
def download(info, geninfo):
    # Create the Excel buffer
    if st.button('Save Canopy Sheet'):
        excel_buffer = create_canopy_sheet(info, geninfo)

    # Provide the download button in Streamlit
        st.download_button(
            label="Download Canopy Cost Sheet",
            data=excel_buffer,  # This is the in-memory Excel file
            file_name="canopy_cost_sheet.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
