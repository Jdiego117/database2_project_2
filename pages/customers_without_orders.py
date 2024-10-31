import streamlit as st
import pandas as pd
from repositories.customers_repository import get_customers_without_orders

st.title("Customers Without Orders")
st.text("List Customers Who Have Not Placed Any Orders")

customers = get_customers_without_orders()

df = pd.DataFrame(customers, columns=['Id', 'Name', 'Identification'])

st.write(df)