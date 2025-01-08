from ast import For
import pyautogui 
import time
import os
import colorama
from colorama import Fore
from colorama import Style
from collections import Counter
clear = lambda: os.system('cls')

#----------------------------------------------------------------------------------------------------------------------

def Repeat():
    print(Fore.BLUE + "What do you want to do?" + Style.RESET_ALL + Fore.RED + "\n  1. Spamm with the same settings \n  2. Spamm with different settings \n  3. Close the spammer")
    repe =int(input(Fore.CYAN + "--> " + Style.RESET_ALL))
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
        print(Fore.RED + "Wrong input!")
        time.sleep(1)
        clear()
        Repeat()


def txtRepeat():
    print(Fore.BLUE + "What do you want to do?" + Style.RESET_ALL + Fore.RED + "\n  1. Spamm with the same settings \n  2. Spamm with different settings \n  3. Close the spammer")
    repe =int(input(Fore.CYAN + "--> " + Style.RESET_ALL))
    if repe == 1:
        clear()
        txtspam()
    if repe == 2: 
        clear()
        Main()
    if repe == 3:
        clear()
        print(Fore.GREEN + "Shutting down.")
        time.sleep(0.5)
        print("Shutting down..")
        time.sleep(0.5)
        print("Shutting down...")
        time.sleep(0.5)
    else:
        clear()
        print(Fore.RED + "Wrong input!")
        time.sleep(1)
        clear()
        txtRepeat()


def sentRepeat():
    print(Fore.BLUE + "What do you want to do?" + Style.RESET_ALL + Fore.RED + "\n  1. Spamm with the same settings \n  2. Spamm with different settings \n  3. Close the spammer")
    repe =int(input(Fore.CYAN + "--> " + Style.RESET_ALL))
    if repe == 1:
        clear()
        sentspam()
    if repe == 2: 
        clear()
        Main()
    if repe == 3:
        clear()
        print(Fore.GREEN + "Shutting down.")
        time.sleep(0.5)
        print("Shutting down..")
        time.sleep(0.5)
        print("Shutting down...")
        time.sleep(0.5)
    else:
        clear()
        print(Fore.RED + "Wrong input!")
        time.sleep(1)
        clear()
        sentRepeat()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Default():
    clear()
    print(Fore.BLUE + "Welocome to the default spam!")
    y = input(Fore.RED + "  What should I spam:  " + Fore.CYAN)
    x = int(input(Fore.RED + "  How often should I spam: " + Fore.CYAN))
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')
    for i in range(1,x):
        pyautogui.typewrite(y + '\n')
    pyautogui.typewrite("Spammer by xMoZz" + '\n')
    print(Fore.GREEN + "Done")
    time.sleep(1)
    clear()
    Repeat()



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def txtspam():
    clear()
    print(Fore.BLUE + "Welcome to the txt-spam! " + Style.RESET_ALL + Fore.RED + "\n In the installation folder you will find a file called data.txt. \n Insert the text you want to spamm in this file." + Style.RESET_ALL)
    input(Fore.CYAN + "  --> If you are ready press enter!" + Style.RESET_ALL)
    
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
    print(Fore.GREEN + "Done")
    time.sleep(1)
    clear()
    txtRepeat()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sentspam():
    clear()
    print(Fore.BLUE +"Welcome to the Sentence-spam! " + Style.RESET_ALL + Fore.RED + " \n  Insert the sentence you want to spamm word by word. \n  Whenever you are ready, enter the sentence and press enter! " + Style.RESET_ALL)
    sent = input(Fore.CYAN + "--> ")
    
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
    print(Fore.GREEN + "Done")
    time.sleep(1)
    clear()
    sentRepeat()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Main():
    clear()
    a = int(input(Fore.BLUE + "Which Spammermode do you prefer?" + Style.RESET_ALL + Fore.RED + "\n  1. Default Spammer" + Style.RESET_ALL + Fore.RED + "\n  2. Txt Spammer" + Style.RESET_ALL + Fore.RED + "\n  3. Sentence Spammer" + Style.RESET_ALL + Fore.GREEN + "\n --> Enter the number of the choosen option: "))
    if a == 1:
        clear()
        Default()
    elif a == 2:
        clear()
        txtspam() 
    elif a == 3: 
        clear()
        sentspam()
    else: 
        print(Fore.RED + "Worng input!" + Style.RESET_ALL)
        clear()
        Main()


Main()