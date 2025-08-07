x=int(input("Enter first number:"))
y=int(input("enter 2nd number:"))
z=input("select operation(+,-,*,/):")
if z == "+":
    print(x+y)
if z=="-":
    print(x-y)
if z=="*":
    print(x*y)
if z=="/":
    print(x/y)

import pyttsx3
engine = pyttsx3.init()


engine.say("Operation complete")
engine.runAndWait()