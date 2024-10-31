import streamlit as st
import pandas as pd
from repositories.customers_repository import get_customers_expense

st.title("Get customers and their total expense")
st.text("Get all customers and the total amount they have ordered, including those who haven't ordered anything.")

customers = get_customers_expense()

df = pd.DataFrame(customers, columns=['Name', 'Email', 'Total'])

st.write(df)