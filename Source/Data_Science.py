import streamlit as st 
import streamlit.components.v1 as stc 
from Code.DS.eda_app import run_eda_app
from Code.DS.ml_app import run_ml_app
from Code.DS.Home import Home

html_tem = """
		<div style="background-color:#3872fb;padding:2px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Prédiction du risque de diabète au stade précoce </h1>
		<h4 style="color:white;text-align:center;">Diabètes </h4>
		
		</div>
		"""

def Data_Science():
	# st.title("ML Web App with Streamlit")
	stc.html(html_tem)

	menu = ["Home","EDA","ML"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		Home()
	elif choice == "EDA":
		run_eda_app()
	else:
		run_ml_app()
	#else:
		#st.subheader("About")
		#st.text("Learn Streamlit Course")
		#st.text("Jesus Saves @JCharisTech")
		#st.text("By Jesse E.Agbe(JCharis)")

Data_Science()