""" Google Question
Given an array = [2,5,1,2,3,5,1,2,4]:
It should return 2

Given an array = [2,1,1,2,3,5,1,2,4]:
It should return 1

Given an array = [2,3,4,5]:
It should return undefined """

""" Bonus... What if we had this:
 [2,5,5,2,3,5,1,2,4]
return 5 because the pairs are before 2,2 """


# Approach without hashtable
# Complexity = O(n^2)
# Space Complexity = O(1)
def func(mylist):
    for i in range(0, len(mylist)):
        for j in range(i+1, len(mylist)):
            if mylist[i] == mylist[j]:
                return mylist[i]
    return 0


# Approach with hashtable
# Complexity = O(n)
# Space Complexity = O(n) worst case
def recurring_character(mylist):
    my_dict = {}
    for i in range(0, len(mylist)):
        if mylist[i] in my_dict:
            return mylist[i]
        else:
            my_dict[mylist[i]] = i
    return 0


# Example
if __name__ == "__main__":
    mylist = [2, 5, 5, 2, 3, 5, 1, 2, 4]
    test = recurring_character(mylist)
    print(test)
