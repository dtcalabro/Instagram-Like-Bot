from selenium import webdriver
from selenium.common.exceptions import *
import sys
import time

# The main bot function.
class instagram_bot():
    # Here we create the window that instagram loads into.
    def __init__(self, driver, url, username, password):
        print("Creating window!")
        # We set the chrome options below.
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        # In the next line, specify the user data directory of your chrome. It might look something like this ...
        chrome_options.add_argument("--user-data-dir = /Users/yourname/Library/Application Support/Google/Chrome/Default")
        chrome_options.add_argument("--profile-directory = Default")
        chrome_options.add_argument("--disable-notifications")
        # We call the driver and give it the instagram url to navigate to, as well as tell it to login with the correct credentials.
        self.driver = webdriver.Chrome(driver)
        self.driver.get(url)
        self.login(username, password)

    # We define what happens when an error occurs.
    def show_exception(self, e):
        print(e)
        self.driver.quit()
        sys.exit()

    # We define what is needed, in order to login to the account(s) and we give it the credentials needed.
    def login(self, username, password):
        try:
            # This first part I found is only needed sometimes. I don't know why, but sometimes it pops up asking about cookies
            # and other times it doesn't. If it doesn't ask about cookies, then just comment it out.
            time.sleep(5)
            accept_cookies = self.driver.find_element_by_xpath("//button[@class='aOOlW  bIiDR  ']")
            accept_cookies.click()
            # If the cookies popup never apears, them comment out, up to this point, as the rest should be needed.
            time.sleep(2)

            # We look for the username textfield and we send it the username of the account.
            email_box = self.driver.find_element_by_xpath("//input[@name='username']")
            email_box.send_keys(username)

            # We look for the password textfield and we send it the password of the account.
            pass_box = self.driver.find_element_by_xpath("//input[@name='password']")
            pass_box.send_keys(password)

            # We look for the login button and then we click it.
            login_btn = self.driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
            login_btn.click()
            time.sleep(3)

            # We accept the popup asking to save your info. It doesn't really save it, as it resets after each chrome window 
            # closes and reopens. We just need to dismiss it in order to access instagram.
            save_info_btn = self.driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
            save_info_btn.click()
            time.sleep(3)

            # Same as before, it doesn't send you notifications, because it resets when you close and reopen the chrome window.
            # We just need to dismiss it in order to access instagram.
            notif_btn = self.driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
            notif_btn.click()
            time.sleep(1)

            # We print out to the console that login to the account was successful.
            print("Finished logging in to Account!")
            time.sleep(2)

        # If it fails for some reason, (like an element that cannot be found), then we call these functions so that the program quits.
        except NoSuchElementException as e:
            self.show_exception(e)

        except Exception as e:
            self.show_exception()

    # This is an extra function that isn't needed but can be used if you plan on adding extra capabilities.
    # All this does is, it navigates to the explore tab.
    def go_home(self):
        try:
            # We look for the explore tab and then we click it.
            go_to_home_btn = self.driver.find_element_by_xpath("//a[@href='/explore/']")
            go_to_home_btn.click()
            time.sleep(5)

        # If it fails for some reason, (like an element that cannot be found), then we call these functions so that the program quits.
        except NoSuchElementException as e:
            self.show_exception(e)

        except Exception as e:
            self.show_exception()

    # This defines a function that goes to the post you want to like, by giving it the post url
    def go_to_post(self, posturl):
        try:
            # It brings us to the post url
            self.driver.get(posturl)
            time.sleep(1)
            print("Going to post!")
            time.sleep(2)

        # If it fails for some reason, (like an element that cannot be found), then we call these functions so that the program quits.
        except NoSuchElementException as e:
            self.show_exception(e)

        except Exception as e:
            self.show_exception()
    
    # This defines a function that likes the post
    def like_post(self):
        try:
            print("Attempting to like post!")
            # Below it looks for the like button
            like_post_btn = self.driver.find_element_by_class_name("fr66n")
            element = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button/div/span/*[name()='svg']")
            
            # Depending on the color of the like button, we can determine if the post is already liked or not
            color = element.get_attribute("fill")
            
            # If we determine that the post is not already liked, then we click the like button
            if color == "#262626":
                like_post_btn.click()
                print("Successfully liked post!")
            # If we determine that the post is already liked, then we don't click the like button, so that way the post stays liked.
            elif color == "#ed4956":
                print("Post is already liked!")
            time.sleep(1)

        # If it fails for some reason, (like an element that cannot be found), then we call these functions so that the program quits.
        except NoSuchElementException as e:
            self.show_exception(e)

        except Exception as e:
            self.show_exception()
    
    # This defines a function that is used to log out of the account.
    def log_out(self):
        try:
            # We look for the profile button and then we click it.
            profile_btn = self.driver.find_element_by_xpath("//span[@class='_2dbep qNELH']").click()
            time.sleep(3)

            # We look for the log out button and then we click it.
            log_out_btn = self.driver.find_element_by_xpath("//div[@class='-qQT3']").click()
            time.sleep(3)

            # We look for the switch account button and then we click it.
            switch_account_btn = self.driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']").click()
            time.sleep(3)

            # We look for the remove account button and then we click it.
            remove_account_btn = self.driver.find_element_by_xpath("//button[@class='aOOlW  bIiDR  ']").click()
            time.sleep(1)

            print("Logging out of account  #1!")
            time.sleep(2)
            self.driver.close()
            print("Closing active Chrome window!")
            time.sleep(2)

        # If it fails for some reason, (like an element that cannot be found), then we call these functions so that the program quits.
        except NoSuchElementException as e:
            self.show_exception(e)

        except Exception as e:
            self.show_exception()
    
    # This defines a function that closes the active chrome window.
    def close_window(self):
        try:
            self.driver.close()
            print("Closing active Chrome window!")
            time.sleep(2)

        # If it fails for some reason, (like an element that cannot be found), then we call these functions so that the program quits.
        except NoSuchElementException as e:
            self.show_exception(e)

        except Exception as e:
            self.show_exception()