# WAbot/bot.py

import platform
import random
import pyperclip
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from typing import List, Dict
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



class WAbot:
    def __init__(self, verbose=True, saveQR=False, headless=False, sandbox=True, shm=True):
        self.verbose = verbose
        self.log("Starting Chrome...")
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless')  # Run in headless mode
        if not sandbox:
            chrome_options.add_argument('--no-sandbox')
        if not shm:
            chrome_options.add_argument('--disable-dev-shm-usage')

        # Set the user agent to Firefox
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
        chrome_options.add_argument(f'user-agent={user_agent}')

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get('https://web.whatsapp.com/')
        self.log("Opened WA please login, waiting for login...")
        if saveQR:
            time.sleep(10)
            self.driver.save_screenshot("QRcode.png")
            self.log("saved QR code")
        time.sleep(2)
        WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/header/header/div/div[1]/h1'))
        )
        self.log("Loaded WA, continuing...")
        self.prepare_textbox()

    def go_to_contact(self, name: str):
        try:
         target_Element = WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable((By.XPATH, f"//*[@title='{name}']"))
         )
         target_Element.click()
         self.log(f"Clicked on contact '{name}' successfully.")
        except Exception as e:
            self.log(f"Could not find contact '{name}': {e}")


    def log(self, message):
        """Print a message if verbose mode is enabled."""
        if self.verbose:
            print(message)



    def prepare_textbox(self):
        """Turns off the enter key to send the message option and clicks on 'Chats' then niggga."""
        try:
            # Create a chord for Control + Alt + Comma
            actions = webdriver.ActionChains(self.driver)

            # Press and hold Control and Alt, then send the comma, and release the keys
            actions.key_down(Keys.CONTROL)
            actions.key_down(Keys.ALT)
            actions.send_keys(',')  # Comma is sent as a literal string
            actions.key_up(Keys.ALT)
            actions.key_up(Keys.CONTROL)
            actions.perform()

            # Find and click the "Chats" text
            chats_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[text()='Chats']"))
            )
            chats_element.click()
            self.log("Clicked on 'Chats' successfully.")

            # Check if the element's class matches the expected class
            checkbox_SVG = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/div/span/div/div/div/div/div/div[2]/div[6]/div/div/div'))
            )
            checkbox_clickable_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/div/span/div/div/div/div/div/div[2]/div[6]/div/div'))
            )
            element_class = checkbox_SVG.get_attribute('class')
            expected_class = "x1n2onr6 x9f619 x5yr21d x47corl xamhcws xol2nv xlxy82 x19p7ews x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi xm3z3ea x1x8b98j x131883w x16mih1h xts7igz xv1tzdm x1mn1qpr x1eqfvxv xh797gm xrn79m2 xfpr502"
            
            if element_class == expected_class:
                print("Element class matches the expected class.")
                checkbox_clickable_element.click()
            else:
                print("Element class does not match the expected class.")


            time.sleep(2)
            actions.key_down(Keys.ESCAPE)
            actions.key_up(Keys.ESCAPE)
            actions.key_down(Keys.ESCAPE)
            actions.key_up(Keys.ESCAPE)
            actions.perform()

            
        except Exception as e:
            self.log(f"Failed to prepare textbox or click 'Chats': {e}")
       


    def go_to_unknown_number(self):
        try:
         target_Element = WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable((By.XPATH, "//*[contains(@title, '+')]"))
         )
         target_Element.click()
         self.log("Clicked on an unknown number successfully.")
        except Exception as e:
            self.log(f"Could not find an unknown number contact: {e}")

    def send_message(self, msg: str, humanize: int):
        try:
            message_Element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'))
            )
            self.log("Message box is clickable, continuing...")
            message_Element.click()
            self.log("Clicked message box successfully...")
            time.sleep(humanize)
            message_Element.send_keys(msg)
            self.log("Typed message successfully, sending...")
            time.sleep(humanize)
            send_Element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[2]/button'))
            )
            send_Element.click()
            self.log("Sent message successfully.")
        except Exception as e:
            self.log(f"Failed to send message: {e}")
            

    def check_if_wa(self, phone_number: str):
        try:
            number_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a._ao3e.selectable-text.copyable-text'))
            )
            for element in number_elements:
                if element.text == phone_number:
                    element.click()
                    self.log("Clicked number successfully...")
                    try:
                        chat_div = WebDriverWait(self.driver, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Chat with')]"))
                        )
                    except:
                        chat_div = None
                    if chat_div:
                        self.log("Number is on WA...")
                        return True
                    else:
                        self.log("The number is not on WA...")
                        return False
        except Exception as e:
            self.log(f"An error occurred: {e}")

    def send_random_ad(self, ads: List[Dict], humanize: int):
        """Clicks 'Chat with' button, sends a random ad message."""
        
        try:
            # Locate and click the "Chat with" button
            chat_div = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Chat with')]"))
            )
            chat_div.click()
            self.log("Clicked the 'Chat with' button...")

            time.sleep(humanize)

            # Send a random advertisement message
            random_ad = random.choice(ads)
            time.sleep(humanize)

            self.send_message(random_ad)
            self.log(f"Sent random ad message: {random_ad}")

        except Exception as e:
            self.log(f"Failed to send random ad: {e}")        
    

    def get_message(self):
        """
        Iterates through elements by increasing the index in the XPATH, 
        starting from the first visible element until a non-existent div is found.
        Returns the WebElement of the last existing div.
        """
        try:
          all_messages_xpath = '//*[@id="main"]/div[3]/div/div[2]/div[3]/div'
          messages = self.driver.find_elements(By.XPATH, all_messages_xpath)
          latest_message = messages[-1]
          parent_div = latest_message.find_element(By.XPATH, './/ancestor::div[contains(@class, "copyable-text")]')
          message_content = latest_message.find_element(By.XPATH, './/span[1]/span').text
          data_pre_plain_text = parent_div.get_attribute('data-pre-plain-text')
          return {'Message': message_content, 'Sender': data_pre_plain_text}
        except:
            self.log("error getting message, contains emojis or is voice message.")
            return None


    def save_screenshot(self, screenshot_path):
      try:
        self.driver.save_screenshot(screenshot_path)
      except Exception as e:
        self.log(f"error saving screenshot: {e}")
