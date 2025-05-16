import streamlit as st
import re
import requests

WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZmMDYzZTA0MzE1MjZjNTUzYzUxMzEi_pc"

def is_valid_email(email):
    # validation email
    email_pat = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pat, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Prénom")
        email = st.text_input("Adresse Email")
        message = st.text_area("Veuillez saisir votre message")
        submit_but = st.form_submit_button(label="Submit")

        if submit_but:
            if not WEBHOOK_URL:
                st.error("Service non disponible, veullez essayer plus tard", icon="📧")
                st.stop()

            if not name:
                st.error("Veullez saisir votre nom.", icon="🧑")
                st.stop()

            if not email:
                st.error("Veullez saisir votre addresse email.", icon="📨")
                st.stop()

            if not is_valid_email(email):
                st.error("Veullez saisir une addresse email valide.", icon="📧")
                st.stop()

            if not message:
                st.error("Veullez entrer votre message.", icon="💬")
                st.stop()
            #Envoyer les données
            data = {"email": email, "name": name, "message": message}
            reponse = requests.post(WEBHOOK_URL, json=data)

            if reponse.status_code == 200:
                st.success("Votre message à été envoyé avec succès !! 🎉", icon="🚀" )
            else:
                st.error("Il y'a une erreur votre message n'a pas ete envoyé.", icon="😰")