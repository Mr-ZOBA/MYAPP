import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np

#%matplotlib inline
import streamlit.components.v1 as stc
from PIL import Image

html_temp = """
		<div style="background-color:#aab7b8;padding:5px;border-radius:11px">
		<h1 style="color:black;text-align:center;"> Analyse des meilleurs films des services Streaming </h1>
		<h4 style="color: #c0392b ;text-align:center;">-- Film streaming -- </h4>
		</div>
		"""

# Load EDA Pkgs

def load_data(data):
    df = pd.read_csv(data)
    return df

def stream():
	#----------- Definition de l'entête ---------------
    stc.html(html_temp)
    dt = "https://media.npr.org/assets/img/2024/01/31/lk_streaming-services_grid1_wide-de87c91fae6166c4363c65d50062c9a83d95dbc3.png?s=1200&c=85&f=webp"
    st.image(dt, use_container_width=True)

    df = load_data("data/moviestreams.csv")
    STMenu = ["Descriptive", "Plot", "Info_Variable"]
    choice1 = st.sidebar.selectbox("Menu ST", STMenu)

    if choice1 == "Descriptive":
        st.success("**Analyse Descriptive**")
        with st.expander("**Le fichier à été télécharge sur Kaggle. (Data we use here is from Kaggle). Cliqué pour afficher les données**"):
            st.dataframe(df)
            st.success("La base de donnée à été importé avec succès")
        #--Determinons le nombre de ligne et de colonne--------
        with st.expander("**Determinons le nombre de lignes et de colonnes**"):
            nb = st.write(df.shape)
            #--------- les types des variables dans la base ----------
        with st.expander("**🍅 Affichons les type de données de la base**"):
            st.write(df.dtypes)
        #-------- Faisons un check des valeurs manquantes -----------
        with st.expander("**🍅 Afficher_Valeurs_manquantes**"):
            st.write(df.isna().sum().T)
            st.text("On remarque qu'il y'a des valeurs manquantes au niveau de plusieurs variables. Il ressort que la variable âge comporte plus de valeurs manquantes (9390)")
        with st.expander("**🍅 Supprimons les deux première ligne de la base de données**"):
            st.write(df.drop(['Unnamed: 0','ID'], axis=1, inplace=True))
            st.write(df.columns.tolist())
        with st.expander("**🍅 calculons les caracteristiques de la base**"):
            st.write(df.describe().T)

    if choice1 == "Plot":
        st.title("representations graphiques")
        col1, col2 = st. columns([2,1])
        with col1:
            with st.expander("🍅 Langues les plus utilisées"):
                lang = df['Language'].value_counts().head(12)
                #lang= lang.sort_values().
                fig2 = px.bar(
                            lang,
                            x=lang.index,
                            y= lang.values,
                            title="Top 12 langues de streaming",
                            labels={'x':'Language du film', 'y':'Nombre'},
                            text=lang.values,
                            height = 600
                            )
                #st.plotly_chart(fig2, textposition='outside')
                st.write(fig2.update_traces(texttemplate='%{text: .2s}', textposition='outside'))
                st.write("Il ressort que parmi les films srtreaming ceux dont la langue est l'anglais sont les plus regarde suivi de l'hindi")
                #---- Nombre de film  de film Netfix par groupe d'âge ----
            with st.expander("🍅 Film de la plateform Netfix en fonction du groupe d'âge"):
                netflix = df[df["Netflix"]==1]
                netf =netflix['Age'].value_counts()
                fig3 = px.bar(netf,
                            x=netf.index,
                            y=netf.values,
                            title="Film de la Platforme Netflix visionne en fonction des groupes d'âge",
                            labels={'x':"Groupe d'âge des films Netflix", 'y':"Nombre"},
                            text=netf.values,
                            height=600
                            )
                st.write(fig3.update_traces(texttemplate='%{text: .2s}', textposition='outside'))
                st.text("Pour le service streaming Netflix, les films du groupe d'âge 18+ sont les plus regardé, ")
        with col2:
            with st.expander("**# de film visionner par groupes d'âge**"):
                fg = df['Age'].value_counts()
                st.write(fg)
                st.text("Les films du groupe d'âge 18+ sont les plus regarde  et ceux du groupe d'âge 16+ sont les moins regarde")
            with st.expander("**Film visionné selon les tranches d'âge**"):
                fig = px.pie(fg,
                            values= fg.values,
                            names= fg.index,
                            )
                st.plotly_chart(fig)

    #------------------------ Hulu ------------------------
        with st.expander("🍅 Film de la plateform Hulu en fonction du groupe d'âge"):
            hulu = df[df["Hulu"]==1]
            hul =hulu['Age'].value_counts()
            fig4 = px.bar(hul,
                            x=hul.index,
                            y=hul.values,
                            title="Film de la Platforme Hulu visionne en fonction des groupes d'âge",
                            labels={'x':"Groupe d'âge des films Hulu", 'y':"Nombre"},
                            text=hul.values,
                            height=600
                        )
            st.write(fig4.update_traces(marker_color=" #7f8c8d",texttemplate='%{text: .2s}', textposition='outside'))
            st.text("Pour le service streaming Hulu, les films du groupe d'âge 18+ sont les plus regardé")
            
    #------------------------ Prime Video ------------------------
        with st.expander("🍅 Film de la plateform Prime Video en fonction du groupe d'âge"):
            prime = df[df["Prime Video"]==1]
            prim =prime['Age'].value_counts()
            fig5 = px.bar(prim,
                        x=prim.index,
                        y=prim.values,
                        title="Film de la Platforme Prime Video visionne en fonction des groupes d'âge",
                        labels={'x':"Groupe d'âge des films Prime Video", 'y':"Nombre"},
                        text=prim.values,
                        height=600
                        )
            st.write(fig5.update_traces(marker_color=" #7f8c8d", texttemplate='%{text: .2s}', textposition='outside'))
            st.text("Pour le service streaming Prime Video, les films du groupe d'âge 18+ sont les plus regardé")

    #----------------------------- Disney+ ----------------------------
        with st.expander("🍅 Film de la plateform Disney+ en fonction du groupe d'âge"):
            disneyp = df[df["Disney+"]==1]
            disn =disneyp['Age'].value_counts()
            fig6 = px.bar(disn,
                        x=disn.index,
                        y=disn.values,
                        title="Film de la Platforme Disney+ visionne en fonction des groupes d'âge",
                        labels={'x':"Groupe d'âge des films Disney+", 'y':"Nombre"},
                        text=disn.values,
                        height=600
                        )
            st.write(fig6.update_traces(marker_color="#7f8c8d", texttemplate='%{text: .2s}', textposition='outside'))
            st.text("Pour le service streaming Disney+, les films du groupe d'âge all (moins de 7) sont les plus regardé")

    #------------------ analyse du score (Rotten Tomatoes --------------------
        with st.expander("🍅 Analyse des score attribués aux differents films"):
            RTO = df['Rotten Tomatoes'].value_counts()#.head(20)
            fig7 = px.bar(RTO,
                        x=RTO.index,
                        y=RTO.values,
                        title="Score attribué au films",
                        labels={'x':'Score', 'y':'Nombre'},
                        text= RTO.values,
                        height= 600
                        )
            st.write(fig7.update_traces(texttemplate='%{text: .2s}', textposition='outside'))
            st.text("De manière generale, Plus de personnes on attribue une note positve superieur ou egale à 60 ")
            
        #-------- Répresentation en fonction des films ayant reçu un score de 100 --------
        with st.expander("🍅 Films ayant reçu la note de 100 par service streaming"):
            data = pd.DataFrame(
                                {'Streaming service':['Netflix','Hulu','Prime Video','Disney+'],
                                'Rotten Tomatoes':[
                                                netflix["Rotten Tomatoes"].value_counts()[0],
                                                hulu["Rotten Tomatoes"].value_counts()[0],
                                                prime["Rotten Tomatoes"].value_counts()[0],
                                                disneyp["Rotten Tomatoes"].value_counts()[0],
                                                ],
                                }
                                )
        
            data = data.sort_values(by='Rotten Tomatoes', ascending=False)
            fig8 = px.pie(data,
                        names= data['Streaming service'],
                        values= data['Rotten Tomatoes'],
                        title= "Films ayant reçu la note de 100 par service streaming"
                        )
            st.plotly_chart(fig8)
            st.text("Il ressort que parmi les films ayant réçu la note maximale 60,6% sont de la plateforme Prime Video, 30,7% sont de la plateforme Netflix, 4,48% sont de la plateforme Disney+ et 4,25% de la plateforme Hulu ")

        #------------- Popularité des films streamings vidéo ------------
        with st.expander("🍅 Répresentation des films selon leurs popularités"):
            FP = df['IMDb'].value_counts()
            fig9 = px.bar(
                        FP,
                        x=FP.index,
                        y=FP.values,
                        title="Films selon leurs popularités",
                        labels={'x':'Popularité', 'y':'Nombre'},
                        text=FP.values,
                        height=600
                        )
            st.write(fig9.update_traces(marker_color="#7f8c8d", texttemplate='%{text: .2s}', textposition='outside'))
            st.text("On remarque qu'il y'a plus de films qui ont une popularté de niveau 6.5")

        #----------- Nombre de fois que le film à ete joué -----------
        with st.expander("🍅 Nombre de fois que le film à ete jouer"):
            RT = pd.DataFrame( dict(df['Runtime'].value_counts().sort_values(ascending=False)[:10]).items(),
                            columns=['Runtime', 'count'] )
            # ------------- Nombre de films les plus jouer --------------
            #st.write(RT)
            # RT = RT.head(20)
            fig10 = px.bar(RT,
                        x=RT['Runtime'],
                        y=RT['count'],
                        title="top 20 des films les plus jouer selon leurs durée",
                        labels= {'Runtime':'La durée du film', 'count':'Nombre de fois que le film à ete joué'},
                        text= RT['count'],
                        height=600
                        )
            st.write(fig10.update_traces(texttemplate='%{text: .2s}', textposition='outside'))
            st.text("On remarque que les films de 90 mn soit 1h30mn de durée ont ete les plus joué")

        #----- les realisateurs et le nombre de films qu'ils ont realisé ------
        with st.expander("🍅 les realisateurs et le nombre de films qu'ils ont realisé"):
            df['Directors']=df['Directors'].astype(str)

            nd = df[df['Directors'] != np.nan]
            dit = dict()
            dr = list(nd['Directors'])

            for i in dr:
                kr = i.split(",")
                for i in kr:
                    if i in dit.keys():
                        dit[i] = dit.get(i)+1
                    else:
                        dit[i]=1
            
            direct = pd.DataFrame(dit.items(), columns=['Director', 'Count'])
            dirct = direct.sort_values(by='Count', ascending=False).head(20)
            if st.checkbox("Aficher liste Directeur des films"):
                st.write(dirct)
            #-- Nous allons supprimer la ligne des valeurs manquantes avec la fonction drop
            dirct = dirct.drop(56, axis=0)
            fig11 = px.bar(dirct,
                        x=dirct['Director'],
                        y=dirct['Count'],
                        text=dirct['Count'],
                        title="Top films selon le Realisateur",
                        height=600
                        )
            st.write(fig11.update_traces(marker_color="#7f8c8d", texttemplate='%{text: .2s}', textposition='outside'))
            #st.plotly_chart(fig11)
            st.text("Il ressort que jay Japman est le realisateur dont les films sont regarde en streaming. 36 de ses films ont ete visionne.")

        #-------- Affichons la liste des films dont le réalisateur est Jay Chapman --------
        with st.expander("🍅 Titres et genres des films dont le réalisateur est Jay Chapman"):
            fg=df[df['Directors']=='Jay Chapman'][['Directors','Title','Genres']]
            st.write(fg)

            # Explorons le genres des films 
            st.info("🍅 Top 20 des Genres de films")
            hy = dict(df['Genres'].value_counts())
            kt = dict()

            for i in hy:
                bv = i.split(",")
                for i in bv:
                    if i in kt.keys():
                        kt[i]=kt.get(i)+1
                    else:
                        kt[i]=1

            bab = pd.DataFrame(kt.items(), columns=['Genre', 'Count'])
            ba1 = bab.sort_values(by='Count', ascending=False)

            fig12 = px.bar(ba1,
                        x=ba1['Genre'],
                        y=ba1['Count'],
                        text=ba1['Count'],
                        title="Top 20 des films selon le genre",
                        height=600
                        )
            st.write(fig12.update_traces(marker_color="#7f8c8d", texttemplate='%{text: .2s}', textposition='outside'))
            #st.plotly_chart(fig11)
        
        #st.write(ba1)
        with st.expander("🍅 Les Top films Netflix. On peut dire qu'un film est meilleur si sa popularite est superieur à 8.5"):
            ntf_top = netflix[netflix['IMDb']>8.5]
            ntf_top = ntf_top[['Title','IMDb']].sort_values(by='IMDb', ascending=False)
            fig13 = px.bar(ntf_top,
                        x=ntf_top['Title'],
                        y=ntf_top['IMDb'],
                        text=ntf_top['IMDb'],
                        title="Les meilleurs films netflix",
                        height=800
                        )
            st.write(fig13.update_traces(marker_color="#7f8c8d", texttemplate='%{text: .2s}', textposition='outside'))
        # Les Top films Hulu
        with st.expander("🍅 Les Top films Hulu. On peut dire qu'un film est meilleur si sa popularite est superieur à 8.5"):
            H_top = hulu[hulu['IMDb']>8.5]
            H_top = H_top[['Title','IMDb']].sort_values(by='IMDb', ascending=False)
            fig14 = px.bar(H_top,
                        x=H_top['Title'],
                        y=H_top['IMDb'],
                        text=H_top['IMDb'],
                        title="Meilleurs films de la plateforme Hulu",
                        height=600
                        )
            st.write(fig14.update_traces(marker_color="#7f8c8d", texttemplate='%{text: .2s}', textposition='outside'))
        
        # Les Top films prime video
        with st.expander("🍅 Les Top films prime video. On peut dire qu'un film est meilleur si sa popularite est superieur à 8.5"):
            p_top = prime[prime['IMDb']>8.5]
            p_top = p_top[['Title','IMDb']].sort_values(by='IMDb', ascending=False)
            fig15 = px.bar(p_top,
                        x=p_top['Title'],
                        y=p_top['IMDb'],
                        text=p_top['IMDb'],
                        title="Meilleurs films de la plateforme Hulu",
                        height=800
                        )
            st.write(fig15.update_traces(marker_color="#7f8c8d", texttemplate='%{text: .2s}', textposition='outside'))
            

        with st.expander("🍅 Les Top films disney+. On peut dire qu'un film est meilleur si sa popularite est superieur à 8.5"):
            d_top = disneyp[disneyp['IMDb']>8.5]
            d_top = d_top[['Title','IMDb']].sort_values(by='IMDb', ascending=False)
            fig16 = px.bar(d_top,
                        x=d_top['Title'],
                        y=d_top['IMDb'],
                        text=d_top['IMDb'],
                        title="Meilleurs films de la plateforme disney+",
                        height=600
                        )
            st.write(fig16.update_traces(marker_color="#7f8c8d", texttemplate='%{text: .2s}', textposition='outside'))

        #---- les films paru avant 1990 ---- 
        with st.expander("🍅 Les films paru avant 1990"):
            YT = df[df['Year']<1990][['Year', 'Title','Directors']]
            st.write(YT)

        #------- La moyenne de visionnage sur ces plateformes -------
        with st.expander("🍅 La durée moyenne de diffusion sur chaque plateforme en mn"):
            aver = pd.DataFrame({
                                "Plateforme de Streaming": ['Netflix','Hulu', 'Prime Video', 'Disney+'],
                                "stream_time": [
                                    round(netflix['Runtime'].mean(),0),
                                    round(hulu['Runtime'].mean(),0),
                                    round(prime['Runtime'].mean(),0),
                                    round(disneyp['Runtime'].mean(),0)
                                    ],
                                })

            fig18 = px.bar(aver,
                        x=aver["Plateforme de Streaming"],
                        y= aver["stream_time"],
                        title= "Durée moyenne des films par plateforme",
                        text= aver["stream_time"],
                        labels={"stream_time":"Durée moyenne"},
                        height=600
                        )
            st.write(fig18.update_traces(marker_color="#7f8c8d", texttemplate='%{text: .2s}', textposition='outside'))
            st.success("Beaucoup d'autres analyses peuvent être faites, cependant nous nous arrêtons à ce niveau")
            st.warning("Pour vos propositions d'ameliorations ou d'emplois, veuillez me contacter")


    if choice1 == "Info_Variable":
        st.info(
        """
            Information sur les variables
            - Title: Titre du film
            - Year: Année de parution du film
            - Netflix: Service de streaming 
            - Hulu: Servide de streaming
            - Disney+: Service de streaming
            - Prime Video: Service de streaming
            - Genre: Genre de film
            - Director: responsable du film
            - type: type de film
            - Country: Pays ou le film à été produit
            - Language: Langue parler dans le film
            - Runtime: Nombre de temps que le film à ete visionner par les telespectateurs
            - Age: groupe d'âge autorisé à visionner le film
            - IMDb: popularité. plus la note tend vers 10, plus le film es populaire
            - Rotten Tomatoes: Critique positive inferieur à 60% , le film est pourri (Tomate pourri)
        """
    )




