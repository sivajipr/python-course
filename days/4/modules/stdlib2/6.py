from collections import deque

d = deque(["task1", "task2", "task3"])
print d

d.append("task4")
print d

print d.popleft()
print d

d.appendleft('task0')
print d


