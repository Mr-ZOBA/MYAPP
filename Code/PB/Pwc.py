import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np

#%matplotlib inline

from PIL import Image

# Load EDA Pkgs

import streamlit.components.v1 as stc

html_tempi = """
		<div style="background-color:#aab7b8;padding:2px;border-radius:11px">
		<h1 style="color:black;text-align:center;"> Customer Churn data Analysis Project.. 📚 </h1>
		<h4 style="color: #c0392b ;text-align:center;">-- Power-BI -- </h4>
		</div>
		"""

def Pwc_Services():
    stc.html(html_tempi)
    imgA = "img/PB5.png"
    #img = open(imgA)
    st.image(imgA, use_container_width=True)
    #st.info("🌍 Stage Virtuel avec L'organisation Americaine Pwc")
    st.divider()
    st.write("\n")
    st.subheader("Stage Virtuel avec L'organisation Americaine Pwc 🌍 ", anchor=False)
    st.write(
        """
            Compétences Necessaire

            - Nettoyage des données 
            - Inspection des données 
            - Transformation des données 
            - Normalisation des données 
            - Visualisation des données 

            -Inspection des données:
            Inspection visuelle des données afin d'identifier les erreurs, les incohérences ou les valeurs manquantes.

            -Transformation des données:
            Conversion des données d'un format ou d'une structure à un autre, afin de les rendre plus adaptées à une tâche ou à une analyse spécifique.

            -Normalisation des données:
            Convertir les données dans un format standard, par exemple en convertissant tout le texte en minuscules ou en normalisant les formats de date.

            Outils necessaires

            - Microsoft Excel 
            - Microsoft SQL Server
            - Microsoft Power BI



            Taches 1: Tendance de centre d'appelle
            
            Taches 2: Retenir les employés
          
            Taches 3: Diversité et inculsion
           
        """
        )
    
    Menu = "img/Menu.png"
    st.image(Menu, use_container_width=True)
    Churn = "img/Churn.png"
    st.image(Churn, use_container_width=True)
    Risk = "img/Risk.png"
    st.image(Risk, use_container_width=True)
    Ser = "img/Serv.png"
    st.image(Ser, use_container_width=True)
    Result = "img/Result.png"
    st.image(Result, use_container_width=True)

    st.info("Pour acceder au fichier PowerBI, veullez cliquer sur ce lien")
    link='check out this [Customer Churn Dashboard](https://app.powerbi.com/links/p8l7X3nhJN?ctid=9ccc2f66-669a-49ea-8050-9ecf5351bb3b&pbi_source=linkShare)'
    st.markdown(link,unsafe_allow_html=True)
    
