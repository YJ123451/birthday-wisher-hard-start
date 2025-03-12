from datetime import datetime
import random, smtplib, pandas

my_email = "yousif.abdeljawad@codepath.org"
app_password = ######


today = datetime.now()
today_tuple = (today.month, today.day)


data = pandas.read_csv("birthdays.csv")
bday_dict = {(data_row["month"],data_row["day"]): data_row for(index, data_row) in data.iterrows()}

if today_tuple in bday_dict:
    birthday_person = bday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path,"r") as file:
        txt = file.read()
        bday_message= txt.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{bday_message}"
        )

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



