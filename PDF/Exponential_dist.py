import numpy as np
from scipy.stats import expon
from matplotlib import pyplot
from plotly import figure_factory as ff
import streamlit as st

def app():
    st.markdown("# Exponential Distribution")
    st.markdown("### Interactive View")
    st.sidebar.title("Input Selection")

    np.random.seed(40)

    original=expon.rvs(scale=1/5,size=1000)
    input_lambda=st.sidebar.slider("Parameter",1,20,value=10)
    changed=expon.rvs(scale=1/input_lambda,size=1000)

    hist=st.sidebar.checkbox("Histogram",value=False)
    curve=st.sidebar.checkbox("PDF Curve",value=True)

    fig=ff.create_distplot([original,changed],group_labels=["Original","Changed"],show_curve=curve,show_hist=hist,show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=800)

    st.plotly_chart(fig)

    col1,col2=st.columns(2)

    with col1:
            st.subheader("Descriptive Statistics for Original Data")
            st.write("Parameter: ",5)
            st.write("Mean: ",np.mean(original))
            st.write("Standard Deviation: ",np.std(original))
            st.write("Max: ",np.max(original))
            st.write("Min: ",np.min(original))

    with col2:
            st.subheader("Descriptive Statistics for Changed Data")
            st.write("Parameter: ",input_lambda)
            st.write("Mean: ",np.mean(changed))
            st.write("Standard Deviation: ",np.std(changed))
            st.write("Max: ",np.max(changed))
            st.write("Min: ",np.min(changed))

    st.subheader("Change in Parameter(λ):")
    st.text("=> When λ is large, the mean(1/λ) decreases, indicating that the expected\nwaiting time between events is shorter and which implies events occur more\nfrequently,the exponential distribution becomes more peaked and concentrated around zero.\nAs λ increases, the variance decreases, meaning that the\ndistribution becomes more concentrated around the mean.")
    st.text("=> When λ is small, the distribution is more spread out. This implies that\nevents occur less frequently, and the waiting times between events are\nlonger. ")
