import streamlit as st
import pandas as pd
from repositories.products_repository import products_min_price

st.title("Product Minimum Price")
st.text("Get the minimum price of products in the store")

products = products_min_price()

df = pd.DataFrame(products, columns=['Min price'])

st.write(df)