#-------------------------------------------------------------------------------
# Name:        Simple OOP
# Purpose:
#
# Author:      kenny.coons
#
# Created:     06/11/2019
# Copyright:   (c) kenny.coons 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class printer:

    def __init__(self, first, last):
        self.first =  first
        self.last = last
        self.email = first + '.' + last + "@email.com"

first_name = input("What is ypur first name?")
last_name = input("What is your last name?")


person = printer(first_name, last_name)

print(person.first, person.last)
print(person.email)