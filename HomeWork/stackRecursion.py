# define ArrayStack by using list 
#-----------------------------------------------
class ArrayStack:

    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data) 

    def is_empty(self):
        return len(self._data) == 0

    def push(self,e):
        self._data.append(e)
    
    def top(self):
        if self.is_empty():
            raise ValueError
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise ValueError 
        return self._data.pop()
#-------------------------------------

#--------------------------------------- check duplication
def deleteDuplication(arr):
    inputStack = ArrayStack()  # ArrayStack for save the word.
    resultStack = ArrayStack() # ArrayStack for save result.

    for item in arr: # push whole word to inputStack.
        inputStack.push(item)
    

    while True:
        resultStack.push(inputStack.pop()) # push the top node of inputStack to resultStack.
        firstWord = resultStack.top() # save what was the top of the resultStack in cycle
        while inputStack.__len__() > 0: 
            if firstWord == inputStack.top(): #if word is same as fistWord it means duplicated  
                inputStack.pop()  # so delete the word
            else: # if the word is nor duplicated
                resultStack.push(inputStack.pop()) # push to resultStack 
        while resultStack.top() != firstWord:
            inputStack.push(resultStack.pop()) #return words while firstWord become the first node.
        if inputStack.is_empty(): # if inputStack is empty, it means whole process is finished so break.
            break

    result = "" # to return in String type, make empty string variable

    while True: # put every word in resultStack to result
        result = result + resultStack.pop()
        if resultStack.is_empty():
            break

    return result #return the result 
#--------------------------------------------------



def main():
    while True:
        print("Input = ", end='')
        arr = input()
        print( "Reasult = " + deleteDuplication(arr))
        print()
        print()


if __name__ == "__main__":
    	main()
