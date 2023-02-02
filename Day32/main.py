import smtplib

my_email = "abbcc@outlook.com"
password = "abcd1234()"

connection = smtplib.SMTP("smtp-mail.outlook.com")
# Transport Layer Security
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr= my_email,
    to_addrs= my_email,
    msg="Subject:Hello\n\nContent "
)
connection.close()

# import datetime as dt
# import random
#
# now = dt.datetime.now()
# print(now)
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(year)
# print(month)
# print(day_of_week)
#
#
# # use datetime to obtain the current day of the week
# # if day_of_week == 1:
# # open the quotes.txt file and obtain a list of quotes
# with open("./quotes.txt") as file:
#     all_quotes = file.readlines()
#
# # Use the random module to pick a random quote from your list of quotes
# quote = random.choice(all_quotes)
#
# print(quote)
