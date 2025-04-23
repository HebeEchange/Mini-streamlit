import requests
import streamlit as st

def getUserTransactions(auth_response, userID):
    page = 1
    finished = False
    transactions = []
    
    def req(_page):
        
        api_url = f"https://flex-integ-api.sharetribe.com/v1/integration_api/transactions/query?userId={userID}&page={_page}"
        try:
            response = requests.get(
                api_url, 
                timeout=5000, 
                headers={
                    "Authorization": f"Bearer {auth_response['access_token']}",
                    "Accept": "application/json"
                }
            )
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
            transactions.extend(response["data"])
            page += 1
        else:
            finished = True
            
    return transactions
        
    