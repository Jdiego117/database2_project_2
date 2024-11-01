import streamlit as st
import pandas as pd
from repositories.suppliers_repository import get_suppliers_products

st.title("Suppliers")
st.text("Get a list of suppliers and the number of products they supply.")

suppliers = get_suppliers_products()

df = pd.DataFrame(suppliers, columns=['Supplier name', 'Number of products'])

st.write(df)