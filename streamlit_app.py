import os
import streamlit as st
import requests
import json
import time
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

# Récupération des secrets depuis le fichier .env
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# Configuration de l'API
API_VERSION = "2024-02-15-preview"
HEADERS = {
    "Content-Type": "application/json",
    "api-key": AZURE_OPENAI_KEY,
}

# URL de l'endpoint
ENDPOINT = f"{AZURE_OPENAI_ENDPOINT}openai/deployments/{DEPLOYMENT}/chat/completions?api-version={API_VERSION}"

# Initialisation de l'historique du chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage des messages de l'historique
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Saisie de l'utilisateur
if prompt := st.chat_input("Que voulez-vous demander ?"):
    # Ajout du message de l'utilisateur à l'historique
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Affichage de la réponse de l'assistant
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Préparation du payload
        payload = {
            "messages": [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            "temperature": 0.7,
            "top_p": 0.95,
            "max_tokens": 800
        }

        try:
            response = requests.post(ENDPOINT, headers=HEADERS, json=payload)
            response.raise_for_status()
            response_json = response.json()
            
            assistant_response = response_json['choices'][0]['message']['content']
            
            for word in assistant_response.split():
                full_response += word + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            
            # Ajout de la réponse de l'assistant à l'historique
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except requests.RequestException as e:
            st.error(f"Une erreur s'est produite lors de la communication avec l'API : {e}")