"""
Name: Maddie Reed
hw5.py

Problem: This program reverses name order, splits a domain name, gives the
initials of a name and list of names, gives every third letter of a sentence
the average length of words in a sentence, and translates sentences into
pig latin

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    full_name = input("enter a name (first last): ")
    list_name = full_name.split()
    reversed_name = list_name[1] + ', ' + list_name[0]
    print(reversed_name)


def company_name():
    domain = input("enter a domain: ")
    split_domain = domain.split('.')
    company = split_domain[1]
    print(company)


def initials():
    students = eval(input("how many students are in the class? "))
    for i in range(students):
        prompt = "what is the name of student " + str(i + 1) + "?"
        student_name = input(prompt)
        split_name = student_name.split()
        first_name = split_name[0]
        last_name = split_name[1]
        first_letter = first_name[0]
        last_letter = last_name[0]
        print(first_letter + last_letter)


def names():
    name_string = input("enter a list of names: ")
    name_list = name_string.split(',')
    name_num = len(name_list)
    for i in range(name_num):
        full_name = name_list[i]
        name = full_name.split()
        first_name = name[0]
        last_name = name[1]
        initial = first_name[0] + last_name[0]
        print(initial, end=' ')


def thirds():
    sentence_num = eval(input("enter the number of sentences: "))
    sentence_list = []
    for i in range(sentence_num):
        prompt = "enter sentence " + str(i + 1) + ": "
        sentence = input(prompt)
        sentence_list.append(sentence)
    for i in sentence_list:
        stop = len(i)
        each_sent = i[0:stop:3]
        print(each_sent)


def word_average():
    sentence = input("enter a sentence: ")
    sentence_list = sentence.split()
    word_num = len(sentence_list)
    letter_num = 0
    for i in range(word_num):
        word = sentence_list[i]
        letter_num = letter_num + len(word)
    average = letter_num / word_num
    print(average)


def pig_latin():
    sentence = input("enter a sentence to convert to pig latin: ")
    sentence_list = sentence.split()
    for word in sentence_list:
        length = len(word)
        pig = word[1: length + 1] + word[0] + "ay"
        print(pig, end=" ")


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
