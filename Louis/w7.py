import math
infomations = list(input("Enter 3 names, gap each with space: ").split())
for i in range(len(infomations)):
    #pass
    print(f"Name{i+1}: {infomations[i]}")
num = 5.43124131
print(f"{num:.2f}")
info2 = list(map(int,input("Enter the year, quantity, and the price: ").split()))
print(f"I have bought {info2[1]} footballs for {float(info2[2]):.2f} pound, in the year {info2[0]}. ")
