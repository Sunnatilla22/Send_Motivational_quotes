import random
import datetime as dt
import smtplib
my_email = "mirvaliyevsunnat@gmail.com"
password = "bkqkhmxfnsrgvkox"

now = dt.datetime.now()
day_of_week = now.weekday()
hour = now.hour
minutes = now.minute

if day_of_week == 7 and hour == 7 and minutes == 13 :
    with open("quotes.txt", "r") as quote_files:
        all_quotes = quote_files.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="hayrullamirvaliyev@gmail.com",
                            msg=f"Subject: Motivatinal quotes\n\n{quote}. Time is {now}")
        print("Email sent")


