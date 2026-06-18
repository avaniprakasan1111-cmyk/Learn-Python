import pywhatkit
import pyautogui
import time

phone_number = "+918157834729"
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

