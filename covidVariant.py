# - *- coding: utf-8 -*-

"""
@author: Diego 

"""
import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('covid-variants.csv')

countries = list(df['location'].unique())
variants = list(df['variant'].unique())


df['date'] = pd.to_datetime(df['date'], yearfirst= True)

country = st.sidebar.selectbox('Selecione o país', ["Todos"] + countries)

variant = st.sidebar.selectbox('Selecione a variante', ["Todas"] + variants)

if(country != 'Todos'):
    st.header( country)
    df = df[df['location'] == country]
else:
    st.header('Resultado para todos os países')
    

if(variant != 'Todas'):
    st.text('Resultado para a variante ' + variant)
    df = df[df['variant'] == variant]
else:
    st.text('Resultado para todas as variantes')

dfShow = df.groupby(by = ['date']).sum()

fig = px.line(dfShow, x=dfShow.index, y='total', markers=True)
fig.update_layout(
    title='Casos diários de covide-19 por tipo de variante', 
    xaxis_title='Data', 
    yaxis_title='Número de Casos',
    template = 'plotly_white',
    plot_bgcolor = 'white',
    font = {'family': 'Arial','size': 16,'color': 'black'})
fig.update_traces(textposition="bottom right")
st.plotly_chart(fig, use_container_width=True)

tableCovid = pd.DataFrame(df.groupby(by = ['location']).sum(), columns=['total'])

st.table(tableCovid)