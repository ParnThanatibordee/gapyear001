import pyautogui
import time
import webbrowser

url = 'https://www.google.com'
webbrowser.open(url)
pyautogui.click()

time.sleep(3)
pyautogui.write('thailand')
pyautogui.press('enter')

def Search(word):
    time.sleep(3)
    for i in range(7):
        pyautogui.press('tab')

    pyautogui.press('backspace')
    pyautogui.write(word)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.screenshot(word + '.png')

Search('singapore')
Search('usa')
Search('china')