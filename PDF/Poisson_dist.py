import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import streamlit as st

def app():
    st.markdown("# Poisson Distribution")
    st.markdown("### Interactive View")
    st.sidebar.title("Input Selection")

    np.random.seed(40)
    original=np.random.poisson(5,size=1000)
    lamda=st.sidebar.slider(label="Parameter",min_value=0,max_value=20,value=10)
    changed=np.random.poisson(lam=lamda,size=1000)

    hist=st.sidebar.checkbox(label="Histogram",value=True)
    curve=st.sidebar.checkbox(label="PDF Curve",value=True)

    fig=ff.create_distplot([original,changed],group_labels=["Original","Changed"],show_hist=hist,show_curve=curve,show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=800)

    st.plotly_chart(fig)
    col1,col2 =st.columns(2)

    with col1:
        st.subheader("Descriptive Statistics for Original Data")
        st.write("Parameter: ",5)
        st.write("Mean: ",np.mean(original))
        st.write("Standard Deviation: ",np.std(original))
        st.write("Max: ",np.max(original))
        st.write("Min: ",np.min(original))

    with col2:
        st.subheader("Descriptive Statistics for Changed Data")
        st.write("Parameter: ",lamda)
        st.write("Mean: ",np.mean(changed))
        st.write("Standard Deviation: ",np.std(changed))
        st.write("Max: ",np.max(changed))
        st.write("Min: ",np.min(changed))


    st.subheader("Change in Parameter(λ):")
    st.text("-> When λ is small, the distribution is skewed right (positively skewed), meaning\nit has a longer tail on the right side.\nAs λ increases, the distribution becomes more symmetric and bell-shaped.")
    st.text("-> For smaller λ values,the probabilities of observing larger numbers of events\ndecrease rapidly.\nFor larger λ values,the probabilities of observing larger numbers of events\ndecrease less rapidly.")
    st.text("-> As λ approaches infinity, the Poisson distribution approaches normal distribution\nwith mean λ and variance λ.\nThis is a consequence of the central limit theorem.")
