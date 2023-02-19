##################### Hard Starting Project ######################
import smtplib

import pandas
import datetime
import random

MY_EMAIL = ""
MY_PASSWORD = ""

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes.
data = pandas.read_csv("./birthdays.csv")
today_month = datetime.datetime().now().month
today_day = datetime.datetime().now().day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for key, data_row in data.iterrows()}
if (today_month, today_day) in birthdays_dict:
    birthday_person = birthdays_dict[(today_month, today_day)]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp
    filepath = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(filepath) as file:
        content = file.read()
        content = content.replace("[NAME]", birthday_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr= MY_EMAIL, to_addrs=birthday_person["email"], msg=f"Subject: Happy birthday\n\n {content}")


