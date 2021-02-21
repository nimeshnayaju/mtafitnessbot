import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from datetime import date

load_dotenv(".env")

SENDER = os.environ.get("SENDER")
PASSWORD = os.environ.get("PASSWORD")
RECIPIENT = os.environ.get("RECIPIENT")
SUBJECT = os.environ.get("SUBJECT")
BODY = os.environ.get("BODY")
NAME = os.environ.get("NAME")

def following_day():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    following_day = ( date.today().weekday() + 1 ) % 7
    return days[following_day]

def time():
    day = following_day()

    if day == "Monday":
        return os.environ.get("MONDAY")
    elif day == "Tuesday":
        return os.environ.get("TUESDAY")
    elif day == "Wednesday":
        return os.environ.get("WEDNESDAY")
    elif day == "Thursday":
        return os.environ.get("THURSDAY")
    elif day == "Friday":
        return os.environ.get("FRIDAY")
    elif day == "Saturday":
        return os.environ.get("SATURDAY")
    elif day == "Sunday":
        return os.environ.get("SUNDAY")
    
def email_body():
    return "Hello, could you please book me a " + time() + " slot on " + following_day() + "?\n\nThanks,\n" + NAME

def send_email():
    host = 'smtp.office365.com'
    port = 587

    with smtplib.SMTP(host, port) as server:

        msg_body = email_body()
        msg = MIMEText(msg_body)
        msg["Subject"] = SUBJECT
        msg["From"] = SENDER
        msg["To"] = RECIPIENT

        server.starttls()
        server.login(SENDER, PASSWORD)
        server.sendmail(SENDER, RECIPIENT, msg.as_string())
        print("email sent successfully")
        server.quit()

send_email()
