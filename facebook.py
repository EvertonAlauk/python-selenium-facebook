# -*- coding: utf-8 -*-

import time
import uuid

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException

class Facebook:

  def __init__(self, browser):
    """ The init """
    # you need have the chromedriver on your project and set the path like that
    self.browser = browser
    print("Inicialiting the Facebook!")

  def log_in(self, credentials):
    """ The login """
    try:
        print("Login-in.")
        # open the browser on the login page
        print("Opening browser...")
        self.browser.get('https://www.facebook.com/')
        time.sleep(2)
        print("Browser opened!")
        # if you need to get any xpath, is:
        # right click, inspect the element, right click on html element inspected, copy, copy xpath
        print("Get the input...")
        username = self.browser.find_element_by_xpath("//input[@name='email']")
        password = self.browser.find_element_by_xpath("//input[@name='pass']")
        submit = self.browser.find_element_by_xpath("//input[@type='submit']")
        print("Input got!")
        # if you have the credentials, send them
        username.send_keys(credentials.username)
        password.send_keys(credentials.password)
        print("Sending the credentials.")
        # get log-in
        submit.send_keys(Keys.ENTER)
        time.sleep(2)
        """
          I need have sure that the user is logged
        """
        print("On-line.")
        return True
    # if dont have a window
    except NoSuchWindowException as err:
      print("NoSuchWindowException: {}". format(err))
    # for any error from webdriver
    except WebDriverException as err:
      print("WebDriverException: {}". format(err))

  def create_post(self, credentials):
    """ Post a text on Instagram """
    try:
      print("Creating a post...")
      self.browser.get('https://www.facebook.com/{}'.format(credentials.user))
      print("Acessing the user profile...")
      # click in the post field
      role_region = self.browser.find_element_by_css_selector('div[role="region"]')
      role_region.click()
      print("Post field opened...")
      role_textbox = self.browser.find_element_by_css_selector('div[role="textbox"]')
      # send the post data to the browser
      role_textbox.send_keys(str(uuid.uuid4()))
      print("Writing on textarea...")
      time.sleep(1)
      # posting the content
      post_submit = self.browser.find_element_by_class_name('_1mf7')
      post_submit.click()
      print("Posting...")
      time.sleep(3)
      return True
    # if dont have a window
    except NoSuchWindowException as err:
      print("NoSuchWindowException: {}". format(err))
    # for any error from webdriver
    except WebDriverException as err:
      print("WebDriverException: {}". format(err))
