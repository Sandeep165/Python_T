'''
Inftq Ac:- 
Github :- 
LinkdIN :- 
'''

# Naming convention

Name = "Harry"
Na_me = "Sam"
_Name = "code"
string = "I love python"
str = "India"

num1 = 25
int = 54


cities = ["mumbai","delhi","pune"]

list2 = [1,2,3,4,20.5,"india",["mumbai",[101,102,103]]]
print(list2[6][1][2])

myList = ["india","Aus","NZ","SA",["mumbai","delhi","pune",[1,2,3,4,[25.25]],"Apple"],["sam","john"],"python",["java"]]


# NZ ,mumbai, pune, 4, 25.25 , john , python , java , [25.25]

print(myList[2])
print(myList[4][0])
print(myList[4][2])
print(myList[4][3][3])
print(myList[5][1])
print(myList[6])
print(myList[7][0])
print(myList[4][3][4][0])


#lex_auth_012693780491968512136

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    
    five_needed = int(rupees_to_make/5)
    one_needed = rupees_to_make%5 
    
    if five_needed <= no_of_five and one_needed <= no_of_one:
         print("No. of Five needed :", five_needed)
         print("No. of One needed  :", one_needed)
         
    elif five_needed > no_of_five:
        total = no_of_five * 5 
        one_needed = rupees_to_make - total
        
        if one_needed <= no_of_one:
            print("No. of Five needed :", no_of_five)
            print("No. of One needed  :", one_needed) 
        else:
            print(-1)
    else:
        print(-1)
            


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28,8,5)





#lex_auth_012693782475948032141

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    if food_type in ['V','N'] and quantity_ordered >= 1 and distance_in_kms > 0:
        if food_type == 'V':
            bill_amount += 120*quantity_ordered
        elif food_type == 'N':
            bill_amount += 150*quantity_ordered
        
        if distance_in_kms>6:
            bill_amount += (distance_in_kms-6)*6 + 9
        elif distance_in_kms>3 :
            bill_amount += (distance_in_kms-3)*3
            
        return bill_amount
        
    else:
        bill_amount = -1
    return bill_amount


#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)

'''
You are given a list of integers having both negative and positive values, except for one integer which can be negative or positive. Create a function to find out that integer.

Examples
lonely_integer([1, -1, 2, -2, 3]) ➞ 3
# 3 has no matching negative appearance.

lonely_integer([-3, 1, 2, 3, -1, -4, -2]) ➞ -4
# -4 has no matching positive appearance.

lonely_integer([-9, -105, -9, -9, -9, -9, 105]) ➞ -9



Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a dictionary of objects like { "name": "John", "top_note": 5 }.

Examples
top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }

top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }

top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }
'''

