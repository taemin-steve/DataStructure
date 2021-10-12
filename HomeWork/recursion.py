def my_recursion(arr):
    if len(arr) == 1: # if size of arr is 1, we don't need to check duplication 
        return arr    # so return directly

    firstWorld = arr[0] #Save the first character of the string.
    newArr = arr[1:] # Make new String except first word of arr.
    is_duplicate = False # check duplicate

    for word in newArr: #check if the first letter duplicate with other
        if word == firstWorld:
            is_duplicate = True
            break # if there is duplicated letter we don't need to check others

    if is_duplicate:
        return my_recursion(newArr) # use recursion to do same operation
    else:
        return firstWorld + my_recursion(newArr) # if the first letter doesn't duplicated, it must be included in result


print("Input = bcabc")
print("Reasult = " + my_recursion("bcabc"))
print()
print("Input = cbacdcbc")
print("Reasult = " + my_recursion("cbacdcbc"))
