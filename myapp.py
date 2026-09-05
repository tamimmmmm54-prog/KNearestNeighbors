import streamlit as st
import pandas as pd
import numpy as np


st.title("k-Nearest Neighbors - Build & Deploy (streamlit)")
st.subheader('K-Nearest Neighbors With Sifat Ahmed Tamim')
st.sidebar.header('Dataset & Preprocessing')

from sklearn.datasets import load_iris,load_wine,load_breast_cancer
def load_sample(name):
  if name == 'Sample Dataset(Iris)':
    df = load_iris(as_frame= True)
  elif name == 'Sample Dataset(Wine)':
    df = load_wine(as_frame=True)
  elif name == 'Sample Dataset(Breast cancer)':
    df = load_breast_cancer(as_frame = True)
  else:
    return None
  df= pd.concat([df.frame.reset_index(drop=True)],axis=1)
  return df

data_source = st.sidebar.selectbox('Data source',['Upload Dataset','Sample Dataset(Iris)','Sample Dataset(Wine)','Sample Dataset(Breast cancer)'])
if data_source =='Upload CSV':
  up_loaded = st.sidebar.file.uploader['Upload CSV',type= ['csv',''txt'])
else:
  df = load_sample(data_source)
  if uploaded is not None:
    try:
      df = pd.read_csv(Upoladed)
      df = df.dropna()
      st.success('Loaded Sample Data')
    except exception as e:
      st.sidebar.error(f'couldnot read file:{e}')
      
    
  else:
    st.info('Upload CSV on the left or a sample dataset get started')
    st.stop()












