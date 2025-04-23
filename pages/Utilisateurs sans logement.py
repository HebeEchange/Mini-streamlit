import streamlit as st
import pandas as pd
from auth.getToken import getAuthToken
from functions.users.getUsersWithNoListings import getUsersWithNoListings

auth = getAuthToken()

st.title("Liste des utilisateurs sans aucun logement déposé")

users = getUsersWithNoListings(auth=auth)

# Convert the users data into a DataFrame
df = pd.DataFrame(users)

# Flatten the attributes column
df = pd.concat([df.drop(['attributes'], axis=1), pd.json_normalize(df['attributes'])], axis=1)

# Select and rename relevant columns for better readability
df = df.rename(columns={
    "profile.displayName": "Pseudo",
    "profile.firstName": "Prénom",
    "profile.lastName": "Nom",
    "profile.publicData.ville": "Ville",
    "profile.protectedData.phoneNumber": "Téléphone",
    "email": "Email",
    "createdAt": "Créé le",
    "state": "État",
    "emailVerified": "Email vérifié",
    "profile.publicData.age": "Âge"
})

# Filter the columns to display
columns_to_display = [
    "Pseudo", "Prénom", "Nom", "Email", "Âge", "Ville", 
    "Téléphone", "Email vérifié", "État", "Créé le", "id"
]
df = df[columns_to_display]

# Display the data in an interactive table
st.dataframe(
    df,
    column_config={
        "Pseudo": st.column_config.TextColumn("Pseudo"),
        "Prénom": st.column_config.TextColumn("Prénom"),
        "Nom": st.column_config.TextColumn("Nom"),
        "Email": st.column_config.LinkColumn("Email"),
        "Âge": st.column_config.NumberColumn("Âge"),
        "Ville": st.column_config.TextColumn("Ville"),
        "Téléphone": st.column_config.TextColumn("Téléphone"),
        "Email vérifié": st.column_config.CheckboxColumn("Email vérifié"),
        "État": st.column_config.TextColumn("État"),
        "Créé le": st.column_config.DatetimeColumn("Créé le"),
        "id": st.column_config.TextColumn("ID"),
    },
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
