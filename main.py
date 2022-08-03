import datetime
import smtplib
import pandas
import random

# ---------------------------- EMAIL DATA------------------------------- #
#TODO Fill your email data
my_email = ""
my_pass = ""

# ---------------------------- CURRENT DAY------------------------------- #

current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day

# ---------------------------- FILE------------------------------- #
data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

# ----------------------------SENDING EMAIL------------------------------- #

for row in data_dict:
    name = row["name"]
    if row["month"] == current_month and row["day"] == current_day:
        with open(f"letter_{random.randint(1, 3)}.txt", mode="r+") as df:
            data = df.read()
            data = data.replace("[NAME]", name)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_pass)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=row["email"],
                    msg=f"Subject: Happy B-DAY! \n\n{data}"
                )
