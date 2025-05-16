import streamlit as st
from PIL import Image

#Definissons les PAGES de notre apk

About_Me = st.Page(
    "Source/CV.py",
    title="Profil",
    icon="✨",
    default=True,
)

projet1 = st.Page(
    "Source/Data_Analysis.py",
    title="Data Analysis",
    icon= ":material/bar_chart:",
)

projet2 = st.Page(
    "Source/Data_Science.py",
    title="Data Science",
    icon= ":material/smart_toy:",
)

projet3 = st.Page(
    "Source/Autre.py",
    title="Autre Logiciels",
    icon= ":material/find_in_page:",
)

# projet4 = st.Page(
#      "Source/AESGIS.py",
#      title="AES",
#      icon= ":material/find_in_page:"
# )

# definir les volets de navigations

pageG = st.navigation(
    {
        "Info": [About_Me],
        "Data Analyst": [projet1, projet2, projet3]
    }
)

# image à afficher sur toutes les pages
st.logo("img/P4.png")

#--- Afficher les volets de navigations
pageG.run()
