import smtplib
from getpass import getpass

def main():
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
    response = smtp_object.ehlo()
    print(f"Response from SMTP hello to server:\n\t{response}")
    response = smtp_object.starttls()
    print(f"Response from SMTP start TLS:\n\t{response}")

    email = input("Your GMail address: ")
    password = getpass("Your GMail App password: ")

    smtp_object.login(email, password)
    smtp_object.quit()

if __name__ == "__main__":
    main()
