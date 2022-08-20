# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import streamlit as st
import pandas as pd



data = pd.read_csv('C:/Users/HP/CDA.AI/week 4/AirPassengers.csv')
print (data)



def main():
    st.title('Air Passengers Analysis')
    #read data file
    data = pd.read_csv ('AirPassengers.csv')
    
    #obtain year from date
    data ('Year') = data('Month').apply(lambda x: x.split('-')[0])
    
    #show unique years
    year = st.selectbox('Select year', data['Year'].unique())
    #button 
    button = st.button('Show results')
    if button:year
        #if button is pressed, subset data on selected 
        subset = data[data['Year'] == year]
        # show subset table
        st.table(subset)
#if  __name__ == '__main__':
    #main()

