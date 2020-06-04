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


def recurring_character(mylist):
    my_dict = {}
    for i in range(0,len(mylist)):
        if mylist[i] in my_dict:
            return mylist[i]
        else:
            my_dict[mylist[i]] = i
    return 0


mylist = [2,1,1,2,3,4,5]
test = recurring_character(mylist)
print(test)


