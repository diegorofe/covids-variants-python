# - *- coding: utf-8 -*-

from distutils.errors import DistutilsGetoptError

"""
@author: Diego 

"""
import pandas as pd
import streamlit as st

df = pd.read_csv('covid-variants.csv')

countries = list(df['location'].unique())
variants = list(df['variant'].unique())


df['date'] = pd.to_datetime(df['date'], yearfirst= True)

st.sidebar.selectbox('Selecione o país', ["Todos"] + countries)

st.sidebar.selectbox('Selecione a variante', ["Todas"] + variants)



