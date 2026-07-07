import streamlit as st
import pandas as pd
import plotly.express as px

# Dashboard Setup
st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Executive Sales Dashboard")

# Load Data
df = pd.read_csv('task5/Global_Superstore2.csv', encoding='ISO-8859-1')

# Sidebar Filters
st.sidebar.header("Filter Options")
region = st.sidebar.selectbox("Select Region:", df['Region'].unique())
category = st.sidebar.selectbox("Select Category:", df['Category'].unique())
sub_category = st.sidebar.selectbox("Select Sub-Category:", df['Sub-Category'].unique())
st.sidebar.markdown("---")
st.sidebar.markdown("### 📋 About This Project")
st.sidebar.info("""
**Executive Sales Dashboard**  
This dashboard provides real-time insights into regional sales performance and customer trends.  
*Built for: Internship Project*
""")

# Data Filtering
filtered_df = df[(df['Region'] == region) & 
                 (df['Category'] == category) & 
                 (df['Sub-Category'] == sub_category)]

# Main Dashboard
if not filtered_df.empty:
    col1, col2 = st.columns(2)
    col1.metric("Total Sales", f"${filtered_df['Sales'].sum():,.2f}")
    col2.metric("Total Profit", f"${filtered_df['Profit'].sum():,.2f}")

    st.subheader("Top 5 Customers by Sales")
    top_5 = filtered_df.groupby('Customer Name')['Sales'].sum().nlargest(5).reset_index()
    fig = px.bar(top_5, x='Customer Name', y='Sales', color='Sales', 
                 color_continuous_scale='Mint', template='plotly_white')
    st.plotly_chart(fig, width='stretch')
else:
    st.error("No data found for this combination!")
