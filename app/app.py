
import math
import pandas as pd
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt
from technical import func
from sentiment import parapluie
from annotated_text import annotated_text
import nltk 


nltk.download('vader_lexicon')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.set_page_config(layout="wide")
with st.container():
    st.title('PARAPLUIE')
    st.code('Enter Stock Ticker, Default Value is AAPL')
    ticker = st.text_input(label='Ticker',value='AAPL')

col1, col2 = st.columns((2,2))

with col1:
 
    st.title("Sentiment Analysis")
    df=parapluie(ticker)
    st.caption("Values are calculated as a sum of positive and negative . When a compound is close to 1 , it is considered postive, and below 0, it is negative. Check the Analysis Chart to see the compound values for each dates")
    sum = 0
    for flag in range(10):
        val1 = df.iloc[[flag]]['compound'].tolist()
        sum = sum +val1[0]
        sum = sum/10
        mainsum = str(sum) + "%"
    with st.expander("Based on avg. compound values from the latest(10) news"):
        if(sum>0.5):
                st.subheader(mainsum)
                st.success('Positive ⬆️')
        elif(sum<0.5 and sum>0):
                st.subheader(mainsum)
                st.success("Towards Positive ⬆️")
        elif(sum<0):
                st.subheader(mainsum)
                annotated_text(    
                    ("Towards", "Negative"))
        else:
                st.subheader(mainsum)
                annotated_text(
                        ("Performing", "Neutrally"))
    with st.expander("Based on the latest news"):
        for flag in df.iloc[[0]]['compound']:
            val= (flag/1)*100 
            percent = str(val)+ "%"
            if(flag>0.5):
                st.subheader(percent)
                st.success('Positive ⬆️')
            elif(flag<0.5 and flag>0):
                st.subheader(percent)
                st.success("Towards Positive ⬆️")
            elif(flag<0):
                st.subheader(percent)
                annotated_text(
                        
                        ("Towards", "Negative"))
            else:
                st.subheader(percent)
                annotated_text(
                        ("Performing", "Neutrally"))
    st.subheader('Data from FINVIZ')
    with st.expander("Chart"):
        plt.style.use('dark_background')
        mean_df = df.groupby(['ticker', 'date']).mean().unstack()
        mean_df = mean_df.xs('compound', axis="columns")
        mean_df.plot(kind='bar')
        st.pyplot(plt)
    startdate = df.iloc[[0]]['date'].tolist()
    enddate = df.iloc[[-1]]['date'].tolist()
    string="Compound Values till " + str(enddate[0])
    with st.expander(string):
        st.dataframe(df[['date','title','compound']])
    st.write("Data from:",startdate[0],enddate[0])
with col2:
    st.title("Technical Analysis")
    st.caption("Based on GoldenCross/DeathCross Strategy")
    st.markdown('Read more about  **[Golden Cross](https://www.investopedia.com/terms/g/goldencross.asp)** , '
                ' '
                '**[Death Cross](https://www.investopedia.com/terms/d/deathcross.asp)**')
    st.subheader('Prediction Graph')
    st.write('Red marker indicates Sell 💸 and  Green marker indicates Buy 🛒')
    df = func(ticker)
    st.pyplot(df)
   