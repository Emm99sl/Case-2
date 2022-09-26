#!/usr/bin/env python
# coding: utf-8

# In[2]:


#pip install streamlit


# In[5]:


import streamlit as st
import pandas as pd
import numpy as np


# In[6]:


HairEye = pd.read_csv("HairEyeColor.csv")


# In[7]:


st.title("Hair Eye Colour Database")


# In[8]:


InputHair = st.sidebar.selectbox("Select Hair Colour", ("Brown", "Black", "Blond", "Red"))


# In[12]:


HairEyeSelect = HairEye[HairEye["Hair"] == InputHair]


# In[13]:


st.dataframe(HairEyeSelect)

