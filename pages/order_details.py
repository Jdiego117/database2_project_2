import streamlit as st
import pandas as pd
from repositories.orders_repository import orders_details

st.title("Orders details")
st.text("Get the details of orders along with their items.")

orders = orders_details()

df = pd.DataFrame(orders, columns=['Order id', 'Customer name', 'Total', 'Total items'])

st.write(df)