# To install steamlit write => pip install streamlit
# To run this go to the termial and type => streamlit run mian.py

# Dependency

import streamlit as st
import pandas as pd
import openapi_helper

col1,col2 = st.columns([3,2])

with col1:
    st.title("Financial Data Extraction Tool")
    news_article = st.text_area('Paste your financial news article here', height = 300)
    if st.button('Extract'):
       financial_data_df =  openapi_helper.extract_financial_data(news_article)

with col2:

    st.markdown('<br/>'*6, unsafe_allow_ntml=True) # Create 5 lines of vertical space

    data = {
            'Measures':['Company Name','Revenue','EPS']
            'Values'  :['Apple','12.34 $ ','56.45 $'
    }
    df = pd.DataFrame(data)
    st.dataframe(financial_data_df,hide_index= True)











# Streamlit app layout
st.title("Financial Data Extraction Tool")
st.write("Enter the news article and click on 'Extract' to extract company information ")

# Text input for the news article
article = st.text_area('News Article',height = 300)

# Button to extract information
if st.button('Extract'):
    if article:
        # Extract Company Information
        company_name, revenue, eps = extract_company_info(article)

        #create pandas DataFrame to extracted information
        data = {
            'Measures':['Company Name','Revenue','EPS']
            'Values'  :[company_name,revenue,eps]
        }
        df = pd.DataFrame(data)

            # Display the table
            st.table(df)
    else:
        st.warning("Please Enter the a News article: ")


