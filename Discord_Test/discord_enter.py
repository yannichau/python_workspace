import keyboard
import time

text_file = open("/Users/yannichau/Documents/App_Development/Discord_Test/sunday_reminder.txt", "r") 

time.sleep(10)

for word in text_file:
    if "$natural" in word:
        keyboard.write(word)
        keyboard.send("enter")
        time.sleep(0.1)
