import streamlit as st
import pandas as pd
from repositories.orders_repository import get_orders_customer

st.title("Orders with Customers")
st.text("Get all orders along with their respective customers.")

orders = get_orders_customer()

df = pd.DataFrame(orders, columns=['Id', 'Name', 'Total'])

st.write(df)