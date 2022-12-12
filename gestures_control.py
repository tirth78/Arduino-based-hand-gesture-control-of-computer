from serial import Serial # add Serial library for serial communication
import pyautogui  # add pyautogui library for programmatically controlling the mouse and keyboard.

Arduino_Serial = Serial('com8', 9600)    # Initialize serial and Create Serial port object called Arduino_Serial
#Arduino_Serial = Serial('/dev/ttyACM0', 9600)    # Initialize serial and Create Serial port object called Arduino_Serial

while 1:
    incoming_data = str(Arduino_Serial.readline())  # read the serial data and print it as line
    print(incoming_data)  # print the incoming Serial data

    if 'next' in incoming_data:  # if incoming data is 'next'
        pyautogui.hotkey('ctrl', 'pgdn')  # perform "ctrl+pgdn" operation which moves to the next tab

    #if 'previous' in incoming_data:  # if incoming data is 'previous'
        #pyautogui.hotkey('ctrl', 'pgup')  # perform "ctrl+pgup" operation which moves to the previous tab

    if 'previous' in incoming_data:  # if incoming data is 'previous'
            pyautogui.hotkey('space')  # play/pause the vedio

    if 'down' in incoming_data:  # if incoming data is 'down'
        # pyautogui.press('down')                   # performs "down arrow" operation which scrolls down the page
        pyautogui.press('down')

    if 'up' in incoming_data:  # if incoming data is 'up'
        # pyautogui.press('up')                      # performs "up arrow" operation which scrolls up the page
        pyautogui.press('up')

    if 'change' in incoming_data:  # if incoming data is 'change'
        pyautogui.keyDown('alt')  # performs "alt+tab" operation which switches the tab
        pyautogui.press('tab')
        pyautogui.keyUp('alt')

    incoming_data = "";  # clears  the data
