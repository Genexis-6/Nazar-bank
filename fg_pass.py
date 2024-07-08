from email.message import EmailMessage
import smtplib
import ssl
from dotenv import load_dotenv
import os
from random import choice


load_dotenv()

ADMIN_EMAIL=os.getenv('EMAIL_USER')
ADIMN_PASSWORD=os.getenv('EMAIL_PASSWORD')

class Otp:
    def __init__(self):
        self.num = [str(x) for x in range(0,9)]
        self.code = ''
        self.generate()
        
    def generate(self):
        for nums in range(6):
            self.code += choice(self.num)

class ForgottenPassword:
    def __init__(self,useremail,code):
        self.code = code
        self.from_email = ADMIN_EMAIL
        self.to_email = useremail
        self.email_pass = ADIMN_PASSWORD
        self.HOST = "smtp.gmail.com"
        self.PORT = 465 # AZUDONI VICTORY CHUWKUNEKU WORK
        self.send_message()
        
        
    def send_message(self):
        subject = "otp code"
        body = f"""
        -> {self.code}
        

        """# AZUDONI VICTORY CHUWKUNEKU WORK

        em = EmailMessage()
        em["From"] = self.from_email
        em['To'] = self.to_email
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()# AZUDONI VICTORY CHUWKUNEKU WORK
        email = smtplib.SMTP_SSL(host= self.HOST, port=self.PORT, context=context)
        email.login(user=self.from_email,password=self.email_pass)
        email.send_message(msg= em,from_addr=self.from_email,to_addrs=self.to_email)
        
        
