import smtplib
from random import choice

def main():
    """
    TODO
    write logic to use the two functions here
    """
    quote = get_qoute()
    send_email(quote)

def get_qoute():
    """
    TODO
    write a function that reads 'qoutes.txt'
    and returns a randomly selected qoute from the 
    qoutes.txt file.
    """
    with open("qoutes.txt", "r") as file:
        quote = file.readlines()
    return choice(quote)


def send_email(message):
    """
    TODO
    write a function that sends
    an email to your self using 
    smtplib and return 'success ' or 'fail' if sending email failed
    """
    with open('email.txt', 'r') as _email:
       sender_email = _email.read()

    with open('password.txt', 'r') as pin:
        password = pin.read()

    subject = "Quote of the day"
    reciever = sender_email
    text = f"Subject: {subject} \n\n {message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(sender_email, password)
    server.sendmail(sender_email, reciever, text)

    print("Email has been sent")
    
if __name__ == "__main__":
    main()
