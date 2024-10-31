import streamlit as st
import pandas as pd
from repositories.customers_repository import get_customers_with_orders

st.title("Customers With Orders")
st.text("Get all customers who have placed orders, even if they have multiple orders.")

customers = get_customers_with_orders()

df = pd.DataFrame(customers, columns=['Email', 'Name', 'Identification', 'Order Count'])

st.write(df)