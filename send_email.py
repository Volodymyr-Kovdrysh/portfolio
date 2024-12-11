import smtplib, ssl
import os

def send_email(message):

    username = 'v.kovdrysh@chnu.edu.ua'
    password = os.environ['PASSWORD']

    host = "smtp.gmail.com"
    port = 465

    receiver = 'v.kovdrysh@chnu.edu.ua'
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username,receiver,message.encode('utf-8'))

if __name__ == '__main__':
    send_email('hi')