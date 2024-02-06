# NEMUEL NUHYEL LAUSHI BHU/23/04/09/0046
# ISHAKU ANDREW  BHU/23/04/09/0050
# NDUKWE EMMANUEL KALU  BHU/23/04/09/0076
# EBENEHI SIMEON  BHU/23/04/09/0025
#

from tkinter import *


def buttonClick(number):
    global operator
    operator = operator + str(number)
    input_value.set(operator)


def buttonclear():
    global operator
    operator = ""
    input_value.set("")


def buttonEqual():
    global operator
    result = str(eval(operator))
    input_value.set(result)
    operator = ""


window = Tk()
window.title("my_calculator")
operator = ""
input_value = StringVar()
display_text = Entry(window, font=("arial", 20, "bold"), textvariable=input_value, bd=20, insertwidth=4, bg="#F5F5F5",
                     justify=RIGHT)
display_text.grid(columnspan=4)