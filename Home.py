import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title("VVKo")
    content = """
    Привіт! Мене звати Володимир, 
    я викладач курсу "Алгоритмізація та програмування". 
    Програмую на Python, C++ та JavaScript і допомагаю студентам 
    освоювати основи програмування та алгоритмізації 
    для вирішення реальних завдань і розвитку практичних навичок.
    """
    st.info(content)

content2 = """
Нижче ви зможете знайти деякі додатки створені мовою програмування Python.
"""

st.text(content2)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv('data.csv', sep=";")


with col3:
    for index, row in df[:5].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/'+row['image'])
        url = 'https://github.com/' if row['url'] is None else row['url']
        st.write(f"[Source code]({url})")

with col4:
    for index, row in df[5:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        url = 'https://github.com/' if row['url'] is None else row['url']
        st.write(f"[Source code]({url})")
