import smtplib, ssl
from django.conf import settings
import os ,sys

class Email:
    def send(self,receiver_email: str,message:str):
        try:
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = settings.DEFAULT_EMAIL 
            password = settings.CRED
            # message = """\
            # Subject: YOUR OTP

            # This message is sent from Python."""

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(
                exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            
            print('*******exception***********',e)