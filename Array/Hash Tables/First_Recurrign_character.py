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


def func(mylist):
    count_dict = {}
    for i in mylist:
        if i not in count_dict.values():
            count_dict[i] = 1
        else:
            count_dict[i] = count_dict[i] + 1
    return count_dict
    