def ispalindrome(str):
    z = len(str)/2
    y = len(str)
    for i in range(0 , int(z)):
        if str[i] == str[y-i-1]:
            return True
        else:
            return False

print(ispalindrome("kiik"))
