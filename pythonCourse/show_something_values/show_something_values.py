from curses.ascii import isalnum, isupper, isalpha, isascii, islower, isdigit, isspace

from numpy.core.defchararray import isnumeric, isdecimal

var = input("Type Something ")
print(type(var))
print("Is it alfa numeric ? \n" , var.isalnum())
print("Is it only numeric? \n",var.isnumeric())
print("Is it Supper or UpperCase? \n",var.isupper())
print("Is it LowerCase? \n", var.islower())
print("Is it alpha digit? \n", var.isalpha())
print("Is it ascii digit? \n", var.isascii())
print("Is it decimal ? \n", var.isdecimal())
print("Is it digit? \n", var.isdigit())
print("Is space? \n", var.isspace())
