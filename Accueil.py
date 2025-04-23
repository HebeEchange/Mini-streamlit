import streamlit as st

from auth.getToken import getAuthToken
from functions.listings.getListings import getListing
from functions.users.getUsersWithNoListings import getUsersWithNoListings
from functions.users.loadCustomerData import loadCustomerData

st.title('Bienvenue')
st.text("Données aujourd'hui")

a, b = st.columns(2)

auth = getAuthToken()
usersCount = len(loadCustomerData(auth))
listingCount = len(getListing(auth))
noListingCount = len(getUsersWithNoListings(auth))

a.metric("Utilisateurs", usersCount, border=True)
b.metric("Logements", listingCount, border=True)

st.metric("Utilisateurs sans logement", noListingCount, border=True)