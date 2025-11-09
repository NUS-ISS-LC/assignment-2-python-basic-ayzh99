def find(numList, target):
    index = {} #dict to store {num: index} of the numbers we have checked

    for i, num in enumerate(numList): #enumerate(numList) - loop over a list and get both the index and the value at the same time.
        difference = target - num
        if difference in index:
            return [index[difference], i]
        else:
            index[num] = i 

print(find([2,7,11,15], 9)) 


