import smtplib

my_email = "talerpalmer@gmail.com"
password = "calleJaime1"            # hhrrki*954+6

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="talera.palmera@yahoo.com",
                        msg="Subject:Hello2\n\nThis is the body of my email")