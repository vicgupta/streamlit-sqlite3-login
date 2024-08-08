import streamlit as st
import smtplib
from email.mime.text import MIMEText

# Taking inputs
email_sender = st.text_input('From')
email_receiver = st.text_input('To')
subject = st.text_input('Subject')
body = st.text_area('Body')
password = st.text_input('Password', type="password") 

if st.button("Send Email"):
    try:
        msg = MIMEText(body)
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg['Subject'] = subject

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_sender, password)
        server.sendmail(email_sender, email_receiver, msg.as_string())
        server.quit()

        st.success('Email sent successfully! 🚀')
    except Exception as e:
        st.error(f"Error in sending email: {e}")