from smtplib import SMTP
from getpass import getpass

class GmailSMTP:
    def __init__(self):
        self.smtp_object = SMTP('smtp.gmail.com', 587)
        response = self.smtp_object.ehlo()
        print(f"Response from SMTP hello to server:\n\t{response}")
        response = self.smtp_object.starttls()
        print(f"Response from SMTP start TLS:\n\t{response}")

    def login(self):
        self.email = input("Your GMail address: ")
        self.password = getpass("Your GMail App password: ")
        response = self.smtp_object.login(self.email, self.password)
        print(f"Response from SMTP login:\n\t{response}")

    def send(self, recipient, subj, text):
        msg = "Subject: " + subj + '\n' + text
        response = self.smtp_object.sendmail(self.email, recipient, msg)
        print(f"Response from SMTP send:\n\t{response}")

    def __del__(self):
        self.smtp_object.quit()


def main():
    client = GmailSMTP()
    client.login()
    client.send(recipient=input("Enter the email of the recipient: "), \
            subj=input("Enter the subject line: "), \
            text=input("Type out the message you want to send: "))

if __name__ == "__main__":
    main()
