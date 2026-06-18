"Automation code to send Messages on Whatsup"

import pywhatkit
import pyautogui
import time

phone_number = "Enter Phone number with country code"
message = "Hello"

pywhatkit.sendwhatmsg_instantly(
    phone_number,
    message,
    wait_time=15,
    tab_close=False
)

time.sleep(5)


pyautogui.click(900, 950)
pyautogui.press("enter")

