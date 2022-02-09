"""""" Notes for week 5 """"""
# strings - sequences of characters. ' ' or " "
# everything inside is part of a string.

# Lists - sequences of any object in []
# [1,2,3,4]
# ["hello", "world"]
b = ["hello", "world", 1, 2, "hi"]
len(b)
# 5
# len() returns the number of objects in a list
# + concatenation
["hello"] + ["world"]
"helloworld"

# list concatenation
a = [1,2,3]
b = [4,5,6]
c = a + b
c = [1,2,3,4,5,6]

#"hi" * 3 = "hihihi"
["John", "Paul"] * 3 # repeats 3 times

for name in ["alice", "bob", "charlie"]
    # loops through each name

a = "super"
for letter in a:
    print(letter)
s
u
p
e
r

# indexing <string>[int]
"hello" [1] # will print e
#indexing starts at zero.
# to get the last element print len() then subtract 1.

a = "hello"
third_char = a[2] # prints l

days = ["mon", "tues", "wed"]
day = days[1]
days[-1] = days[len(days)-1]
#syntactic sugar

#substring- a portion of a list
#slicing- the process of getting individual objects from the list
# <string>[<start>:<end>:<step>]
"hello, world!"
h = a[0:5] #hello
w = a[7:] #world!
all = a[:] #hello, world!
b = a[12:6-1] #!dlrow
backwards = a[12::-1] # or a[::-1]
                    #!dlrow ,olleh
#when you slice a list it always returns a list even if its single
b = ["john", "paul", "george,"]
