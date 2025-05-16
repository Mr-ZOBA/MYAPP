import streamlit as st

from Code.PB.Pwc import Pwc_Services
from Code.PB.Marvel import Marvel_services
from Code.PB.GIS import GIS

def powerbi_project():
    Menu2 = ["Pwc", "Marvel", "AESGIS"]
    choice1 = st.sidebar.selectbox("Autre Logiciels", Menu2)

    if choice1 == "Pwc" :
        Pwc_Services()
    elif choice1 == "Marvel":
        Marvel_services()
    elif choice1 == "AESGIS":
        GIS()
    else:
        st.text("cette partie n'est pas pris en compte")

powerbi_project()