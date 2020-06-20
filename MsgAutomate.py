from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from urllib.parse import quote

from time import sleep

# css_selector of message slot
css_selector = "#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text"

# message to be sent to everyone
msg = '''
Hey!!
This message is sent by automation.
'''
driver = webdriver.Chrome()

# enter comma separated 10 digit phone numbers here or read them from the numbers_file
phone = ['8285662036', '9718868859']


# url-encode the message, use other functions for handling dictionaries, not recommended
msg = quote(msg)
driver.get("https://web.whatsapp.com")
sleep(3)
for number in phone:
    url = "https://web.whatsapp.com/send?phone=91" + number + "&text=" + msg
    driver.get(url)
    sleep(3)
    driver.find_element_by_css_selector(css_selector).send_keys(Keys.RETURN)
    driver.execute_script("window.onbeforeunload = function() {};")
    print('Message sent successfully to ' + str(number))
print("Message sent to all contacts successfully")
driver.quit()
