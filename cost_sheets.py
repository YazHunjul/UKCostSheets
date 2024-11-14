from General_info import genInfo as GI
from Canopy_sheet import canopy_sheet as CS
from Canopy_sheet import canopyQuote as CQ
import streamlit as st

sheets = []


def cost_sheets():
	info = GI.genInfo()


	for select in info['selections']:
		sheets.append(select)
		if select == "Canopy":
			canopySheet = CS.canopyMain(info)
			CQ.download_button(canopySheet, info)


