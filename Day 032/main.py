import pandas as pd
import datetime as dt
import smtplib
import os
import random

# CONFIGURATION: Replace with your Gmail credentials
# NOTE: Use App Password, not your regular Gmail password
# GUIDE: https://support.google.com/accounts/answer/185833

my_email = "YOUREMAILHERE@EMAIL.COM"
password = "YOURPASSWORDHERE"

now =dt.datetime.now()
this_month = now.month
this_day = now.day

df = pd.read_csv("birthdays.csv")

#Temp Variables
name = "name"
recipient_email = "email"
final_letter = "final"

#Pick a letter and replace the [Name]
def write_letter(name):
    global final_letter
    random_letter = random.choice(os.listdir('letter_templates'))
    with open(f"letter_templates/{random_letter}") as f:
        letter_content = f.read()

    final_letter = letter_content.replace("[NAME]", name)
    
#send mail
def send_mail():
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password= password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=recipient_email,
                                    msg=f"Subject:Happy Birthday!!\nTo:{recipient_email}\n\n{final_letter}")
                
#MainLooP
def bd_mail():
    global name, recipient_email

    for index, row in df.iterrows():
        if row["month"] == this_month and row["day"] == this_day:
            name = row["name"]
            recipient_email = row["email"]
            write_letter(name)
            send_mail()

#One Function to Rule 'Em All
bd_mail()