import streamlit as st
import librería_funciones as lf

st.title("Paradigmas de la programación")

st.sidebar.image("UCG.png")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Carlos Carrillo")

capital = st.number_input("Ingrese el capital")
tasa_anual_pct = st.number_input("Ingrese de la tasa anual")
dias_mora = st.number_input("Ingrese los días de mora")


resultado = lf.calcular_interes_mora()
