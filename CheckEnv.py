# superHero= input("what's your superhero Name:")
# print(superHero +" is my fav hero")

# num1=int(input("add num 1: "))
# num2=int(input("add num 2: "))

# sum=num1+num2
# print("total " + str(sum))

# name = "Romman Khan"
# print("finded position : " + str(name.find('K') + 1))

###Basic Calculator

# num1 = int(input("Add 1st Number : "))
# num2 = int(input("Add 2nd Number : "))

# oparator= input("which oparator you want + * / - % : ")

# if oparator == '+' :
#     print(num1 + num2)
# elif oparator == '*' :
#     print(num1 * num2)
# elif oparator == '-' :
#     print(num1 - num2)
# elif oparator == '/' :
#     print(num1 / num2)
# else:
#     print("please add perfect output")


# marks=[]

# for i in range(10):
#     marks.append(i+1)

# marks.insert(0,0)

# print(marks)
# print(len(marks))

# import math

# print(dir(math))

import os
import platform

def speak(text):
    if platform.system() == 'Windows':
        command = f'powershell -command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"'
    elif platform.system() == 'Darwin':  # macOS
        command = f'say "{text}"'
    else:
        raise NotImplementedError("Text-to-speech not supported on this platform")
    
    os.system(command)

if __name__ == '__main__':
    print("Welcome to Robospeaker")
    text = input("Input text: ")
    speak(text)
