import streamlit as st 
import time
from googlesearch import search
import csv
import json
import requests
from bs4 import BeautifulSoup


src = st.text_input("Source")
keyw = st.text_input("Keyword")


query = "site:"+src+" "+keyw
results = search(query, num_results=1)

channels = []
for result in results:
    html = requests.get(result).text
    soup = BeautifulSoup(html, 'html.parser')
    channel_link = soup.select_one("a[href*=channel][href*=user]").get('href')
    time.sleep(3)
    if channel_link:
        channels.append(channel_link)


st.dataframe(channels)


