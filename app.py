import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Nao sei o nome")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write(df)

number = st.number_input("Intervalo de Amostragem", value=1,
                         placeholder="Digite o numero de linhas")
st.write('O intervalo atual e ', number)

df2 = df.iloc[np.arange(0, len(df), number).tolist()]

st.write(df2)

fig = px.line(df2, x="Time", y="StrainPercent")

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

fig2 = px.scatter(df2,  x="Time", y="StrainPercent", log_x=False)

st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
