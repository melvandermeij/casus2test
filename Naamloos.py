#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import streamlit as st

import plotly.express as px


# In[2]:


header_container = st.container()
data_container = st.container()


# In[3]:


with header_container:
    
    st.image('fiets.png')
    st.title('Welkom bij Casus 2')
    st.header('Op deze pagina gaan we kijken naar de verkopen van fietsen vanuit Europa')


# In[4]:


with data_container: 
    df = pd.read_csv("Sales.csv")


# In[5]:


df = df.drop(['Profit', 'Cost', 'Revenue'], axis =1)


# In[6]:


df['Total_Cost'] = df['Order_Quantity'] * df['Unit_Cost']
df['Revenue'] = df['Order_Quantity'] * df['Unit_Price']
df['Profit'] = df['Revenue'] - df['Total_Cost']
df.head(2)


# In[7]:


st.write(df.head(8))


# In[8]:


country_options= df['Country'].unique().tolist()
country= st.selectbox("Welk land zou je willen zien?", country_options,0)
df= df[df['Country']==country]

fig2 = px.histogram(df, x='Date', y='Revenue', color='Product_Category')
fig2.update_layout(title="Reveneu per product category in years")
fig2.update_xaxes(title_text="Date in years")
fig2.update_yaxes(title_text="Revenue in millons")
st.write(fig2)


# In[14]:


year_options= df['Year'].unique().tolist()
year=st.selectbox("Welk jaar wil je zien?", year_options)

fig3 = px.histogram(df, x='Product_Category', y='Profit', color='Age_Group', animation_frame='Year')
fig3.update_layout(
    title="Global profit by age group of product category",
    legend_title="Age group",
    xaxis_title="Product category",
    yaxis_title="Profit")
st.write(fig3)


# In[ ]:





# In[15]:


check = st.checkbox("klik hier als je fietsen leuk vind")
st.write('Ik vind fietsen leuk:', check)

if check:
    st.write(":smile:"*5)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[10]:


#country_options= df['Country'].unique().tolist()
#country= st.selectbox("Welk land zou je willen zien?", country_options,0)
#df= df[df['Country']==country]

#fig= px.scatter(df, x="Year", y="Revenue",
            #   size="Order_Quantity", color="Country", 
            #   log_x=True)

#fig.update_layout(width=800)
#st.write(fig

