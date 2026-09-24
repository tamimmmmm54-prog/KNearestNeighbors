import streamlit as st
import pandas as pd
import numpy as np


st.title("k-Nearest Neighbors - Build & Deploy (streamlit)")
st.subheader('K-Nearest Neighbors With Sifat Ahmed Tamim')
st.sidebar.header('Dataset & Preprocessing')

from sklearn.datasets import load_iris,load_wine,load_breast_cancer
def load_sample(name):
  if name == 'Sample dataset(Iris)':
    df = load_iris(as_frame= True)
  elif name == 'Sample dataset(Wine)':
    df = load_wine(as_frame=True)
  elif name == 'Sample dataset(Breast Cancer)':
    df = load_breast_cancer(as_frame = True)
  else:
      return None
  df= pd.concat([df.frame.reset_index(drop=True)],axis=1)
  return df

data_source = st.sidebar.selectbox('Data source',['Upload CSV','Sample dataset(Iris)','Sample dataset(Wine)','Sample dataset(Breast Cancer)'])

if data_source =='Upload CSV':
  uploaded = st.sidebar.file_uploader('Upload CSV', type=['csv', 'txt'])
  if uploaded is not None:
    try:
      df = pd.read_csv(uploaded)
      df = df.dropna()
      st.success('Loaded Sample Data')
    except Exception as e:
      st.sidebar.error(f'couldnot read file:{e}')
      st.stop()
    
  else:
      st.info('Upload CSV on the left or a sample dataset get started')
      st.stop()

else:
    df = load_sample(data_source)


st.write('## Dataset Preview')
st.write(df.head())


st.subheader('Data Preprocessing')

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
if len(numeric_cols) < 2:
  st.error('Need at least two nummeric columns for Knearest neighbors')
  st.stop()

target_cols = st.selectbox('Select Output Target Variable',numeric_cols)
features = [c for c in numeric_cols if c != target_cols]
st.multiselect('features (numeric)',options=features,default=features)

x = df[features].copy()
y = df[target_cols].copy()
st.sidebar.header('Preprocessing & Model')
scale_method = st.sidebar.selectbox('Scaling',['None', 'StandardScaler','MinMax Scaling'])
use_pca = st.sidebar.checkbox('Project to 2 components with PCA for vizualization',value=True)
text_size = st.sidebar.slider('Test set size (%)',min_value=5,max_value=50,value=20)
random_state = st.sidebar.number_input('Random seed',value = 42,step=1)
st.sidebar.subheader('KNN hyperparameter')
k = st.sidebar.slider('k(neighbors)',min_value=1,max_value=50,value=5)
weights = st.sidebar.selectbox('Weight function',['uniform','distance'])
metric = st.sidebar.selectbox('Distance metrics',['minkowski','euclidean','manhattan'])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=text_size/100.0,random_state=int(random_state))

from sklearn.preprocessing import StandardScaler, MinMaxScaler
if scale_method == 'StandardScaler':
  scaler = StandardScaler()
  X_train = pd.DataFrame(scaler.fit_transform(x_train), columns = features)
  X_test = pd.DataFrame(scaler.transform(x_test),columns = features)
elif scale_method == 'MinMax Scaling':
  scaler = MinMaxScaler()
  X_train = pd.DataFrame(scaler.fit_transform(x_train), columns = features)
  X_test = pd.DataFrame(scaler.transform(x_test),columns = features)
else:
  scealer = None

from sklearn.neighbors import KNeighborsClassifiers
clf = KneighborsClassifier(n_neighbors=int(k),weights = weights, metric = metric)
clf.fit(x_train,y_train)

from sklearn.metrics import accuracy_score, classification_report,confusion_metrix
y_pred = clf.predict(x_test)
acc = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict = True)
cm = confusion_Matrix(y_test, y_pred)
import matplotlib.pyplot as plt
st.write('##Model Evaluatio')
col1, col2 =st.columns([1, 1])
with col1:
  st.metric('Accuracy': f'{acc=3f}')
  st.write('##Classification report')
  st.dataframe(pd.DataFrame(report),transpose())

with col2:  
  st.write('##Confusion Metrix')
  fig, ax = plt.subplot()
  im = ax.mathshow()
  for (i,j), val in npndenumerate(cm):
    ax.text(i, j, int(val),ha='center',va= 'center')
  ax.set_xlabel('Predicted')
  ax.set_ylabel('Actual')
  st.pyplot(fig)





















