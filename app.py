import streamlit as st
from multiapp import Multiapp
from PDF import Poisson_dist,Normal_dist,Binomial_dist

app=Multiapp()
app.add_app("Poisson Distribution",Poisson_dist.app)
app.add_app("Normal Distribution",Normal_dist.app)
app.add_app("Binomial Distribution",Binomial_dist.app)

app.run()
