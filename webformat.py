import streamlit as st
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Read data
dt = pd.read_csv('budget_allocation_opinion.csv')

my_page = st.sidebar.radio('Page Navigation', ['page 1', 'page 2', 'page 3','page 4'])

if my_page == 'page 1':
    st.title("city budget opinion")
    st.header("favored sector")
    st.markdown('introduction Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ligula magna, pulvinar non pretium eu, venenatis vestibulum orci. Sed non luctus nisl. Nulla facilisi. Duis ultrices, dolor vel porta hendrerit, mauris justo finibus diam, semper faucibus urna tellus id nibh. Mauris facilisis arcu massa, ut molestie nunc scelerisque in. Nullam nisi lorem, blandit a est vel, aliquet viverra augue. Interdum et malesuada fames ac ante ipsum primis in faucibus. Duis interdum ante ut orci condimentum, at scelerisque augue consequat. Praesent convallis pretium nisl. Etiam velit tellus, hendrerit sit amet rhoncus sed, convallis non mi. Sed sodales molestie augue, in pharetra elit dictum ut. Integer sodales sit amet ex non auctor.',unsafe_allow_html=False)
    
elif my_page == 'page 2':
    st.title("city budget opinion")
    st.header("favored sector")
    fig = plt.figure(figsize=(8,8))
    dt['favored_sector'].value_counts()
    fav_sector = dt['favored_sector'].value_counts()
    plt.title("favored sectors", fontsize=14)
    plt.pie(fav_sector,labels=['health','education','green initiatives','infrastructure'],autopct='%1.1f%%',startangle=90)
    
    st.pyplot(fig)
    
elif my_page == 'page 3':
    st.title("city budget opinion")
    st.header("unfavored sector")
    fig = plt.figure(figsize=(8,8))
    dt['unfavored_sector'].value_counts()
    unfav_sector = dt['unfavored_sector'].value_counts()
    plt.title("unfavored sectors", fontsize=14)
    plt.pie(unfav_sector,labels=['security','green initiatives','infrastructure','universal basic income'],autopct='%1.1f%%',startangle=90)
    plt.show()
    
    st.pyplot(fig)

    
elif my_page == 'page 4':
    fig = plt.figure(figsize=(8,8))
    workforce = dt['workforce_group'].value_counts()
    workforce.plot.barh()
    st.pyplot(fig)