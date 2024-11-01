import streamlit as st
import pandas as pd
from repositories.orders_repository import get_orders_item_count

st.title("Orders Item Count")
st.text("Get the total number of items for each order.")

orders = get_orders_item_count()

df = pd.DataFrame(orders, columns=['Id', 'Total items'])

st.write(df)