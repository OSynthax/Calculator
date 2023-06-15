#Imports

import os 
import math
import sys
from fractions import Fraction

#give num1 and num2 values

num1 = 0
num2 = 0

#Possible Choices for Choice variable 

AddChoice = ("addition", "add", "+", "plus", "pluss", "adding", "1")

SubChoice = ("subtraction", "sub", "take", "take away", "minus", "2", "-")

MultChoice = ("multiplication", "mult", "×", "times", "times by", "3")

DivisionChoice = ("division", "divide", "÷", "4")

PercentChoice = ("percentage", "perc", "percentages", "%", "6", "percent")

HelpChoice = ("help", "h", "support", "8")

QuitChoice = ("quit", "stop", "exit", "q", "halt", "break")

AlgebraChoice = ("algebraic", "algebra", "alg", "7")

FractionChoice = ("fraction", "fractions", "frac", "5")

ClearChoice = ("clear", "clr", "ac", "c", "clean", "9")

DIVChoice = ("div", "8")

MODChoice = ("mod", "9")

#functions

def Quit():
  exit()
def NumberSelectionBasicMath():
  global num1, num2
  while True:
        try:
            num1 = int(input("|Enter your first number: "))
            num2 = int(input("|Enter your second number: "))
            break
        except ValueError:
            print("|Invalid input. Please enter two valid numbers")

def ChoiceSelect():
 print ("")
 Choice = input("|What would you like to do? ").lower()

 #if in basic math
 if Choice in AddChoice:
    Addition()
 elif Choice in SubChoice:
   Subtraction()
 elif Choice in MultChoice:
   Multiplication()
 elif Choice in DivisionChoice:
   Division()

 #if in algebraic, percentage, fraction

 elif Choice in PercentChoice:
  Percent()
 elif Choice in AlgebraChoice:
  Algebra()
 elif Choice in FractionChoice:
  Fractions()

#if help, clear or quit

 elif Choice in HelpChoice:
   Help()
 elif Choice in QuitChoice:
   Quit()
 elif Choice in ClearChoice:
   Clear()

#if DIV and MOD

 elif Choice in DIVChoice:
   DIV()
 elif Choice in MODChoice:
   MOD()
 else:
   print("|No Valid input selected, try again")
   print ("")
 ChoiceSelect()

   

#functions for basic maths

def Addition():
 NumberSelectionBasicMath()
 answer = num1 + num2
 print ("|", num1, "+", num2, "=",  answer)

def Subtraction():
 NumberSelectionBasicMath()
 answer = num1 - num2
 print ("|", num1, "-", num2, "=", answer)

def Multiplication():
 NumberSelectionBasicMath()
 answer = num1 * num2
 print ("|", num1, "×", num2, "=",  answer)

def Division():
  
  if num2 == 0:
        print("|Division by zero is undefined.")
        NumberSelectionBasicMath()
  else:
        answer = num1 / num2
        print("|", num1, "÷", num2, "=", answer)
#functions for algebraic, fractions and percentage

def Percent():
  while True:
    num1 = input("|Enter the number: ")
    num2 = input("|Enter the percentage: ")
    try:
      num1 = float(num1)
      num2 = float(num2)
      answer = num1 * (num2 / 100)
      print("|", num2, "% of", num1, "=", answer)
      

    except ValueError:
      print("|Invalid input. Please enter a valid number and percentage")
    break     

def Fractions():
  NumberSelectionBasicMath()
  print ("|The fraction of", num1, "and", num2, "is", (Fraction(num1, num2)))

def Algebra():
  print ("|Work in progress")

#help function

def Help():
  print ("|Made By Amy Readman")
  print ("|Type a variation of 'Quit' to exit the calculator")
  print ("|Type a variation of 'Clear' to clear the screen")

#DIV and MOD

def DIV():
  NumberSelectionBasicMath()
  answer = num1 // num2
  print ("|The DIV is", answer)

def MOD():
  NumberSelectionBasicMath()
  answer = num1 % num2
  print ("|The MOD is", answer)
   
#main menu function 

def Menu():
  print ("|Addition      |+|")
  print ("|Subtraction   |-|")
  print ("|Multiplication|×|")
  print ("|Division      |÷|")
  print ("|Fraction      |½|")
  print ("|Percentage    |%|")
  print ("|Algebraic     |∞|")
  print ("|DIV           |/|")
  print ("|MOD           |#|")
  print ("")
  print ("|Help          |?|")
  print ("|Clear         |C|")
  ChoiceSelect()

#clear function 

def Clear():
  os.system('cls')
  os.system('clear')
  Menu()


#main program

Menu()




