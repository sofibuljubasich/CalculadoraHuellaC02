import streamlit as st
import pandas as pd
from constantes import FACTORES

lista_factores = FACTORES

def calcula_huella(*arguments):
    """
    Esta función calcula la huella de carbono
    Parameters
    ----------
    *arguments: int 
        Lista con los consumos por categoría
    """
    totalSum = 0
    for(number,factor) in zip(arguments,lista_factores):
        totalSum += number*factor

    return totalSum        
 

st.title("Calculadora Huella de Carbono :earth_americas:")


st.write("Ingresa tus datos de consumo")

with st.form("my_form"):
   st.write("Inside the form")
   km_auto_gas = st.number_input("KM en automóvil gasoil")
   km_auto_die = st.number_input("KM en automóvil diesel")
   km_auto_elec = st.number_input("KM en automóvil eléctrico")
   km_auto_gnc = st.number_input("KM en automóvil gnc")
    
   km_moto_gas = st.number_input("KM en moto gasoil")

   km_camion_liviano_die = st.number_input("KM en camión liviano diésel")
   
   km_colect_die = st.number_input("KM en colectivo diésel")
   km_colect_gas = st.number_input("KM en colectivo gasoil")

   km_subte = st.number_input("KM en Subte")

   submitted = st.form_submit_button("Calcular")

   huella = calcula_huella(km_auto_gas,km_auto_die,km_auto_elec,km_auto_gnc,km_moto_gas,km_camion_liviano_die,km_colect_gas)
   
if submitted:
       st.write("Tu huella de carbono es:", huella)
    



