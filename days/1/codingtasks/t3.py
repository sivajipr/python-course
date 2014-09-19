
#Coding Tasks Group 3
#Source: Exercises from Coursera's "Coding the Matrix: Linear Algebra through Computer Science Applications"
#course by Dr.Philip Klein
#URL: https://www.coursera.org/course/matrix

#Note: You are allowed to modify only the right hand side
#of those expressions which are marked `None'

#Task 1
#Using `range', write a dictionary comprehension: the
#keys of the dictionary are values from 0 to 4 and the
#value corresponding to each key is the square of the key

square_dict = None

#Task 2
#Assume we have a set called colors_d with value say {'red', 'blue', 'green'}
#Using dictionary comprehension, create a dict whose keys are elements of colors_d.
#The value of each key should be equal to that key itself.

colors_d = {'red', 'blue', 'green'}
identity_dict = None

#Task 3
#Assume base = 2 and digits=set(range(base))
#Write a dict comprehension which will map each number from 0 to
# 7 to a list of three separate digits like this:
#0 -> [0, 0, 0]
#1 -> [0, 0, 1]
#2 -> [0, 1, 0]
#3 -> [0, 1, 1]
#4 -> [1, 0, 0]
#5 -> [1, 0, 1]
#6 -> [1, 1, 0]
#7 -> [1, 1, 1]
#That is, each list will be composed of the three digits of the 
#representation of the corresponding key in the given base.
#All three digit keys (in the given base - if the base is say 10,
#the keys should be from 0 to 999) should be enumerated.
#Your code should be general and should work for any `base`.

base = 2
digits = set(range(base))
representation_dict = None



#Please do NOT modify any of the lines below

#--------------------Test Routines-----------------------


def testcase_1():
    r = {0:0, 1:1, 2:4, 3:9}
    return square_dict == r

def testcase_2():
    r = {'red':'red', 'blue':'blue', 'green':'green'}
    return r == identity_dict

def testcase_3():
    r = {0:[0,0,0], 1:[0,0,1], 2:[0,1,0], 3:[0,1,1],
         4:[1,0,0], 5:[1,0,1], 6:[1,1,0], 7:[1,1,1]}
    return representation_dict == r


