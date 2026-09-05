import streamlit as st
import pandas as pd
import numpy as np


st.title("k-Nearest Neighbors - Build & Deploy (streamlit)")
st.subheader('K-Nearest Neighbors With Sifat Ahmed Tamim')
st.sidebar.header('Dataset & Preprocessing')

from sklearn.datasets import load_iris,load_wine,load_breast_cancer
def load_sample(name):
  if name == 'Sample dataset (Iris)':
    df = load_iris(as_frame= True)
  elif name == 'Sample dataset (Wine)':
    df = load_wine(as_frame=True)
  elif name == 'Sample dataset (Breast Cancer)':
    df = load_breast_cancer(as_frame = True)
  else:
    return None
  df= pd.concat([df.frame.reset_index(drop=True)],axis=1)
  return df

data_source = st.sidebar.selectbox('Data source',['Upload CSV','Sample dataset(Iris)','Sample dataset(Wine)','Sample dataset(Breast cancer)'])

if data_source =='Upload CSV':
  uploaded = st.sidebar.file_uploader('Upload CSV', type=['csv', 'txt'])
  if uploaded is not None:
    try:
      df = pd.read_csv(uploaded)
      df = df.dropna()
      st.success('Loaded Sample Data')
    except Exception as e:
      st.sidebar.error(f'couldnot read file:{e}')
      
    
  else:
    st.info('Upload CSV on the left or a sample dataset get started')
    st.stop()

else:
  df = load_sample(data_source)


st.write('## Dataset Preview')
st.write(df.head())








