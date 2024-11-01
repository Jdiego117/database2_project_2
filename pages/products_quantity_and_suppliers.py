import streamlit as st
import pandas as pd
from repositories.products_repository import products_supplier_quantity

st.title("Products")
st.text("Get all products with their stock quantity and supplier name")

products = products_supplier_quantity()

df = pd.DataFrame(products, columns=['Product name', 'Stock quantity', 'Supplier name'])

st.write(df)