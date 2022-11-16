def duplicate_check(list):
    print("the list has " ,len(list))
    newlist = set(list)
    print("the set has " ,len(newlist))
    if newlist == list:
        print("no duplicates are found")
    elif newlist != list:
        print("duplicates are found")
        print("the list without duplicate ARE:")
        print(set(list))
        
check = duplicate_check(list = [1,2,3,3])
