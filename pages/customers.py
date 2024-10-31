import streamlit as st
import pandas as pd
from repositories.customers_repository import get_customers

st.title("Get customers")

customers = get_customers()

df = pd.DataFrame(customers, columns=['Id', 'Name', 'Email', 'Identification'])

st.write(df)