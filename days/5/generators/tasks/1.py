import time
task_list = []

def task1():
    while True:
        print 'task1 ...'
        yield

def task2():
    while True:
        print 'task2 ...'
        yield

def task3():
    while True:
        print 'task3 ...'
        yield


def add_task(task):
    global task_list
    task_list.append(task)

def run_task(task):
    task.next()

def mainloop():
    while True:
	time.sleep(1)
        for task in task_list:
            run_task(task)

add_task(task1())
add_task(task2())
add_task(task3())

mainloop()
