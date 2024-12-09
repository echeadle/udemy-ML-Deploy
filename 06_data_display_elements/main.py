import streamlit as st 
import pandas as pd 

df = pd.read_csv("data/sample.csv", dtype="int")

# dataframe has additional capabilites, like sorting columns
st.dataframe(df)

# write is generic, usually better to use dataframes.
st.write(df)

# static tables if you do not want the extra capabilites
# such as sorting.
# also apperance is different. Sizing seems  to occur.
st.table(df)

# metric values

st.metric(label="Population", value=900, delta=20, delta_color="normal")
st.metric(label="Population", value=900, delta=-20, delta_color="normal")
st.metric(label="Expenses", value=900, delta=20, delta_color="inverse")

