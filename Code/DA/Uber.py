import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sn
import calendar
import datetime as dt
import streamlit.components.v1 as stc

from PIL import Image

html_tem = """
        <div style="background-color:#aab7b8;padding:5px;border-radius:11px">
        <h1 style="color:black;text-align:center;"> Uber data Analysis ....🚗 </h1>
        <h4 style="color: #c0392b ;text-align:center;">-- Uber Travel -- </h4>
        </div>
        """

# Load EDA Pkgs
def load_uber_data(data):
    dg = pd.read_csv(data)
    return dg

def uber():
    stc.html(html_tem)
    imag="https://img.choice.com.au/-/media/11798b8063c74fb4b282b29e2c582378.ashx?w=760"
    st.image(imag, use_container_width=True)
    st.write("\n")
    with st.expander("**🚖 Affichons les informations sur la base de données**"):
        st.divider()
        st.write("""
            **Questions à repondre:**\n
                - A quelle distance les clients de Uber voyagent-ils ?
                - À quelle heure la plupart des gens prennent-ils 
                Uber pour se rendre à leur destination ?
                - Vérifier le but des trajets ?
                - Quel est le jour où le nombre de trajets est le plus élevé ?
                - Quel est le nombre de trajets par jour ?
                - Quels sont les trajets effectués au cours du mois ?
                - Les points de départ des trajets. Quel est le point de départ 
                le plus fréquent du voyage ?
                """)
        st.divider()

    #st.info("Affichons la base de données")
    dg = load_uber_data("data/UberD.csv")
    with st.expander("**🚖 Affichons la base de données**"):
        st.write(dg)
    c1, c2 = st.columns([2,1])
    with c1:
        with st.expander("**🚖 Verifions les details des valeurs manquantes (DVM)**"):
            st.write(dg.isnull().sum())
        with st.expander("**🚖 Verifions le nombre de lignes et de colonnes (NLC)**"):
            st.write(dg.shape)
    with c2:
        with st.expander("**🚖 Verifions si la base de données contient des lignes dupliquées doubles (DV)**"):
            st.write(dg.duplicated().sum())
            st.text("On voit que qu'une ligne est dupliqué")
        with st.expander("**🚖 Effacons la ligne contenant les valeurs manquantes (LCVM)**"):
            st.write(dg.drop_duplicates(inplace=True))
            st.success("La ligne à ete suprimé avec succès")
    with st.expander("**🚖 Déterminons les lignes qui comportent des valeurs manquantes**"):
        dg["PURPOSE*"].fillna("Not Mentioned", inplace=True)
        sf=dg[dg["END_DATE*"].isnull()]
        sj=dg[dg["CATEGORY*"].isnull()]
        sk=dg[dg["START*"].isnull()]
        sl=dg[dg["STOP*"].isnull()]
        st.write(sf)
        st.write(sj)
        st.write(sk)
        st.write(sl)
        st.text("Il ressort que seul la ligne 1155 comporte des valeurs manquantes. Nous allons donc supprimer cette ligne")
    with st.expander("**🚖 On vois qu'il n'ya plus de valeurs manquantes dans la base**"):
        dg.drop(1155, axis=0, inplace=True)
        st.write(dg.isnull().sum())
        dg["START_DATE*"]=pd.to_datetime(dg["START_DATE*"], format="%m/%d/%Y %H:%M")
        dg["END_DATE*"]=pd.to_datetime(dg["END_DATE*"], format="%m/%d/%Y %H:%M")
        hour=[]
        day=[]
        dayofweek=[]
        month=[]
        weekday=[]
        for x in dg['START_DATE*']:
            hour.append(x.hour)
            day.append(x.day)
            dayofweek.append(x.dayofweek)
            month.append(x.month)
            weekday.append(calendar.day_name[dayofweek[-1]])
        dg['Heure']=hour
        dg['Jour']=day
        dg['Jour_Semaine']=dayofweek
        dg['Mois']=month
        dg['Jour_Ouvrable']=weekday
        dg["Duration"] = dg["END_DATE*"]-dg["START_DATE*"]
        st.write(dg)
        cat=dg["CATEGORY*"].value_counts()

    with st.expander("**🚖 Catégorie des services**"):
        fig=px.bar(cat,
            x=cat.index,
            y=cat.values,
            text=cat.values,
            labels={'CATEGORY*':'CATEGORY', 'y':'Nombre'},
            title="CATEGORY DU SERVICE"
            )
        #st.pyplot(fig)
        st.write(fig.update_traces(marker_color="#0b5345",texttemplate="%{text:.2s}",textposition="outside"))
    #-------------------------------------------------------------------------------------------
    with st.expander("**🚖 Graphique**"):
        if st.checkbox("**Sur quelle distance les clients Uber voyagent-ils ?**"):
            Mil=dg["MILES*"].describe()
            st.write(Mil)
            st.info("La distance moyenne parcourue  est de 10.56 miles avec un écart type de 21.57. La plus petite distance est de 0.5mile et la plus grande est de 310 miles. également, moins de 75% ont distance parcourue inférieur à la moyenne 10.4 miles")
        if st.checkbox("**Graph de densité**"):
            fig1=plt.figure()
            k = dg["MILES*"].value_counts()
            sn.distplot(k.index,hist=True, kde=True,
            bins=20, color='#0b5345',
            hist_kws={'edgecolor':'black'},
            kde_kws={'linewidth': 2})
            st.pyplot(fig1)
            st.text("On remarque que les clients Uber prefèrent voyager sur les courtes distances")

    with st.expander("**🚖 Distance moyenne parcourue selon le motif du déplacement**"):
        DistMoy=dg.groupby("PURPOSE*")["MILES*"].mean()
        fig2=px.bar(DistMoy,
                x=DistMoy.index,
                y=DistMoy.values,
                text=DistMoy.values,
                labels={'x':'Objectif du voyage', 'y':'Moyenne de la distance (MILES)'},
                title="Distance moyenne parcourue en fonction de l'objectifs",
                height=600
                )
        st.write(fig2.update_traces(marker_color="#0b5345",texttemplate="%{text:.2s}", textposition="outside"))
        st.text("On remarque que la durée moyenne varie en fonction des objectifs de déplacements du client")
        #st.dataframe(df)

    with st.expander("**🚖 À quelles heures la plupart des gens prennent-ils Uber pour se rendre à leur destination ?**"):
        fig4=plt.figure()
        dg["Heure"].value_counts().plot(kind="bar")
        text=dg["Heure"].value_counts().values
        st.pyplot(fig4)
        st.text("Les gens prenent Uber le plus à l'heure de 15 suivi de 17h, 13h et 18h")

    with st.expander("**🚖 Objectifs du voyage (PURPOSE)**"):
        dfh=dg["PURPOSE*"].value_counts()
        fig5=px.pie(dfh,
                names=dfh.index,
                values=dfh.values,
                title="Objectifs de deplacements",
                height=450
                )
        st.plotly_chart(fig5)
        st.text("La plus part des gens n'ont pas mentionné le motif du voyage, 16% voyagent pour un meeting, 13% pour un entretien")
