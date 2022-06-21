# ex1
# print the sum of 23424 and 78211
print(23424 + 78211)
# given the list in the variable "list", print the 
# element "3" from the list by accesing it's index
list = [1, 2, 3, 4]
print(list[2])

# given the variables "list1" and "list2" that each contain a 
# list print a list containing all the elements of list1 & list2
# the output should print [8, 7, 6, 1, 3, 4]
list1 = [1, 3, 4]
list2 = [8,7,6]
print(list2 + list1)



#ex 2
# write a program that based on the value in the variable "a"
# prints a message showing either "value is greater than 3" or 
# "value is lower than 3"
a = 5
if a > 3: print("value is greater than 3")
else: print("value is lower than 3")

#ex 3
# print on a separate line using a for statement
# all the numbers in the list
a = [3, 2, 1]
for nums in a:
    print(nums)


#ex 4
# implement the function 'greet_person' so that it
# displays the message 'Hello Peter' where 'Peter'
# is the value contained in the parameter 'name'
def greet_person(name):
    print("Hello" + name)


greet_person("Peter") # should print 'Hello Peter'
greet_person("George") # should print 'Hello George'


#ex 5
# make the sum of all the numbers in the list
# do not use the built in 'sum' function
def sumOflist(a):
    total = 0
    for val in a:
        total = total + val
    return total
a = [1, -8, 3, 4] 
print(sumOflist(a))

def sumOflist(a):
    total = 0
    for val in  a:
        total = total + val
    return total
a = [1, -8, 3]    # should print -4
print(sumOflist(a))


#ex 6
# print the highest number in a list using
# a for loop (do not use the built in max function)
a = [1, -8, 3, 4] # should print 4
for nums in a:
    print(a[-1])
    break

a = [1, -8, 3]    # should print 3
for nums in a:
    print(a[-1])
    break



#ex 7
# write if else statements that check if the string in the
# variable 'email' is a valid and if not it should display
# that it is either missing the '@' sign or the '.' sign


# uncomment the variable that you want to test with
email = "peter@codecool.com" # should print 'valid email'
#email = "peter.codecool.com" # should print 'missing at sign'
#email = "peter@codecool"     # should print 'missing dot sign'
if ('@') not in email:
    print('missing at sign')
elif ('.') not in email:
    print('missing dot sign')
else:
    print('valid email')

#ex 8
# given the 2 strings (a & b) print many characters each have
# do not use the "input" function, it will not work, always 
# hard code the values
a = "hello"
b = "world"
# should print 10
print(len(a+b))

a = ""
b = "1234"
# should print 4
print(len(a+b))


#ex 9
# write code that prints the sum of all the numbers in a list,
# if the sum is negative print the absolut value
a = [1, 8, 3, 4]
# should print 16
print(abs(sum(a)))


a = [1, -8, -3, 4]
# should print 6
print(abs(sum(a)))


#ex 10
# write code that prints the sum of all the numbers in a list,
# if any number is negative, make it positive before adding it
a = [-1, -2] # => [1, 2]
# should print 3
print(abs(sum(a)))


a = [1, -8, -3, 4] # => [1, 8, 3, 4]
# should print 16
abs = [abs(x) for x in a]

def summ(a):
    total = 0
    for x in a:
        total = total = x
    return total
print(sum(abs))


#ex 11
# write a code that prints the sum of
# all the even & positive numbers in a list
a = [2, -8, -3, 4, 3]
# should print 6
def sum_positive_even(a):
    return sum(filter(lambda x: x > 0 and x % 2 == 0, a))
def sum_positive_even_v2(a):
    sum = 0
    for i in a:
        if i % 2 == 0 and i > 0:
            sum += i
        return sum
print(sum_positive_even(a))


a = [-1, -8, -3, -4]
# should print 0
def sum_positive_even(a):
    return sum(filter(lambda x: x > 0 and x % 2 == 0, a))
def sum_positive_even_v2(a):
    sum = 0
    for i in a:
        if i % 2 == 0 and i > 0:
            sum += i
        return sum
print(sum_positive_even(a))

#ex 12
# write code that displays the sum of all the even
# numbers between 1 and a number in the variable "a"

a = 5
# should print 6 (2+4)
def sum_even():
    return sum(i for i in range(1, 5 + 1) if i % 2 == 0)
print(sum_even())

a = 4
# should print 6 (2+4)
def sum_even():
    return sum(i for i in range(1, 4 + 1) if i % 2 == 0)
print(sum_even())

#ex 13
# write the code that returns the sum of all the numbers
# in 2 lists
a = [1, 8, 3, 4]
b = [3, 4]
# should print 23
print (sum(a + b))


#ex 14
# write the code that transforms a string to a list
# where the elements of the list are separated by 
# a pattern you have to recognize


# HINT: use the split() function
a = "11|12|78"
b = a.split("|")
print(b)

b = "11*|*22*|*8"
# should print: ['11', '22', '8']
d = b.split("*|*")
print(d)


c = """11
22
33"""
# should print: ['11', '22', '8']


#ex 15
# write the code that prints each letter of the string in 
# the variable 'name' only if it is part of the list
# contained in the variable 'characters_to_show'
# HINT: use a for loop to iterate through all the letters
# and in each iteration check if that letter is part of
# the list characters_to_show

characters_to_show = ["e", "a"]
name = "peter"
# should print:
# e
# e
characters_to_show = ["e", "n"]
name = "Andr3i"
# should print
# n


#ex 16
# write a function that receives as a parameter 2 numbers
# than returns the sum of those numbers which is printed
def calculator():
    input1 = input("pick a number: ")
    input2 = input("pick second number: ")
    print("the sum is: " + sum(input1 + input2))
    return calculator
calculator()


#ex 17
a = {
  "nume": {
    "familie": "dragoe",
    "mijlociu": "maniu",
    "mic": "cipi",
    "nickname": {
      "copilarie": "speedy",
      "adolescenta": "gigel"
    }
  },
  "varsta": {
    "luna": 7,
    "ziua": 14,
    "an": 1987
  },
  "hobby": ["fotbal", "citit", "pescuit"],
  "ticTacToe": [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ],
  "loc_munca": "codecool",
  "in_a_relationship": False
}
# scrieti printul sa apara 'codecool' accesand cheile din dictionarul in variabila 'a'
# scrieti printul sa apara 'dragoe' accesand cheile din dictionarul in variabila 'a'
# scrieti printul sa apara '9' accesand cheile din dictionarul in variabila 'a'

# incrementati cu 1 luna in care s-a nascut
# adaugati un nou nickname, pentru perioada 'adulta'
# adaugati un hobby nou
















