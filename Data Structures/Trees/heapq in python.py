'''
Heapqueue
Complexity :
Lookup :  O(n)
Insert : O(log N)
Delete : O(log N)
'''

import heapq
x = [2, 32, 213, 12, 321, 312]
heapq.heapify(x)
print(x)

heapq.heappush(x, 0)
print(x)
