import streamlit as st
import pandas as pd
from auth.getToken import getAuthToken
from functions.users.flattenAttributes import flatten_attributes
from functions.users.loadCustomerData import loadCustomerData
from functions.users.getUserListing import getUserListing

def getUsersWithNoListings(auth):
    customer_data = loadCustomerData(auth_response=auth)
    customers = []
    if customer_data:
        # Suppression des utilisateurs qui ont au moins un logement dans le listing
        for user in customer_data:
            userID = user["id"]
            listing = getUserListing(auth=auth, userID=userID)
            if not listing:
                customers.append(user)                
                
    return customers