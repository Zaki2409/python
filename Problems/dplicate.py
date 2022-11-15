def duplicate(list):
    print(len(list))
    newlist = set(list)
    print(len(newlist))
    if newlist == list:
        print("no duplicate found")
    elif newlist != list:
        print("duplicate entries are found")

duplicate(list= [ 1 ,2, 3])