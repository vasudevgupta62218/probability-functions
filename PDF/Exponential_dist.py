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

    original=expon.rvs(scale=5,size=1000)
    input_lambda=st.sidebar.slider("Parameter",1,20,value=10)
    changed=expon.rvs(scale=input_lambda,size=1000)

    hist=st.sidebar.checkbox("Histogram",value=False)
    curve=st.sidebar.checkbox("PDF Curve",value=True)

    fig=ff.create_distplot([original,changed],group_labels=["Original","Changed"],show_curve=curve,show_hist=hist,show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=800)

    st.plotly_chart(fig)

    col1,col2=st.columns(2)

    with col1:
            st.subheader("Descriptive Statistics for Original Data")
            st.write("Parameter: ",5)
            st.write("Mean: ",1/5)
            st.write("Standard Deviation: ",1/5)
            st.write("Max: ",np.max(original))
            st.write("Min: ",np.min(original))

    with col2:
            st.subheader("Descriptive Statistics for Changed Data")
            st.write("Parameter: ",input_lambda)
            st.write("Mean: ",1/input_lambda)
            st.write("Standard Deviation: ",1/input_lambda)
            st.write("Max: ",np.max(changed))
            st.write("Min: ",np.min(changed))

    st.subheader("Change in Parameter(λ):")
    st.text(" Consider λ as waiting time ")
    st.text("=> As λ increases, the average waiting time also increases,then there will be the\n chances for the higher average time also. And the curve will be\nflatter and more stretched due to this.")
    st.text("=> When λ is small, the PDF is relatively steep, indicating that values of x\nfarther from zero are less probable.Decreasing λ makes\nthe PDF steeper and more concentrated near 0.")
