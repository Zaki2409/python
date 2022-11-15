lower = 100 
upper = 200
print("the prime numbers betwenn", lower , "and", upper, "numbers are: ")
for num in range(lower , upper + 1):
    if (num % 2) != 0 and (num % 3) != 0:
        print(num)
