import tkinter as tk

# Creating Some Variables

firstNumber=0
secondNumber=0
result=0

# Creating a Window

window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

# Creating Functions

        # Functions

def calculate(firstNumber,secondNumber,symbol):
    if symbol=="+":
        
        result = str(firstNumber + secondNumber)

        screen.delete(0,"end")
        screen.insert("end", result)
    elif symbol=="-":
        
        result = str(firstNumber - secondNumber)

        screen.delete(0,"end")
        screen.insert("end", result)

    elif symbol=="/":
        
        result = str(firstNumber / secondNumber)

        screen.delete(0,"end")
        screen.insert("end", result)

    elif symbol=="x":

        result = str(firstNumber * secondNumber)

        screen.delete(0,"end")
        screen.insert("end", result)
    else:
        screen.delete(0,"end")
        screen.insert("end", "Error")

def getLine():
    
    numberStr = screen.get()

    numberList = numberStr.split(symbol)

    firstNumber = int(numberList[0])
    secondNumber = int(numberList[1])

    calculate(firstNumber,secondNumber,symbol)

def clear():
    screen.delete(0,"end")


    # Creating Functions for Symbols

def plusFunc():
    screen.insert("end","+")

    global symbol
    symbol="+"

def minusFunc():
    screen.insert("end","-")

    global symbol
    symbol="-"


def divisionFunc():
    screen.insert("end","/")

    global symbol
    symbol="/"

def multiplicationFunc():
    screen.insert("end","x")

    global symbol
    symbol="x"

#Creating App Design

    # Creating Frames for Organizing the App
    
screenFrame = tk.Frame(window,width=300,height=100)
screenFrame.pack(side="top")

buttonFrame = tk.Frame(window,width=300,height=300)     
buttonFrame.pack(side="bottom")

    # Creating a Entry for Input and Output

screen = tk.Entry(screenFrame)
screen.pack()
screen.place(width=300,height=100)

    # Creating Buttons

        # First Column

        # First, I defined funcitons like one(),two()... on functions' section but then I realise that there is lambda function to simple action
        # so that's why I use lambda on button definition

seven = tk.Button(buttonFrame,width=9,height=4,text="7",command=lambda:screen.insert("end", 7))
seven.grid(row=1,column=1)

four = tk.Button(buttonFrame,width=9,height=4,text="4",command=lambda:screen.insert("end", 4))
four.grid(row=2,column=1)

one = tk.Button(buttonFrame,width=9,height=4,text="1",command=lambda:screen.insert("end", 1))
one.grid(row=3,column=1)

zero = tk.Button(buttonFrame,width=9,height=4,text="0",command=lambda:screen.insert("end", 0))
zero.grid(row=4,column=1)

        # Second Column

eight = tk.Button(buttonFrame,width=9,height=4,text="8",command=lambda:screen.insert("end", 8))
eight.grid(row=1,column=2)

five = tk.Button(buttonFrame,width=9,height=4,text="5",command=lambda:screen.insert("end", 5))
five.grid(row=2,column=2)

two = tk.Button(buttonFrame,width=9,height=4,text="2",command=lambda:screen.insert("end", 2))
two.grid(row=3,column=2)

clear = tk.Button(buttonFrame,width=9,height=4,text="C",command=clear)
clear.grid(row=4,column=2)

        # Third Column

nine = tk.Button(buttonFrame,width=9,height=4,text="9",command=lambda:screen.insert("end", 9))
nine.grid(row=1,column=3)

six = tk.Button(buttonFrame,width=9,height=4,text="6",command=lambda:screen.insert("end", 6))
six.grid(row=2,column=3)

three = tk.Button(buttonFrame,width=9,height=4,text="3",command=lambda:screen.insert("end", 3))
three.grid(row=3,column=3)

enter = tk.Button(buttonFrame,width=9,height=4,text="ENTER",command=getLine)
enter.grid(row=4,column=3)

        # Fourth Column

plus = tk.Button(buttonFrame,width=9,height=4,text="+",command=plusFunc)
plus.grid(row=1,column=4)

minus = tk.Button(buttonFrame,width=9,height=4,text="-",command=minusFunc)
minus.grid(row=2,column=4)

division = tk.Button(buttonFrame,width=9,height=4,text="/",command=divisionFunc)
division.grid(row=3,column=4)

multiplication = tk.Button(buttonFrame,width=9,height=4,text="*",command=multiplicationFunc)
multiplication.grid(row=4,column=4)


# Starting the app

window.mainloop()