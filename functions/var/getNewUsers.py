import requests
import streamlit as st
from datetime import datetime

def getNewUsers(auth_response):
    # URL de l'API
    page = 1
    finished = False
    customers = []
    
    # Obtention de la date du jour
    date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=1).isoformat()
    
    def req(_page):
        api_url = f"https://flex-integ-api.sharetribe.com/v1/integration_api/users/query?createdAtStart={date}&page={_page}"
        try:
            # Effectuer une requête GET
            response = requests.get(api_url, timeout=5000, headers={"Authorization": f"Bearer {auth_response['access_token']}"})
            response.raise_for_status()
            
            # Retourner les données JSON
            return response.json()
        except requests.exceptions.RequestException as e:
            # Gérer les erreurs d'appel API
            st.error(f"Erreur lors de l'appel API : {e}")
            return None
        
    while not finished :
        response = req(page)
        
        if response and int(response["meta"]["totalPages"]) >= page:
            customers.extend(response["data"])
            page += 1
        else:
            finished = True
            
    return customers