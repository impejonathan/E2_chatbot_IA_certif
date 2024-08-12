# Chat-bot GPT-4 avec Streamlit

Ce projet est une application de chat-bot utilisant GPT-4 d'OpenAI, déployée sur Azure, et développée avec Streamlit. L'application permet aux utilisateurs d'interagir avec un assistant IA avancé dans une interface de chat conviviale.

## Fonctionnalités

- Interface de chat interactive
- Utilisation du modèle GPT-4 d'OpenAI via Azure
- Historique de conversation persistant pendant la session
- Affichage progressif des réponses pour une expérience utilisateur améliorée

## Prérequis

- Python 3.10+
- Compte Azure avec OpenAI déployé
- Clé API Azure OpenAI

## Installation

1. Clonez ce dépôt :
git clone https://github.com/impejonathan/E2_chatbot_IA_certif
cd E2_chatbot_IA_certif

2. Installez les dépendances :
pip install -r requirements.txt

3. Créez un fichier `.env` à la racine du projet et ajoutez vos informations d'identification Azure :
AZURE_OPENAI_ENDPOINT=votre_endpoint_azure
AZURE_OPENAI_KEY=votre_cle_api_azure
AZURE_OPENAI_DEPLOYMENT=nom_de_votre_deploiement

## Utilisation

Pour lancer l'application, exécutez :

L'application sera accessible dans votre navigateur, généralement à l'adresse `http://localhost:8501`.

## Structure du projet

- `streamlit_app.py` : Le script principal contenant le code de l'application Streamlit
- `.env` : Fichier contenant les variables d'environnement (ne pas partager ou commiter)
- `requirements.txt` : Liste des dépendances Python

## Configuration

Vous pouvez ajuster les paramètres suivants dans le code :

- `temperature` : Contrôle la créativité des réponses (0.0 - 1.0)
- `top_p` : Contrôle la diversité des réponses (0.0 - 1.0)
- `max_tokens` : Nombre maximum de tokens dans la réponse

## Sécurité

- Ne partagez jamais votre fichier `.env` ou vos clés API.
- Ajoutez `.env` à votre fichier `.gitignore`.


## Licence

[MIT License](https://opensource.org/licenses/MIT)

## Contact

Pour toute question ou suggestion, veuillez ouvrir une issue dans ce dépôt GitHub.