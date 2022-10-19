#!python3


def getIntegers(myList):
    # myList : expected list or tuple
    # iterate through myList and add all the integers to the new list
    integers = [myList]

    return integers

def getFactor(myList,factor):
    # myList : expected list or tuple
    # factor : integer
    # iterate through the list and add the number to the list if
    # it is a factor of the number
    factors = []
    factorlist = []
    for a in myList:
        if 1%a == factors:
            factorlist.append(factors)

    return factorlist

def getNegatives(myList):
    # myList : expected list or tuple
    # iterate through myList and add all the negative numbers to the new list
    negatives = []
    for a in myList:
           if a < 0:
               negatives.append(a)
    

    return negatives

def getIntersection(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # return a list of numbers that is in both lists
    # the intersection of the 2 number sets
    common = []
    for a in list1:
        if a in list2:
            common.append(a)

    return common

def getUnion(list1,list2):
    union = []
    for a in list1:
        union.append(a)
    for b in list2:
        if b not in list1:
            union.append(b)
    return union   

def getMerge(list1,list2):
    for b in list2:
        if b not in list1:
            union.append(b)
    merge = list.copy()

    return merge


def main():
    easy1 = [5,10,15,2,4,6,8]
    easy2 = [-2,-4,-6,2,4,6,0.1]
    numbers1 = [3,5,8,12,11,19,10,7,2,15,25,34,16,32,50,60,100,-3,0.25]
    numbers2 = [3,7,11,15,19,23,27,31,35,39,44,50]
    print(getUnion(numbers1,numbers2))

if __name__ == "__main__":
    main()