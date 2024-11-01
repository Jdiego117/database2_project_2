import streamlit as st
import pandas as pd
from repositories.products_repository import products_avg_price

st.title("Product Average Price")
st.text("Get the average price of products")

products = products_avg_price()

df = pd.DataFrame(products, columns=['Average price'])

st.write(df)