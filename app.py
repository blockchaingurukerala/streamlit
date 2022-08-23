import streamlit as st
import pickle

st.title("Iris Flower Ml Deployment")
st.write("Decision Tree")

sl = st.slider('Sepal Length',4.3,7.9,5.0)
sw = st.slider('Sepal Width',2.0,4.4,3.0)
pl = st.slider('Petal Length',1.0,6.9,5.0)
pw = st.slider('Petal Width',0.1,2.5,2.3)

label = ['setosa','versicolor','virginica']


model = pickle.load(open('output.pkl','rb'))

op = model.predict([[sl,sw,pl,pw]])
op = label[op[0]]

st.title(f'The flower species is {op}')
