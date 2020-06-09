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

# To pop elements out of the heap.
print(heapq.heappop(x))
print(x)

# Used to pop and push the element in same time
print(heapq.heappushpop(x, 34))
print(x)

# Used to get n largest elements in heap.
print(heapq.nlargest(2, x))

# Used to get n smallest elements in heap.
print(heapq.nsmallest(2, x))
