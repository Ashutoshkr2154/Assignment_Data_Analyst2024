#!/usr/bin/env python
# coding: utf-8

# #### Assignement 3 part II 
# ##### Name - Ashutosh kumar 

# ##### 1. Write a Python function that takes a list of numbers as input and returns the sum of all even numbers in the list.

# In[3]:


def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num %2 ==0)

## Drivers code 
numbers = [1 ,2, 3,4,5,6]
result = sum_of_even_numbers(numbers)
print(result)


# ##### 2. Create a Python function that accepts a string and returns the reverse of that string.

# In[4]:


def reverse_string(s):
    return s[::-1]

## Drivers Code 
input_string = "Hello"
reversed_string = reverse_string(input_string)
print(reversed_string)


# ##### 3. Implement a Python function that takes a list of integers and returns a new list containing the squares of each number

# In[5]:


def square_numbers(numbers):
    return[num ** 2 for num in numbers]
## Drivers Code 
numbers = [1, 2,3, 4, 5]
squared_numbers = square_numbers(numbers)
print(squared_numbers)


# ##### 4. Write a Python function that checks if a given number is prime or not from 1 to 200.

# In[6]:


def is_prime(n):
    if n < 2 : 
        return False
    for i in range(2 , int(n** 0.5) + 1):
        if n%i == 0 : 
            return False 
        return True 
## Drivers Code 
for num in range(1 , 201):
    if is_prime(num):
        print(f"{num} is a prime number")


# ##### 5. Create an iterator class in Python that generates the Fibonacci sequence up to a specified number of terms.

# In[15]:


class FibonacciIterator : 
    def __init__(self , n_terms):
        self.n_terms = n_terms 
        self.current = 0 
        self.next= 1 
        self.count = 0 
        
    def __iter__ (self):
        return self
    
    def __next__(self):
        if self.count >= self.n_terms:
            raise StopIteration
        fib_number = self.current 
        self.current , self.next = self.next , self.current + self.next 
        self.count += 1 
        return fib_number 
    
## Drivers Code
fib_sequence = FibonacciIterator(10)
for num in fib_sequence: 
    print(num , end =" ")


# ##### 6. Write a generator function in Python that yields the powers of 2 up to a given exponent.
# 

# In[16]:


def power_of_two(max_exponent):
    for exp in range (max_exponent + 1 ):
        yield 2 ** exp 
        
## Drivers Code 
for power in power_of_two(5):
    print(power)


# ##### 7. Implement a generator function that reads a file line by line and yields each line as a string.
def read_file_line_by_line(file_path):
    with open(file_path , 'r')as file :
        for line in file : 
            yeild line.strip()
            ## Strip removes any leading /trailling whitespace 
##Drivers code 
for line in read_line_by_line('example.txt'):
    print(line)
# ###### 8. Use a lambda function in Python to sort a list of tuples based on the second element of each tuple.

# In[21]:


## list of tuples 
tuples_list = [(1,3),(4,1) , (5,2) , (2,4)]

## Sort using a lambda function 
sorted_tuples = sorted(tuples_list , key = lambda x: x[1])

## output the sorted list 
print(sorted_tuples)


# ##### 9. Write a Python program that uses `map()` to convert a list of temperatures from Celsius to Fahrenheit.

# In[24]:


## Function to convert Celcius to Fahrenheit 
def celcius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32 

## List of temprature in celcius 
celcius_temps = [0 , 20 , 37 , 100]

## Use map() to apply the conversion fuction to each temprature 
fahrenheit_temps = list(map(celcius_to_fahrenheit , celcius_temps))

## Output the converted tempratures 
print(fahrenheit_temps)



# ##### 10. Create a Python program that uses `filter()` to remove all the vowels from a given string.

# In[25]:


## Function to check if a character is not a vowel 
def is_not_vowel(char):
    return char.lower() not in 'aeiou'

## Input string 
input_string = "Hello, World"

## Using filter() to remove vowels 
filtered_string = ''.join(filter(is_not_vowel , input_string))

## Output the result 
print(filtered_string)


# ###### 11.Answer --> Here ,is the python program that uses lambda and map() to solve the problem . 
# 

# In[26]:


## List of orders 
orders = [
    [34587, "Learning Python, Mark Lutz", 4, 40.95],
    [98762, "Programming Python, Mark Lutz", 5, 56.80],
    [77226, "Head First Python, Paul Barry", 3, 32.95],
    [88112, "Einführung in Python3, Bernd Klein", 3, 24.99]
]

## lambda function to calculate the total price and apply the 10$ increase if the total is less than 100$
calculate_total = lambda order: (order[0] , round(order[2] * order[3] + (10 if order[2] * order[3] < 100 else 0 ) , 2))

## Use map () to apply the lambda function to each other 
result = list(map(calculate_total , orders))

## output the result 
print(result)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




