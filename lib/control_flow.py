#!/usr/bin/env python3

def admin_login(username, password):
     if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
     else:
        return "Access denied"
    

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
    
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
   

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
    
print(admin_login("admin", "12345"))  
print(admin_login("user", "password")) 

print(hows_the_weather(30))  
print(hows_the_weather(60)) 
print(hows_the_weather(90))  
print(hows_the_weather(70))  

print(fizzbuzz(3)) 
print(fizzbuzz(5))
print(fizzbuzz(15))  
print(fizzbuzz(7))  

print(calculator("+", 3, 4))  
print(calculator("-", 10, 4)) 
print(calculator("*", 2, 5))  
print(calculator("/", 8, 2)) 
print(calculator("%", 8, 2))  