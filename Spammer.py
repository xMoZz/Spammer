import pyautogui  
import time

#Allgemeine Variablen:
y = input("What should I spamm:  ")
x = int(input("How often should I spamm: "))


def Repeat():
    z =int(input("If you want to spamm again with the same settings write 1: "))
    if z == 1:
        time.sleep(3)
        Main()
   
    else:
        print("Shutting down.")
        time.sleep(0.5)
        print("Shutting down..")
        time.sleep(0.5)
        print("Shutting down...")
        time.sleep(0.5)

def Main():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

    for i in range(0,x):
        pyautogui.typewrite(y + '\n')

    pyautogui.typewrite("Spammer by xMoZz" + '\n')

    Repeat()


#Main Program:
Main()

