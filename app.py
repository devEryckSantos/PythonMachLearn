import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

model = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

model.fit(x, y)

st.title("Prevendo o valor de uma pizza")
st.divider()

diameter = st.number_input("Digite o tamanho do diâmetro da pizza: ")

if diameter:
    predicted_price = model.predict([[diameter]])[0][0]
    st.write(f"A pizza com o diâmetro {diameter:.2f}cm custa R$ {predicted_price:.2f}.")
