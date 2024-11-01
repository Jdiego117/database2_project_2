import streamlit as st
import pandas as pd
from repositories.orders_repository import get_orders_total

st.title("Orders Total")
st.text("Get the total value of all orders.")

orders = get_orders_total()

df = pd.DataFrame(orders, columns=['Total'])

st.write(df)