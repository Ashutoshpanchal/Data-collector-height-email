from email.mime.text import MIMEText
import smtplib


def send_email(email,height):
    from_email="ashutosh0215@gmail.com"
    from_password="spiderman02"
    to_email=email


    subject="Height Data"
    message="hey there, Your height is <b>%s</b>." % height

    msg = MIMEText(message,"html")
    msg["Subject"]=subject
    msg["To"] = to_email
    msg["From"] =from_email


    gmail = smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)


