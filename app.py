# Streamlit app 
import pandas as pd
import streamlit as st 
from sklearn.cluster import KMeans
from elbow import get_optimum_k

# Page Configuration 
st.set_page_config(page_title="Customer Segmentation", page_icon="Images/logo (1).png")

# Sidebar
with st.sidebar:
    st.title("Customer Segmentation")
    st.image("Images/logo (1).png")

# File uploader
file = st.file_uploader("Upload Dataset: ", type=["csv", "xlsx"])

if file:
    ext = file.name.split(".")[-1]
    if ext =="csv":
        df = pd.read_csv(file)
    elif ext =="xlsx":
        df = pd.read_excel(file)
    else:
        st.error("Un-Supported Extension")
    columns = st.multiselect("Select festures: ",
                             options=df.columns,
                             default=["Annual Income (k$)","Spending Score (1-100)"])
    df = df[columns]

    # Model Training
    K = get_optimum_k(df)
    model = KMeans(n_clusters=K, random_state=42)
    model.fit(df)
    df["labels"]= model.labels_
    df

    # Scatter Chart 
    st.scatter_chart(x="Annual Income (k$)",
                     y="Spending Score (1-100)",
                     data=df, 
                     color="labels")
    