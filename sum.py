data ="10 20 30 40"
numbers=data.split() #split the string into parts
total=0
for n in numbers:
    total += int(n)
    print("sum of all numbers:",total)