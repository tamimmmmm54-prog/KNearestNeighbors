import streamlit as st
import pandas as pd
import numpy as np


st.title("k-Nearest Neighbors - Build & Deploy (streamlit)")
st.subheader('K-Nearest Neighbors With Sifat Ahmed Tamim')
st.sidebar.header('Dataset & Preprocessing')

from sklearn.datasets import load_iris,load_wine,load_breast_cancer
def load_sample(name):
  if name == 'Iris':
    df = load_iris(as_frame= True)
  elif name == 'Wine':
    df = load_wine(as_frame=True)
  elif name == 'Breast canccer':
    df = load_breast_cancer(as_frame = True)
  else:
    return None
  df= pd.concat[df.frame.reset_index(drop=True),axis=1]
  return df

data_sourrce = st.sidebar.selectbox['Upload Dataset','Sample Dataset(Iris)','Sample Dataset(Wine)','Sample Dataset(Breast cancer)]














