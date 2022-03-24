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

a = "super" # very important
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
third_char = a[2] # prints l as a string

days = ["mon", "tues", "wed"]
day = days[1]
days[-1] = days[len(days)-1]
#syntactic sugar

#substring- a portion of a list
#slicing- the process of getting individual objects from the list, still a list
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

def user_name():
    first_name = input("enter first name: ")
    last_name = input("enter last name: ")
    first_letter = first_name[0]
    last_seven = last_name[:8]
    user = first_letter + last_seven
    print("username: " + user)

# list methods
#start a list with []
a = []
a.append("monday") #use this method to add to lists
a = a + ["tuesday"]

# string methods
a = hello
a.upper() # returns new string, all uppercase "HELLO"
a.lower() # returns new string, all lowercase "hello"
a.capitalize() # Hello capitilizes first word
a.title() # Hello capitalizes each word
a.count(e) # 1 (theres one e in hello)
a.find(l) # 2 returns the index value of where it finds the object first
a.rfind(l) # 3 finds from the right
#.find will return a negative number if the object is not found
a.replace('l', 'f') # heffo <what you want to replace, replacement>

" ".join(days) # return the list with a space between each element
a = "hello"
a.center(0)
"hello"
a.center(10) #resulting string is 10 characters
a.ljust(10) #
a.rjust(10)
a.strip() #takes the spaces out in front and back
a.lstrip()
a.rstrip()
a.split() #splits a string on a certain character, defaults spaces

# encoded "A" is 010010
# unicode is the standard code that almost every computer uses.
# = A is 65, B is 66, C is 67 and so on.
#ord() = ordinal, tells us unicode value of a letter.
ord('a') # = 97
chr(97) # = a

def encode():
    ordinals = []
    word = input("enter a word: ")
    for letter in word:
        num = ord(letter)
        ordinals.append(num)
    output_string = " ".join(ordinals)
    print(output_string)


def decode():
    numbers = input("enter encoded message: ")
    number_list = numbers.split()
    for number in number_list:
        my_string = ""
        letter = chr(eval(number))
        my_string = my_string + letter
    print(my_string)


#int(<expresstion>) makes int
#float(<expr>) makes float
#str(<expr>) makes string
#eval(<expr>)
# don't convert numbers with a leading 0

"hi my name is {}".format("Eric") # adds to a string inside curly brackets
"my name is {} and i am {} years old".format("eric", 7) # default is to put each in order
"my name is {1} and i am {0} years old".format("eric", 7) # switches the inputs
# fill align(<^>) width(int)
"my name is {0:*>10} and i am {1} years old".format("eric", 7) #width is how many characters
"my name is ***eric*** an i am 7 years old"
dollars = 12
cents = 4
"I have ${}.{}".format(dollars, cents)
"I have $12.4"
"I have ${}.{:0>2}".format(dollars, cents)
"I have $12.04"
money = 0.10
"I have ${}".format(money)
'I have ${:2f}'.format(money)
'I have '

#open function opens a file
# open(<filename>, <mode>) 220 modes are "r"/"w"
# r for read, w for write
my_file = open("data.txt", "r")
my_file.read() #returns a single string that is the entire file.
my_file.readline() # returns one line "string with a /n" at the end
my_file.readlines() # returns each line in the file with a "/n" at the end of each line

my_file = open("data.txt", "r")
data = my_file.read()
data = data.replace('e', '$')
print(data)
my_file.close()

def print_file_lines():
    my_poem = open('poem.txt', 'r')
    for i in range(5):
        print(my_poem.readline(), end="")
    print_file_lines()
input_file = open("poem.txt", 'r')
ouput_file = open('output.txt', 'w')
print(input_file.read(), file=ouput_file)




