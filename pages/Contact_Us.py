import streamlit as st

from send_email import send_email

st.header("Зв'язатися зі мною")

with st.form(key='email_form'):
    user_mail = st.text_input("Введіть Вашу електронну адресу")
    raw_message = st.text_area("Ваше повідомлення")
    message = f"""\
Subject: Нове повідомлення від {user_mail}

Від: {user_mail}
{raw_message}
"""
    button = st.form_submit_button("Надіслати!")
    print(button)
    if button:
        send_email(message)
        st.info('Ваше повідомлення надіслано')


