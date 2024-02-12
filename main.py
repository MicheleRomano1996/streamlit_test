# python -m streamlit run main.py

import pandas as pd
import streamlit as st
import json

# config
all_text = ""

# page style
st.markdown('<div style="text-align:center"><h1>File Reader (csv, txt, json)</h1></div>', unsafe_allow_html=True)

# style CSS
st.markdown(
    """
    <style>
    .styled-border {
        border: 2px solid #ddd; /* Set border color and width */
        padding: 10px; /* Add padding to the content inside the border */
        border-radius: 5px; /* Add rounded corners */
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# upload csv file
uploaded_file = st.file_uploader("Upload a file",label_visibility='hidden', type=['csv','txt','json','py'])
st.divider()

if uploaded_file is not None:

    # file csv
    if uploaded_file.type == 'text/csv':
        df = pd.read_csv(uploaded_file)
        columns = list(df.columns)
        
        # colonna Unnamed: 0 -> indice
        if 'Unnamed: 0' in columns:
            df.rename(columns={'Unnamed: 0': 'indice'}, inplace=True)
            df.set_index('indice', drop=True, inplace=True)

        st.write('<div style="text-align:center"><h3>Contenuto File CSV</h3></div>', unsafe_allow_html=True)
        st.table(df)
        
        st.divider()

    # file txt
    elif uploaded_file.type == 'text/plain':
        txt_data = uploaded_file.read().decode('utf-8')
        txt_data = txt_data.replace('\r', '')
        sections = [section.strip() for section in txt_data.split('\n') if section.strip()]
        for section in sections:
            all_text += section + "<br>" + "<br>" 
            bordered_text = section
        st.write('<div style="text-align:center"><h3>Contenuto File TXT</h3></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="styled-border">{all_text}</div>', unsafe_allow_html=True)
        st.divider() 

    # file json
    elif uploaded_file.type == 'application/json':
        json_data = json.load(uploaded_file)
        st.write('<div style="text-align:center"><h3>Contenuto File JSON</h3></div>', unsafe_allow_html=True)
        st.json(json_data)
    
    elif uploaded_file.type == 'application/octet-stream':
        python_code = uploaded_file.read().decode('utf-8')
        st.markdown("```python\n" + python_code + "\n```")
    else:
        st.warning('You need to upload a CSV, TXT or JSON file!')