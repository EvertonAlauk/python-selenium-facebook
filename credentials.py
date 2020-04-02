# -*- coding: utf-8 -*-

class Credentials:

    def __init__(self, user="", username="", password=""):
        self.user = user
        self.username = username
        self.password = password

    def validate_credentials(self):
        print("Request the credentials.")
        # if you don't have the credentials, create some executation for this
        if not self.user and not self.username and not self.password:
            # you need have the credentials
            print("Username and password doesn't exist!")
            # get the data however you want
            print("Asking for the data...")
            user = self.get_user()
            username = self.get_username()
            password = self.get_password()
            print("The data is ok!")
            # and created the init with validated data
            Credentials(user=user, username=username, password=password)
            print("Username and password has created!")
        else:
            print("Username and password already exists!")

    def get_user(self):
        # try to get something
        try:
            self.user = str(input("User (url): "))
        except SyntaxError:
            # if don't, try again
            print("Please, inform the user url!")
            self.get_user()
        # if you got some data, try to split it in two elements
        # the first is the begging of facebook url
        # the second is the facebook username
        try:
            self.user = self.user.split('https://www.facebook.com/')[1]
        except IndexError:
            # if don't, try again
            print("Please, inform the user url!")
            self.get_user()
        # for any case, return the user
        return self.user

    def get_username(self):
        # try to get something
        try:
            self.username = str(input("Username: "))
        except SyntaxError:
            # if don't, try again
            print("Please, inform the user!")
            self.get_username()
        return self.username

    def get_password(self):
        # try to get something
        try:
            self.password = str(input("Password: "))
        except SyntaxError:
            # if don't, try again
            print("Please, inform the password!")
            self.get_password()
        return self.password
        
credentials = Credentials()
credentials.validate_credentials()