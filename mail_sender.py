import pyautogui
import time

reciver_email = input("Enter reciver email (ex. namanswpd@gmail.com): ")
sub = input("Enter subject: ")
msg = input("Enter message to send: ")
brow = input("Enter browser name(edge,chrome): ")

time.sleep(4)

pyautogui.press("win")
time.sleep(2)
pyautogui.write(brow)
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
time.sleep(2)
pyautogui.press("enter")
time.sleep(13)


pyautogui.press("c")


time.sleep(4)

pyautogui.write(reciver_email)
time.sleep(2)
pyautogui.press("tab")
pyautogui.press("tab")
time.sleep(1)
pyautogui.write(sub)
time.sleep(2)
pyautogui.press("tab")
time.sleep(1)
pyautogui.write(msg)
time.sleep(2)


pyautogui.hotkey("ctrl", "enter")
