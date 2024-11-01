import streamlit as st
import pandas as pd
from repositories.orders_repository import get_avg_quantity_per_order

st.title("Average Quantity Per Order")
st.text("Get the average quantity of items ordered per order.")

orders = get_avg_quantity_per_order()

df = pd.DataFrame(orders, columns=['Average Quantity Per Order'])

st.write(df)