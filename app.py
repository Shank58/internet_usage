import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide', page_title='Internet Usage Dashboard')

st.header('Internet Usage Dashboard')

df = pd.read_csv('share-of-individuals-using-the-internet.csv')
df = df[(df['Year'] >= 2000) & (df['Year'] <= 2016)] # get just years 2000 to 2016

# get unique values
countries = df['Country'].unique()
years = df['Year'].unique()
years.sort()

# create variable for year selection
selected_year = st.selectbox(label='Years',
                             options=years)

# create data frame for selected year
df_plot = df[df['Year'] == selected_year]

# create charts
choropleth = px.choropleth(data_frame=df_plot,
                     locations='Country',
                     locationmode='country names',
                     color='Individuals using the Internet (% of population)',
                     color_continuous_scale=px.colors.sequential.YlGnBu,
                     title=f'Internet Usage % by Country for Year {selected_year}')

hist1 = px.histogram(data_frame=df_plot,
                    title=f'Distribution of Internet Usage by Country for Year {selected_year}',
                    x='Individuals using the Internet (% of population)'
                    )

# create columns to place charts into
col1, col2 = st.columns([2, 1])

# add charts to columns
col1.plotly_chart(choropleth)
col2.plotly_chart(hist1)

