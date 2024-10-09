import streamlit as st
import snowflake.connector
import pandas as pd

# Title of the Streamlit app
st.title("Customers Purchasing Behaviour")

# Snowflake connection details
# You can replace the placeholders with your Snowflake credentials
def create_snowflake_connection():
    return snowflake.connector.connect(
        user='YOUR_SNOWFLAKE_USER',
        password='YOUR_SNOWFLAKE_PASSWORD',
        account='YOUR_SNOWFLAKE_ACCOUNT',
        warehouse='YOUR_SNOWFLAKE_WAREHOUSE',
        database='YOUR_SNOWFLAKE_DATABASE',
        schema='YOUR_SNOWFLAKE_SCHEMA'
    )

# Function to fetch data from the Snowflake customers table
def fetch_customers_data():
    conn = create_snowflake_connection()
    query = "SELECT * FROM customers"
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    
    # Fetch column names
    columns = [desc[0] for desc in cur.description]
    
    # Close cursor and connection
    cur.close()
    conn.close()
    
    # Create a DataFrame
    return pd.DataFrame(data, columns=columns)

# Button to load the customers data
if st.button("Load Customers Data"):
    st.text("Fetching data from Snowflake...")
    
    # Fetch customers data from Snowflake
    customers_df = fetch_customers_data()
    
    if customers_df.empty:
        st.text("No data found in the customers table.")
    else:
        st.dataframe(customers_df)

