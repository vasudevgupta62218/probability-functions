import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
import  plotly.figure_factory as ff

def app():
    st.markdown("# Binomial Distribution")
    st.markdown("#### Interactive view")

    st.sidebar.title("Input Selection")

    original=np.random.binomial(10,0.5,300)

    n=st.sidebar.slider("n:",min_value=1,max_value=80,step=1,value=20)
    p=st.sidebar.slider("p: ",min_value=0.1,max_value=1.0,step=0.10,value=0.5)

    changed=np.random.binomial(n,p,size=300)

    hist=st.sidebar.checkbox("Histogram",value=True)
    curve=st.sidebar.checkbox("PDF",value=True)

    fig=ff.create_distplot([original,changed],["Original","Changed"],show_hist=hist,show_curve=curve,show_rug=False)
    fig.update_layout(autosize=False,height=1000,width=1200)

    st.plotly_chart(fig)

    col1,col2=st.columns(2)

    with col1:
            st.subheader("Descriptive Statistics for Original Data")
            st.write("n: ",10)
            st.write("p: ",0.5)
            st.write("Mean: ",np.mean(original))
            st.write("Standard Deviation: ",np.std(original))


    with col2:
            st.subheader("Descriptive Statistics for Changed Data")
            st.write("n: ",n)
            st.write("p: ",p)
            st.write("Mean: ",np.mean(changed))
            st.write("Standard Deviation: ",np.std(changed))


    st.subheader("Changed in parameter(n) ")
    st.text("When n is small, the binomial distribution is skewed and discrete, reflecting\nthe fact that with fewer trials, the outcomes are more likely to be either\nall successes or all failures.")
    st.text("Larger n generally reduces the probability of extreme outcomes (either very few\nor many successes) and increases the probability of outcomes around the mean.")
    st.text("Changing n, primarily affects the mean, variance, and shape of the distribution.\nLarger n values lead to distributions that are more concentrated around the mean,\nless variable, and more closely approximate a normal distribution shape.")

    st.subheader("Changed in parameter(p) ")
    st.text(" Increases p shifts the distribution to the right (more successes expected),\ndecreases p shifts it to the left.")
    st.text("When p is close to 0 or 1, the distribution becomes more skewed. For example,\nIf p is close to 1, the distribution will be skewed to the left because most\noutcomes will be successes. When p is close to 0.5, the distribution is more\nsymmetric and bell-shaped, resembling normal distribution,specially as n increases.")
    st.text("Increasing p increases probabilities of higher successes\nDecreasing p increases probabilities of lower successes.")
