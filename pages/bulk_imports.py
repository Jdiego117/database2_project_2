import streamlit as st
import pandas as pd
from repositories.products_repository import bulk_insert_products
from repositories.customers_repository import bulk_insert_customers
from repositories.suppliers_repository import bulk_insert_suppliers
from repositories.product_suppliers_repository import bulk_insert_product_suppliers
from repositories.orders_repository import bulk_insert_orders
from repositories.order_items_repository import bulk_insert_order_items

def extract_products_from_excel(products_excel):
    try:
        products_df = pd.read_excel(products_excel)
    except Exception as e:
        st.write(f'Error reading the products excel file: {e}')
        return None

    products_df = products_df.rename(columns={
        "Name" : "name",
        "Price" : "price",
        "Stock Quantity" : "stock_quantity"
    })

    products_df['price'] = products_df['price'].astype(float)
    products_df['stock_quantity'] = products_df['stock_quantity'].astype(int)
    
    bulk_insert_products(products_df)
    
    st.write(products_df)

def extract_customers_from_excel(customers_excel):
    try:
        customers_df = pd.read_excel(customers_excel)
    except Exception as e:
        st.write(f'Error reading the products excel file: {e}')
        return None
    
    customers_df = customers_df.rename(columns={
        "Name" : "name",
        "Contact Email" : "contact_email",
        "Identification" : "identification"
    })
    
    customers_df['identification'] = customers_df['identification'].astype(str)
    
    bulk_insert_customers(customers_df)
    
    st.write(customers_df)
    
def extract_suppliers_from_excel(suppliers_excel):
    try:
        suppliers_df = pd.read_excel(suppliers_excel)
    except Exception as e:
        st.write(f'Error reading the products excel file: {e}')
        return None
    
    suppliers_df = suppliers_df.rename(columns={
        "Name" : "name",
        "Contact Email" : "contact_email"
    })
    
    bulk_insert_suppliers(suppliers_df)
    
    st.write(suppliers_df)
    
def extract_product_suppliers_from_excel(product_suppliers_excel):
    try:
        product_suppliers_df = pd.read_excel(product_suppliers_excel)
    except Exception as e:
        st.write(f'Error reading the products excel file: {e}')
        return None
    
    product_suppliers_df = product_suppliers_df.rename(columns={
        "Product ID" : "product_id",
        "Supplier ID" : "supplier_id"
    })
    
    bulk_insert_product_suppliers(product_suppliers_df)
    
    st.write(product_suppliers_df)
    
def extract_orders_from_excel(orders_excel):
    try:
        orders_df = pd.read_excel(orders_excel)
    except Exception as e:
        st.write(f'Error reading the products excel file: {e}')
        return None
    
    orders_df = orders_df.rename(columns={
        "Customer ID" : "customer_id",
        "Total" : "total"
    })
    
    bulk_insert_orders(orders_df)
    
    st.write(orders_df)

def extract_order_items_from_excel(order_items_excel):
    try:
        order_items_df = pd.read_excel(order_items_excel)
    except Exception as e:
        st.write(f'Error reading the products excel file: {e}')
        return None
    
    order_items_df = order_items_df.rename(columns={
        "Order ID" : "order_id",
        "Product ID" : "product_id",
        "Quantity" : "quantity",
        "Price" : "price"
    })
    
    order_items_df['quantity'] = order_items_df['quantity'].astype(int)
    order_items_df['price'] = order_items_df['price'].astype(float)

    bulk_insert_order_items(order_items_df)

    st.write(order_items_df)

products_excel = st.file_uploader('Upload the products excel file', type=['xlsx', 'xls'])
customers_excel = st.file_uploader('Upload the customers excel file', type=['xlsx', 'xls'])
suppliers_excel = st.file_uploader('Upload the suppliers excel file', type=['xlsx', 'xls'])
product_suppliers_excel = st.file_uploader('Upload the product suppliers excel file', type=['xlsx', 'xls'])
orders_excel = st.file_uploader('Upload the orders excel file', type=['xlsx', 'xls'])
order_items_excel = st.file_uploader('Upload the order items excel file', type=['xlsx', 'xls'])

if st.button('Upload'):
    if products_excel is not None:
        extract_products_from_excel(products_excel)
        
    if customers_excel is not None:
        extract_customers_from_excel(customers_excel)
        
    if suppliers_excel is not None:
        extract_suppliers_from_excel(suppliers_excel)
        
    if product_suppliers_excel is not None:
        extract_product_suppliers_from_excel(product_suppliers_excel)
        
    if orders_excel is not None:
        extract_orders_from_excel(orders_excel)
        
    if order_items_excel is not None:
        extract_order_items_from_excel(order_items_excel)