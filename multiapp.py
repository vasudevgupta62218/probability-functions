import streamlit as st

class Multiapp:

    def __init__(self):
        st.set_page_config(page_title="Vizualization",page_icon="logo.png",layout='wide',initial_sidebar_state='auto')
        self.apps=[]

    def add_app(self,title,func):
        self.apps.append({
            "title":title,
            "function":func
        })

    def run(self):
        app=st.sidebar.selectbox("Select Distribution",self.apps,format_func=lambda app:app["title"])
        app['function']()
