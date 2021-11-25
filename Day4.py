'''
You are given a list of integers having both negative and positive values, except for one integer which can be negative or 
positive. Create a function to find out that integer.

Examples
lonely_integer([1, -1, 2, -2, 3]) ➞ 3
# 3 has no matching negative appearance.

lonely_integer([-3, 1, 2, 3, -1, -4, -2]) ➞ -4
# -4 has no matching positive appearance.

lonely_integer([-9, -105, -9, -9, -9, -9, 105]) ➞ -9

[1,9,7,-1,-9,-7,-55,-55,100,-100] -55

[1, -1, 2, -2, 3] -> 3
[-3, 1, 2, 3, -1, -4, -2]  -> -4
[-9, -105, -9, -9, -9, -9, 105]


'''

def lonely_integer(lst):
    return sum(set(lst))

print(lonely_integer([-9, -105, -9, -9, -9, -9, 105]))







'''
Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and 
returns a dictionary of objects like { "name": "John", "top_note": 5 }.

Examples
top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }

top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }

top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }
'''

def dict_creation(x):
    n = x['name']
    l = x['notes']
    m = max(l)
    d = {"name":n, "top_note":m}
    return d

print(dict_creation({"name": "John", "notes":[3,6,5]}))

def topnote(dicts):
    dict_ret = {}
    dict_ret['name'] = dicts['name']
    dict_ret['topnote'] = max(dicts['notes'])
    return dict_ret


'''
7days
15days


C, C++, Java 
(ReactJs, Javascript, NUmy, Pandas)

1hr :- coding (yt+websites) (day1.js,day1.py)

30days

22-8

22(js -  project)

#day1 #15daysoflearning #30dayscodingchallenge

#Sandeep #Aditya

summarize

29th Nov

Sat :- Topic
Duration :- 7/15/30
Hashtags :- #day1 #15daysoflearning #30dayscodingchallenge
Mention :-
Github:- 

7 - 7
15 - 15
30 - 30  


'''


'''
Write a Python program to generate the next 15 leap years starting from a given year.
 Populate the leap years into a list and display the list.
'''
#lex_auth_012693797166096384149

def find_leap_years(given_year):
    list_of_leap_years = []
    count = 0

    while(count<15):
        if given_year%4 == 0 or given_year%400 == 0 and given_year%100 ==0 :
            list_of_leap_years.append(given_year)
            given_year = given_year+1
    return list_of_leap_years
    


list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)

'''
Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number
 possible by concatenating the list of numbers. 
Note: Assume that all the numbers are two digit numbers.
 

Sample Input

23,34,55

Expected Output

553423

'''
def create_largest_number(number_list):
    s = ""
    for i in range(len(number_list)):
        m = max(number_list)
        s = s + str(m)
        number_list.remove(m)
    return int(s)


'''
Write a method that returns array of all the numbers from 1 to an integer argument.
 But for multiples of three use “Fizz” instead of the number and for the multiples of five use “Buzz”. For numbers which are multiples of both three and five use “FizzBuzz”.

Example
fizzBuzz(10) ➞ [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"]

fizzBuzz(15) ➞ [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]


Create a function that takes a number n and checks if each digit is divisible by the digit on its left. Return a boolean array depending on the condition checks.

Examples
divisible_by_left(73312) ➞ [False, False, True, False, True]
# no element left to 7 = False
# 3/7 = False
# 3/3 = True
# 1/3 = False
# 2/1 = True

divisible_by_left(1) ➞ [False]

divisible_by_left(635) ➞ [False, False, False]
Notes
The array should always start with False as there is no digit to the left of the first digit.


Create a function that takes a string and returns the letters that occur only once.

Examples
find_letters("monopoly") ➞ ["m", "n", "p", "l", "y"]

find_letters("balloon") ➞ ["b", "a", "n"]

find_letters("analysis") ➞ ["n", "l", "y", "i"]
Notes
The final list should not include letters that appear more than once in the string.
Return the letters in the sequence they were originally in, do not sort them.
All letters will be in lowercase.

'''