#---------------------------------------------------------------------------------------------------
    with st.expander("**🚖 Quel est le jour où le nombre de trajets est le plus élevé ?**"):
        fig6=plt.figure()
        dg["Jour_Ouvrable"].value_counts().plot(kind="bar")
        plt.xlabel("Jour de Travail")
        plt.ylabel("Nombre de voyage")
        plt.title("Nombre de voyage par jour")
        st.pyplot(fig6)
        st.text("On remarque que le vendredi est le jour ou on a plus de déplacements")
    #Quel est le nombre de trajets par jour ?
    with st.expander("**🚖 Quel est le nombre de trajets pour chaque date du mois ?**"):
        fig7=plt.figure()
        dg["Jour"].value_counts().plot(kind="bar")
        plt.xlabel("le jour du mois")
        plt.ylabel("Nombre de deplacement")
        plt.title("Nombre de trajet par mois")
        st.pyplot(fig7)
        st.text("Le 19ième du mois a connu le plus de déplacement")

    #Quels sont les trajets effectués au cours du mois ?
    with st.expander("**🚖 Quels sont les trajets au cours du mois ?**"):
        fig8=plt.figure()
        dg["Mois"].value_counts().plot(kind="bar")
        plt.xlabel("Numero du Mois")
        plt.ylabel("Nombre de deplacement")
        plt.title("Nombre selon le numero du mois")
        st.pyplot(fig8)
        st.text("Il y'a plus de voyage dans le mois de Décembre et le moins de voyage à ete observé au mois de Septembre")

    #Les points de départ des trajets. Quel est le point de départ le plus fréquent du voyage ?
    with st.expander("**🚖 Quel est le point de départ le plus fréquent du voyage ?**"):
        dg["START*"].replace({"Kar?chi":"Karachi"}, inplace=True)
        dg["STOP*"].replace({"Kar?chi":"Karachi"}, inplace=True)
        do=dg["START*"].value_counts().head(30)
        fig9=px.bar(do,
                    x=do.index,
                    y=do.values,
                    text=do.values,
                    labels={'y':'Nombre', 'START*':'Point de depart du trajet'},
                    title="Top 30 des point de départ Uber",
                    height=600
                    )
        fig9.update_xaxes(autotickangles=[45, 60, 90])
        st.write(fig9.update_traces(marker_color="#0b5345", texttemplate="%{text: .2s}", textposition="outside"))
        # st.plotly_chart(fig9)
    with st.expander("**🚖 Quel est le point de d'arrive le plus fréquent du des trajets ?**"):
        do1=dg["STOP*"].value_counts().head(30)
        fig10=px.bar(do1,
                    x=do1.index,
                    y=do1.values,
                    text=do1.values,
                    labels={'y':'Nombre', 'STOP*':"Point d'arrivé du trajet"},
                    title="Top 30 des point d'arrivé Uber",
                    height=600
                    )
        fig10.update_xaxes(autotickangles=[45, 60, 90])
        st.write(fig10.update_traces(marker_color="#0b5345", texttemplate="%{text: .2s}", textposition="outside"))
        st.text("Le point de départ le plus fréquenté est Cary et le point d'arrivé le plus frequenté est toujours Cary ")

    # fig11, axs = plt.subplots(2,2, figsize = (16,6))
    # sn.barplot(data = uc[(uc['PURPOSE*']=='Meeting')].groupby('START*').size().reset_index(name = 'count').sort_values(by = 'count', ascending = False)[:5], x = 'START*', y = 'count',ax = axs[0,0])
    # sn.barplot(data = uc[(uc['PURPOSE*']=='Meal/Entertain')].groupby('START*').size().reset_index(name = 'count').sort_values(by = 'count', ascending = False)[:5], x = 'START*', y = 'count',ax = axs[0,1])
    # sn.barplot(data = uc[(uc['PURPOSE*']=='Errand/Supplies')].groupby('START*').size().reset_index(name = 'count').sort_values(by = 'count', ascending = False)[:5], x = 'START*', y = 'count',ax = axs[1,0])
    # sn.barplot(data = uc[(uc['PURPOSE*']=='Customer Visit')].groupby('START*').size().reset_index(name = 'count').sort_values(by = 'count', ascending = False)[:5], x = 'START*', y = 'count',ax = axs[1,1])
    # st.pyplot(fig11)
    # st.text("")


