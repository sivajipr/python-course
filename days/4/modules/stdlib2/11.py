import heapq

h = [100, 2, 10, 30, 25, 40]

heapq.heapify(h)

print h

heapq.heappush(h, 5)

print h

print 'popped ', heapq.heappop(h)

print h
