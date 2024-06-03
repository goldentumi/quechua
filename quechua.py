# -*- coding: utf-8 -*-

# leemos el Excel


import pandas as pd
verbos = pd.read_excel("quechua.xlsx")

##diccionario

quechua = list(verbos['quechua'])
español = list(verbos['español'])

dict_que_esp = dict(zip(quechua,español))

#importamos streamlit

import streamlit as st

option = st.selectbox(
    "Selecciona un verbo en quechua", quechua)

st.write("La traducción es:", dict_que_esp[option])


#variable persona
persona = ['primera inclusiva', 'primera exclusiva', 'segunda', 'tercera']
option1 = st.selectbox(
    "Selecciona la persona", persona)


#variable número
numero = ['singular','plural']
option2 = st.selectbox(
   "Selecciona el número", numero)

#st.write("La conjugación es:", dict_que_esp[option] + ' ' + diccionario[option1][option2][option3])
