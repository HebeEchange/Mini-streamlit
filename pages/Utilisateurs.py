import streamlit as st
import pandas as pd
from auth.getToken import getAuthToken
from functions.users.flattenAttributes import flatten_attributes
from functions.users.getUserTransactions import getUserTransactions
from functions.users.loadCustomerData import loadCustomerData   

auth = getAuthToken()

st.title("Données Clients")
    
customer_data = loadCustomerData(auth_response=auth)
if customer_data:
    st.write("Données clients récupérées avec succès")

    # Aplatir les données
    flattened_data = flatten_attributes(customer_data)

    # Convertir en DataFrame
    df = pd.DataFrame(flattened_data)
    filteredDF = df[["id", "deleted", "banned", "email", "createdAt", "state", "emailVerified", "displayName", "firstName", "lastName", "age", "ville", "phoneNumber"]]
    
    # Ajouter une colonne transaction à filteredDF
    filteredDF["transactions"] = 0
       
    # Ajouter le nombre de trnansactions sur chaque utilisateur
    for index, row in filteredDF.iterrows():
        userID = row["id"]
        transactions = getUserTransactions(auth_response=auth, userID=userID)
        if transactions:
            filteredDF.at[index, "transactions"] = len(transactions)
        else:
            filteredDF.at[index, "transactions"] = 0
    
    # Afficher les données dans un tableau interactif
    st.dataframe(
        filteredDF, 
        column_config={
            "id": st.column_config.TextColumn("ID"),
            "deleted": st.column_config.CheckboxColumn("Supprimé"),
            "banned": st.column_config.CheckboxColumn("Banni"),
            "email": st.column_config.LinkColumn("Email"),
            "createdAt": st.column_config.DatetimeColumn("Créé le"),
            "state": st.column_config.TextColumn("État"),
            "emailVerified": st.column_config.CheckboxColumn("Email vérifié"),
            "displayName": st.column_config.TextColumn("Pseudo"),
            "fistName": st.column_config.TextColumn("Prénom"),
            "lastName": st.column_config.TextColumn("Nom"),
            "ville": st.column_config.TextColumn("Ville"),
            "phoneNumber": st.column_config.TextColumn("Téléphone"),
            "age": st.column_config.TextColumn("Age"),
            "transactions": st.column_config.NumberColumn("Transactions"),
        }, 
        column_order=[
            "displayName", "firstName", "lastName", "email", "age", "ville", 
            "phoneNumber", "naissance", "emailVerified", "state", 
            "deleted", "banned", "createdAt", "id", "transactions"
        ],
        use_container_width=True,
    )

st.markdown(
        r"""
        <style>
        .stMainBlockContainer {
               max-width: 100vw;
            }
        </style>
        """, unsafe_allow_html=True
    )
