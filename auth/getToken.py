import streamlit as st
import requests 
from dotenv import load_dotenv
import os

def getAuthToken():
    # URL de l'API pour obtenir le token
    auth_url = "https://flex-api.sharetribe.com/v1/auth/token"
    
    # Données nécessaires pour l'authentification
    # Load environment variables from a .env file
    load_dotenv()

    # Retrieve sensitive data from environment variables
    payload = {
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "grant_type": "client_credentials",
        "scope": "integ"
    }
    
    # En-têtes de la requête
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Accept": "application/json"
    }
    
    try:
        # Effectuer une requête POST
        response = requests.post(auth_url, data=payload, headers=headers, timeout=5000)
        response.raise_for_status()  # Vérifie si la requête a réussi
        
        # Retourner les données JSON contenant le token
        return response.json()
    except requests.exceptions.RequestException as e:
        # Gérer les erreurs d'appel API
        st.error(f"Erreur lors de l'obtention du token : {e}")
        return None

