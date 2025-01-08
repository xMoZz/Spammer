from ast import For
import pyautogui 
import time
import os
import colorama
clear = lambda: os.system('cls')

print("Spammer by xMoZz")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Repeat():
    print("What do you want to do?" + "\n  1. Spamm with the same settings \n  2. Spamm with different settings \n  3. Close the spammer")
    repe =int(input("--> "))
    if repe == 1:
        clear()
        Default()
    if repe == 2: 
        clear()
        Main()
    if repe == 3:
        clear()
        print("Shutting down.")
        time.sleep(0.5)
        print("Shutting down..")
        time.sleep(0.5)
        print("Shutting down...")
        time.sleep(0.5)
    else: 
        clear()
        print("Wrong input!")
        time.sleep(1)
        clear()
        Repeat()


def txtRepeat():
    print("What do you want to do?" + "\n  1. Spamm with the same settings \n  2. Spamm with different settings \n  3. Close the spammer")
    repe =int(input("--> "))
    if repe == 1:
        clear()
        txtspam()
    if repe == 2: 
        clear()
        Main()
    if repe == 3:
        clear()
        print("Shutting down.")
        time.sleep(0.5)
        print("Shutting down..")
        time.sleep(0.5)
        print("Shutting down...")
        time.sleep(0.5)
    else:
        clear()
        print("Wrong input!")
        time.sleep(1)
        clear()
        txtRepeat()


def sentRepeat():
    print("What do you want to do?" + "\n  1. Spamm with the same settings \n  2. Spamm with different settings \n  3. Close the spammer")
    repe =int(input("--> "))
    if repe == 1:
        clear()
        sentspam()
    if repe == 2: 
        clear()
        Main()
    if repe == 3:
        clear()
        print("Shutting down.")
        time.sleep(0.5)
        print("Shutting down..")
        time.sleep(0.5)
        print("Shutting down...")
        time.sleep(0.5)
    else:
        clear()
        print("Wrong input!")
        time.sleep(1)
        clear()
        sentRepeat()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Default():
    clear()
    print("Welocome to the default spam!")
    y = input("  What should I spam:  ")
    x = int(input("  How often should I spam: "))
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')
    for i in range(1,x):
        pyautogui.typewrite(y + '\n')
    pyautogui.typewrite("Spammer by xMoZz" + '\n')
    print("Done")
    time.sleep(1)
    clear()
    Repeat()



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def txtspam():
    clear()
    print("Welcome to the txt-spam! " + "\n In the installation folder you will find a file called data.txt. \n Insert the text you want to spamm in this file.")
    input("  --> If you are ready press enter!")
    
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

    with open("data.txt", "r") as f:
        counter = Counter(f)
        l = counter['\n']
        lenght = int(l)
        print("Spamming " + str(lenght) + " lines of text.")
        
        i = 0  

        while i <= lenght:
        #for item in f:  
            with open("data.txt", "r") as f:
                data = f.readline(-1)
                pyautogui.typewrite(data)
                i += 1
                print("Line " + str(i) + "/" + str(lenght))
            

    pyautogui.typewrite("\n")
    pyautogui.typewrite("Spammer by xMoZz" + '\n')
    print("Done")
    time.sleep(1)
    clear()
    txtRepeat()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sentspam():
    clear()
    print("Welcome to the Sentence-spam! " + " \n  Insert the sentence you want to spamm word by word. \n  Whenever you are ready, enter the sentence and press enter! ")
    sent = input("--> ")
    
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

    y = sent.split(" ", -1)

    for i in range(0, len(y)):
        uwu = y[i]
        pyautogui.typewrite(uwu + '\n')


    pyautogui.typewrite("\n")
    pyautogui.typewrite("Spammer by xMoZz" + '\n')
    print("Done")
    time.sleep(1)
    clear()
    sentRepeat()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Main():
    a = int(input("Which Spammermode do you prefer?" + "\n  1. Default Spammer" + "\n  2. Txt Spammer" + "\n  3. Sentence Spammer" + "\n --> Enter the number of the choosen option: "))
    if a == 1:
        clear()
        Default()
    elif a == 2:
        clear()
        txtspam() 
    elif a == 3: 
        clear()
        sentspam()

Main()