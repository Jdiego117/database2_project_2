import streamlit as st
import pandas as pd
from repositories.products_repository import products_out_of_stock

st.title("Products out of stock")
st.text("Get the products that are out of stock ")

products = products_out_of_stock()

df = pd.DataFrame(products, columns=['Product name'])

st.write(df)