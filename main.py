# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from facebook import Facebook
from credentials import Credentials

# exclude the notifications
options = Options()
options.add_argument("--disable-notifications")
browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)

def main():
  """
  The main code.
  You need have chromedriver in your path.
  """
  # get the credentials
  credentials = Credentials()
  # to get online on facebook
  facebook = Facebook(browser)
  facebook.log_in(credentials)
  # choice on action to do on Facebook
  actions(facebook, credentials)

def actions(facebook, credentials):
  """
  The system will be able to allow some options. Choice one.
  1) Create Post
  2) Exit
  Any other option the system will done.
  Anothers options are in development.
  """
  action_text = "Do you want to do something?\n1) Create a Post \n2) Exit \nOption: "
  action = int(input(action_text))
  while action <= 0:
    action = int(input(action_text))
  if action == 1:
    facebook.create_post(credentials)
    actions(facebook, credentials)
  else:
    print("Thank you. Come back!")
    browser.close()

main()
