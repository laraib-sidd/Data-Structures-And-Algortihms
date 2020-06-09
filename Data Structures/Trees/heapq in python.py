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

# To push elements in the heap.
heapq.heappush(x, 0)
print(x)

print(heapq.heappop(x))
print(x)

# Used to pop and push the element in same time
print (heapq.heappushpop(x, 5)) 
print(x)