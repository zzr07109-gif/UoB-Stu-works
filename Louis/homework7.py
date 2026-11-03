from datetime import date
import random
string1 = "I have bought 3 footballs for 450.00 pound, in the year 2023."
print("Output1: ",string1[0])

string2 = "I have bought 3 footballs."
print("Output2: ",len(string2))

print(date.today())

print(random.randint(1,100))

a = list(map(int,input("input two numbers gap each with space: ").split()))
b = max(a[0],a[1])
s = min(a[0],a[1])
print(random.randint(s,b))

original_number = list(map(float,input("input two numbers gap each with space: ").split()))
print(original_number[0]+original_number[1])