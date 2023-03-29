import smtplib
from email.message import EmailMessage
from nameko.rpc import rpc
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv('ADDRESS')
EMAIL_PASSWORD = os.getenv('PASSWORD')

def send(id, firstname, lastname, email):
    msg = EmailMessage()
    msg['To'] = email
    msg['Subject'] = 'Microservice Workshop Complete!!!'
    msg['From'] = EMAIL_ADDRESS
    text = f"สวัสดีค่ะ คุณ {firstname} {lastname} รหัสนักศึกษา {id} ได้ทำ workshop microsevice เสร็จสักทีนะไอ่เวร"
    msg.set_content(text)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print('send!')

class Email:
    name = "email"

    @rpc
    def send(self, id, firstname, lastname, email):
        print('rabbitmq rpc')
        send(id, firstname, lastname, email)