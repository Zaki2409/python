#CALCULATOR

first = input("write the first number ")
opp = input("write the opperator +,-,*,%,/ ")
second = input("write the second number ")
first = int(first)
second = int(second)
if opp == "+":
    print(first + second)
elif opp == "-":
    print(first - second)
elif opp == "*":
    print(first * second)
elif opp == "%":
    print(first % second)
elif opp == "/":
    print(first / second)
else:
    print("wrong inputs ")



