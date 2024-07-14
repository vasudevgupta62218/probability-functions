import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
from plotly import figure_factory as ff



st.set_page_config(page_title="Visualization",page_icon="logo.png",layout="wide",initial_sidebar_state='auto')
st.markdown("#  Gaussian Distribution")
st.markdown('### Interactive View')

np.random.seed(42)
original=np.random.normal(0,1,10000)

st.sidebar.title("Input Selection")
mean=st.sidebar.slider(label='Mean',min_value=-20,max_value=20,value=1) #value=> default value
std=st.sidebar.slider(label="Standard Deviation",min_value=0.1,max_value=10.0,value=2.0,step=0.1)

curve=st.sidebar.checkbox("PDF Curve",value=True)
hist=st.sidebar.checkbox("Histogram",value=True)

sample_data=np.random.normal(loc=mean,scale=std,size=10000)
fig=ff.create_distplot([original,sample_data],group_labels=['Original','Changed'],show_curve=curve,show_hist=hist,show_rug=False)
fig.update_layout(autosize=False,width=1000,height=800)

st.plotly_chart(fig)
col1,col2=st.columns(2)
with col1:
    st.subheader("Descriptive Statistics for Original Data")
    st.write("Mean: ",np.mean(original))
    st.write("Standard Deviation: ",np.std(original))
    st.write("Max: ",np.max(original))
    st.write("Min: ",np.min(original))

with col2:
    st.subheader("Descriptive Statistics for Changed Data")
    st.write("Mean: ",np.mean(sample_data))
    st.write("Standard Deviation: ",np.std(sample_data))
    st.write("Max: ",np.max(sample_data))
    st.write("Min: ",np.min(sample_data))


st.subheader("Change in Mean: ")
st.text(" The entire distribution shifts horizontally along the x-axis.\n The shape (bell curve), spread (standard deviation), and symmetry remain unchanged.")

st.subheader("Change in Standard Deviation: ")
st.text(" Increasing the standard deviation makes the distribution wider (more spread out), while\n decreasing it, makes the distribution narrower (less spread out).\n It does not change the bell-shaped and symmetric nature of the distribution.")
