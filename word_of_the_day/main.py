import smtplib
import random

def get_qoute():
    """
    TODO
    write a function that reads 'qoutes.txt'
    and returns a randomly selected qoute from the 
    qoutes.txt file.
    """
    with open("qoutes.txt", "r") as file:
        quote = file.readlines()
    return random.choice(quote)


def send_email(message):
    """
    TODO
    write a function that sends
    an email to your self using 
    smtplib and return 'success ' or 'fail' if sending email failed
    """

def main():
    """
    TODO
    write logic to use the two functions here
    """

print(get_qoute())