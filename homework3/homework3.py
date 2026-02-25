# 3 -- Print Functions
# -- 3.1 Say Goodbye --
def say_goodbye(Nicole):
    print("Goodbye,", Nicole)

# -- 3.2 Area of a Circle --
def print_area(radius):
    pi = 3.14
    area = pi * radius ** 2
    print("The area of the circle is:", area)

# 4 -- Return Functions
#  4.1 Return Functions
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a ,b):
    return a / b

# 5 -- Conditions
# -- 5.1 What Should I Wear? --
def min_max_temps(readings):
    minimum = min(readings)
    maxiumum = max(readings)
    return (minimum, maxiumum)
temps = [15, 14, 17, 20, 23, 28, 20]
print(min_max_temps(temps))

# -- 5.2 Check if it's the Weekend --
def is_weekend(day):
    if day == 6 or day == 7:
        return True
    else: 
        return False
print(is_weekend(6)) # True
print(is_weekend(3)) # False

# -- 5.3 Fuel Efficiency Calculator
def fuel_efficiency(distance, gallons):
    return distance / gallons

# -- 5.4 Secret Code --
def secret_code(num):
    last_digit = num % 10
    remaining = num // 10
    # find how many digits are in remaining
    multiplier = 1
    temp = remaining
    while temp > 0:
        multiplier *= 10
        temp //= 10
    return last_digit * multiplier + remaining 

# 6 -- Loops
# -- 6.1 Oski Stole Your Power --
def power (x, y):
    result = 1
    for i in range(y):
        result *= x
    return result

# -- 6.2.1 For Loops --
def min_for(nums):
    minimum = nums[0]
    for num in nums:
        if num < minimum:
            minimum = num
        return minimum

def max_for(nums):
    maximum = nums [0]
    for num in nums:
        if num > maximum:
            maximum = num
        return maximum
    
# -- 6.2.2 While Loops --
def min_while(nums):
    minimum = nums[0]
    i = 0
    while i < len(nums):
        if nums[i] < minimum:
            minimum = nums[i]
        i += 1
    return minimum

def max_while(nums):
    maxiumum = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] > maximum:
            maximum = nums[i]
        i += 1
    return maximum

# -- 6.3 Calculate the Sum of Digits --
def sum_digit(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

x = 2
y = 3
result = power(x, y) # 2 raised to the power of 3

print(f"the Result of Oski Stole Your Power (5.1) with x = {x} and y = {y} is {result}.")