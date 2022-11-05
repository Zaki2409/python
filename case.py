#Write a program to check whether the given input is digit or lowercase character or uppercase 

name = input("write any word")

for i in name:
    k = i.isupper()
    if k == True:
        print("true")
    else:
        print(false)