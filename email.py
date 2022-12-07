import logging
import datetime
import smtplib
import ssl

SMTP_SERVER = "your.smtp.server"
SENDER_EMAIL = "your@email.com"
EMAIL_PASSWORD = "Secret_Email_Password"
REDIS_BASE_URL = 'redis://localhost:6379'


def send_email(to: str, message: str):
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(SMTP_SERVER, 587) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(SENDER_EMAIL, EMAIL_PASSWORD)
            server.sendmail(SENDER_EMAIL, to, message)
            return True
    except Exception as _ex:
        logging.error(str(_ex))
        logging.critical(
            "Error occured while trying to"\
            f"send invoice to: <{to}>"
        )
        return False