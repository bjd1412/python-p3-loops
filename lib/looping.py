#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i >= 1:
        print(i)
        i -= 1       
        print("Happy New Year!")

def square_integers(int_list):
    return [integer ** 2 for integer in int_list ]

def fizzbuzz():
    for integers in range(1, 101):
        if integers % 3 == 0 and integers % 5 == 0:
            print("FizzBuzz") 
        elif integers % 3 == 0:
            print("Fizz") 
        elif integers % 5 == 0:
            print("Buzz") 
        else:
            print(integers)            
        pass
