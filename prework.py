#Question 1 Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
    print(hello_name)

#Question 2 Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():

    for number in range(1, 101, 2):
        print(number)
first_odds()

#Question 3 Please write a Python function, max_num_in_list to return the max number of a given list. 
def max_num_in_list(a_list): #This line is defining a function

    if not a_list: 
        return None # Determining whether or not the list is empty

    else:
        return max(a_list)

#Question 4 Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).


def is_leap_year(a_year):

    return (a_year % 4 ==0 and a_year % 100 != 0) or (a_year % 400 == 0)

year_to_check = 2024
result = is_leap_year(year_to_check)
print(f"{year_to_check} is a leap year: {result}")

#Question 5 Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_constructive(a_list):
    if not a_list or len(a_list) == 1:
        return False 
    sorted_list = sorted(a_list)

    return all(sorted_list[i] + 1 == sorted_lost[i + 1] for i in range (len(sorted_list) - 1))

consecutive_list = [2, 3, 4, 5, 6]
result = is_consecutive(consecutive_list)
print(f"The list {cosecutive_list} is consecutive: {result}")

non_consecutive_list = [1, 2, 4, 5]
result = is_consecutive(non_consecutive_list)
print(f"The list {non_consecutive_list} is consecutive: {result}")