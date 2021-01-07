import config
import smtplib


class NotificationManager:

    def __init__(self):
        pass

    def send_mail(self, message, subject):
        yahoo_address = config.to_address
        my_email = config.from_address
        password = config.password

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=yahoo_address,
                msg=f"Subject:{subject}\n\n"
                    f"{message}".encode("utf-8")
                )
