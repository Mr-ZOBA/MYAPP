import streamlit as st
from Code.contact import contact_form


@st.dialog("Contacter Moi")
def cont_forms():
    contact_form()



#--------- HERO SECTION ------------
st.image("./img/Linkdhin.png", width=900)
col1, col2 = st. columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./img/DB.png", width=230)
with col2:
    st.title("M. ZONGO Babou", anchor=False)
    st.write(
        "Monitoring and Evaluation spécialist | Data Scientist | Power-Bi developper | Gis Analyst | Impact Evaluator | Commcare expert"
    )
    if st.button(" ✉️ Contacter Moi"):
        cont_forms()

st.image("./img/P2.png", width=800)
# Expériences & Qualification
with st.expander("Experiences & Qualifications"):
    st.markdown(
        """
        - Plus de 5 ans d'expérience en Suivi-évaluation, apprentissage, redevabilité, collecte et analyse des données;
        - Très bonne expérience et connaissance en conduite d'études de recherche quantitative et qualitative;
        - Très bonne expérience et connaissance en analyse de données, rédactions de rapports et restitution des résultats en s'aidant du data Storytelling;
        - Bonne compréhension des principes statistiques et de leurs applications respectives;
        - Très à l'aise avec l'outil informatique;
        - Très forte capacité d'adaptation à la fois dans le domaine de l'urgence que dans le développement;
        - Réalisation des cartes geographiques;
        - Numérisation de la collecte des données (ODK, KoboCollect, Commcare).
        """
        ) 

#----------- Compétences -------------
with st.expander("Compétences"):
    st.markdown(
        """
        - Monitoring, Evaluation, learning and Research
        - Impact évaluation (très bonne connaissances des méthodes expérimentales et quasi-expérimentales d'évaluations d'impacts)
        - Programming: Python (Scikit-learn, Pandas), SQL, R, SPSS, STATA
        - Data visualisation: PowerBi, MS Excel, Plotly, shiny, streamlit
        - Modeling: Logistic regression, linear regression, decision trees 
        - Databases: MySQL
        - GIS: QGis and ArcGis
        - Edit: Latex, Word, Adobe Indesign
        - Archivage: sharepoint
        - OS: Windows
        """ 
    )

#-------- Auto formation certifiant -------
with st.expander("Auto formation"):
    st.markdown(
            """
            - Data Analyst
            - Data Scientist ( Machine learning and artificial intelligence)
            - PowerBi
            - Excel for busness intelligence
            - Analyse de données avec tityverse (Rstudio)
            - Adobe Indesign
            - QGis, ArcGis
            - github
            - R, Commcare
            - Streamlit, flask
            """
        )

#-------- Virtual InternShip -------
with st.expander("Virtual Internship"):
    st.markdown(
        """
        - Data Analytics Virtual Experience (Forage Quantium)
        - Power BI virtual case experience (Forage Pwc)
        - Busness Data Analysis GoldMan Sach (Forage Goldman Sachs)
        """
    )

with st.expander("Formations Universitaire"):
    st.markdown(
        """
        - Master en Statistiques et modélisations stockastques (MAIME-Statistiques) UFR/SEA
        - Licence en Statistiques et Informatique (LSI) UFR/ST
        """
    )

#------ ONG --------
with st.expander("ONG"):
    if st.checkbox("**Mercy Corps**"):
        st.write("Responsable Suivi-évaluation et apprentissage")
        st.success("Mercy Corps | 21 Novembre 2022 à Aujourd’hui")
        st.markdown(
                """ 
                    - Suivi évaluation des indicateurs de performance ;
                    - Mise à jour du système de suivi-évaluation ;
                    - Comptage des bénéficiaires des projets ;
                    - Paramétrage des questionnaires de collectes (XLSForm)
                    - Formation des enquêteurs ;
                    - Collecter, appurer et analyser des données ;
                    - Renseigner les indicateurs de performances ;
                    - Réaliser les évaluations (DM, PDM, Endline, Baseline, Midline)
                    - Appuyer l’équipe CARM dans la gestion du système d’apprentissage et de redevabilité ;
                    - appuyer l'organisation de l’atelier MERL au Mali (Mayambougou).
                """
                )

    if st.checkbox("**Norvegian Refugee council**"):
        st.success("NRC | 1er Septembre 2021 – 20 Novembre 2022")
        st.write("Responsable Suivi-évaluation et apprentissage et redevabilité")
        st.markdown(
                """ 
                    - Renforcer la capacité en suivi-Evaluation de l’équipe ;
                    - Conduire les évaluations sectorielles et multi-sectorielles ;
                    - Participer à atelier Régional M&E à Dakar au Sénégal du 12 au 20 Mars 2022 ;
                    - Aider à Développer les outils de suivi et d’apprentissage ;
                    - Mettre en place et assurer le fonctionnement du mécanisme de gestion des plaintes et des feedbacks ;
                    - Coordonner et effectuer la collecte de données ;
                    - Renforcement des capacités des staffs programmes en Suivi-Evaluation ;
                    - Appuyer l’équipe du Sahel et du Nord dans les évaluations.

                """
                )
        st.success("NRC | 15 Septembre 2020 – 31 Aout 2021")
        st.write("Assistant Suivi-évaluation et apprentissage et redevabilité")
        st.markdown(
                """ 
                    - Elaborer les questionnaires de collectes ;
                    - Formation des enquêteurs ;
                    - Configuration des tablettes pour les collectes de données ;
                    - Supervision des enquêteurs ;
                    - Apurement des données collectées ;
                    - Aider à l’analyse des données ;
                    - Appuyer la mise en place et le suivi du mécanisme de gestion de plaintes et des feedbacks.
                """
                )
    
    if st.checkbox("**Marie Stopes**"):
            st.success("Marie Stopes | 16 Mars 2019 – 13 Septembre 2020")
            st.write(" *Prestataire Suivi-Evaluation* ")
            st.markdown(
                    """ 
                        - Numériser la collecte de données ;
                        - Aider à la formation des enquêteurs ;
                        - Configurer les tablettes pour la collecte ;
                        - Appuyer la supervision des enquêteurs;
                        - Appuyer les activités de suivi et évaluation dans le domaine de la santé sexuelle et reproductive (SSR).
                    """
                    )

st.success("Email: zongo.babou1@gmail.com ")

st.image("./img/P3.png", width=800)