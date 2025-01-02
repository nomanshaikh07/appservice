import pandas as pd
import streamlit as st
st.write('Welcome to AVD 1234')
data = {
    "Task": ["Extract", "Transform", "Load"],
    "Status": ["Completed", "InProgress", "Pending"]
}
df = pd.DataFrame(data)
st.write("ETL Processing Status : ", df)
