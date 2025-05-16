import streamlit as st 
import streamlit.components.v1 as stc 

def Home():
        st.subheader("Home")
        st.write("""
            ### Prédiction du risque de diabète
           Cet ensemble de données contient les données relatives aux 
                 signes et symptômes des patient nouvellement diabétique ou en passe de le devenir.
            #### Source des données
                - https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
            #### Les points abordés
                - EDA Section: Analyse des données
                - ML Section: Prediction grâce à l'apprentissage automatique

            """)
        with st.expander("**Information sur les variables**"):
            if st.checkbox("Age"):
                st.info("Age du repondant 1.20-65") 
            if st.checkbox("Sex"): 
                st.info("Sexe du repondant")
                st.success("1. Homme, 2. Femme")
            if st.checkbox("Polyuria"): 
                st.info("maladie caractérisée par des urines abondantes, fréquemment rencontrée dans le cas du diabète insipide et du diabète sucré")
                st.success("1.Yes, 2.No")
            if st.checkbox("Polydipsia"): 
                st.info("La polydipsie est un symptôme rencontré le plus souvent en endocrinologie et caractérisé par une " \
                "soif excessive avec augmentation de l'absorption de liquide")
                st.success("1.Yes, 2.No")
            if st.checkbox("sudden weight loss"): 
                st.info("Perte de poids")
                st.success("1.Yes, 2.No")
            if st.checkbox("weakness"): 
                st.info("Maladie chronique de longue durée et qui évolue avec le temps.")
                st.success("1.Yes, 2.No")
            if st.checkbox("Polyphagia"):
                st.info("consommation de nourriture excessive qui s'observe en dehors d'un " \
                "contexte pathologique")
                st.success("1.Yes, 2.No")
            if st.checkbox("Genital thrush"):
                st.info("Les infections à levures désignent des infections causées par un " \
                "champignon ou candida. Elles peuvent survenir à différents endroits, dont les organes")
                st.success("1.Yes, 2.No")
            if st.checkbox("visual blurring"):
                st.info("Troubles de vue")
                st.success("1.Yes, 2.No")
            if st.checkbox("Itching"):
                st.info("Déshydratation due à l'élimination du sucre excédentaire par les urines")
                st.success("1.Yes, 2.No")
            if st.checkbox("Irritability"):
                st.info("irritabilité")
                st.success("1.Yes, 2.No")
            if st.checkbox("delayed healing"):
                st.info("retard de cicatrisation")
                st.success("1.Yes, 2.No")
            if st.checkbox("partial paresis"):
                st.info("paralysie partielle")
                st.success("1.Yes, 2.No")
            if st.checkbox("muscle stiffness"):
                st.info("paralysie partielle")
                st.success("1.Yes, 2.No")
            if st.checkbox("Alopecia"):
                st.info("perte de poils sur le corps")
                st.success("1.Yes, 2.No")
            if st.checkbox("Obesity"):
                st.info("Obesité")
                st.success("1.Yes, 2.No")
            if st.checkbox("Class"):
                st.info("Class")
                st.success("1.Positive, 2.Negative.")