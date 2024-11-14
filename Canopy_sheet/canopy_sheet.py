import streamlit as st
from Canopy_sheet import canopyExcel as CE
from Canopy_sheet import canopyQuote as CQ


def canopyMain(info):
	st.markdown("<hr style='border:1px solid gray'>", unsafe_allow_html=True)
	st.markdown(
		f"""
		    <div style="text-align: center;">
		    <h2>Canopy Cost Sheet</h2>
		    </div>
		    """,
		unsafe_allow_html=True
	)
	# Get num of canopies and canopy types
	canopies = {}
	numItems = st.number_input('Enter Number of Canopies', min_value=0, max_value=100)
	st.markdown("<hr style='border:1px solid gray'>", unsafe_allow_html=True)
	for i in range(numItems):
		#Create a new canopy selection
		canopy = get_canopies(i + 1)
		#Store the canopy in the dictionary
		canopies[i + 1] = canopy
	print(canopies)
	CE.download(canopies, info)
	return canopies


def get_canopies(num):
	canopies = {}
	st.markdown(f"<h3>Canopy {num}</h3>", unsafe_allow_html=True)
	col11, col22, col33, col44 = st.columns(4)
	st.markdown("<hr style='border:1px solid gray'>", unsafe_allow_html=True)
	col1, col2, col3, col4 = st.columns(4)

	with col11:
		model = st.selectbox("MODEL",
							 ["", "KVX", "KVX-M", "KVI", "KVF", "UVX", "UVX-M", "UVI", "UVF", "UV-C POD", "CMWI",
							  "CMWF", "CXW", "CXW-M", "KVV"], key=f'model{num}')
	with col22:
		length = st.selectbox('Length', ['', 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000], key=f'length{num}')
	with col33:
		width = st.selectbox('Width', ['', 1000, 1250, 1500, 1750, 2000], key=f'width{num}')
	with col44:
		height = st.number_input('Height', key=f'height{num}')
	with col11:
		sections = st.number_input('Sections', key=f'sections{num}', min_value=0)
	with col22:
		flowrate = st.number_input('Flowrate', key=f'flowrate{num}')

	with col1:
		configuration = st.selectbox(f'Configuration', ["WALL", "ISLAND"], key=f'config{num}')
	with col2:
		lights = st.selectbox('Lights',
							  ["", "LED STRIP L6 Inc DALI", "LED STRIP L12 inc DALI", "LED STRIP L18 Inc DALI",
							   "Small LED Spots inc DALI", "Large LED Spots inc DALI", "HCL600 DALI",
							   "HCL1200 DALI", "HCL1800 DALI", "LM6"], key=f'lights{num}')
	with col3:
		fireSuppression = st.selectbox('FireSuppression',
									   ["TANK SYSTEM", "TANK TRAVEL", "TANK DISTANCE", "NOBEL", "AMEREX"],
									   key=f'fire{num}').lower()
	#if fireSuppression.startswith('tank'):
		#with col4:
			#num_tanks = st.number_input('Number of Tanks', min_value=0, max_value=100, key=f'tanks{num}')
	with col1:
		special_works = st.selectbox("Special Works", [], key=f'special{num}')
	with col2:
		cladding = st.selectbox("Cladding", ['', '2M² (HFL)'], key=f'cladding{num}')
	with col3:
		infill_pannel = st.number_input("Infill Pannel", min_value=0, max_value=20, key=f'infill{num}')
	with col4:
		grease_filters = st.number_input("Grease Filters", min_value=0, max_value=20, key=f'grease{num}')
	with col1:
		junction_box = st.number_input("PSU / Junctions Box", min_value=0, max_value=20, key=f'junction{num}')
	with col2:
		crating = st.number_input("Crating", min_value=0, max_value=20, key=f'crating{num}')

	st.markdown("<hr style='border:1px solid gray'>", unsafe_allow_html=True)
	st.markdown("<hr style='border:1px solid gray'>", unsafe_allow_html=True)

	return {
		'model': model,
		'length': length,
		'sections': sections,
		'configuration': configuration,
		'lights': lights,
		#'fireSuppression': fireSuppression,
		'cladding': cladding,
		'infill_pannel': infill_pannel,
		'junction_box': junction_box,
		'grease_filters': grease_filters,
		'junction_box': junction_box,
		'special_works': special_works,
		'crating': crating,
		'width': width,
		'height': height,
		'flowrate': flowrate,

	}


