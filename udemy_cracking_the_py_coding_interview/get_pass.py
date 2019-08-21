#!/usr/bin/env python3

from getpass import  getpass

def take_input_from_user(prompt=''):
    try:
        line = raw_input(prompt)
    except:
        line = input(prompt)

def fetch_creds():
    username = take_input_from_user('Username: ')
    password = None
    while not password:
        password = getpass('Password: ')
        password_verify = getpass('Re-enter Password: ')
        if password != password_verify:
            print ('Passwords do not match! Try again.')
            password = None
    return username, password

if __name__ == "__main__":
    fetch_creds()
