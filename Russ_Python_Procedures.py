# Lesson 2.3: Procedures

# Functions (also known as procedures or methods) take input and return an output.
# Programmers use functions all the time! They may seem confusing at first but
# the more you use and make them, the better you'll get!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4141089439/m-48667860

def rest_of_string(s):
    return s[1:]

print rest_of_string('audacity')

# Add your own code and notes here
#Example from lesson 3
#This does nothing, because sum never returns anything
def sum(a,b):
	a = a + b
	return a #this return command has to be added to make this do anything
print sum(2, 123)

# Define a procedure, square, that takes one number 
# as its input, and returns the square of that 
# number (result of multiplying
# the number by itself).
# To help you out, the code for sum(a,b) is below.

def sum(a,b):
    c = a + b
    return c
#

# Define a procedure, sum3, that takes three
# inputs, and returns the sum of the three
# input numbers.
# To help you out, the code for sum(a,b) is below.

def sum(a,b):
    return a + b



def sum3(a,b,c):
	return a + b + c

print sum3(1,2,3)
#>>> 6

print sum3(93,53,70)
#>>> 216

#
#
# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.

#def abbaize(a,b):
#	return a + b + b + a

#print abbaize('a','b')
#>>> 'abba'

#print abbaize('dog','cat')
#>>> 'dogcatcatdog'


# worksession # 3

# # Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.
# for example, when you enter

# print udacify('dacians')

# the output should be the string 'Udacians'
## !!!!The only issue I had with this one was my original print command was indented!!!!
def udacify(s):
	return 'U' + s


# Remove the hash, #, from infront of print to test your code.

print udacify('dacians')
#>>> Udacians

#print udacify('turn')
#>>> Uturn

##>>> Uboat

#!!! NEW SECTION!!!!

# Lesson 2.4: Making Decisions - If Statements

# We'll often write programs that need to make comparisons between values.
# We can do comparisons just like we do in math with the < and > signs.
# We can also do equality comparisons with != (not equal) and ==.
# Comparisons always return a Boolean value (either True or False).

# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-48727556/m-48724313

print 2 < 3
print 21 < 3
print 7 * 3 < 21
print 7 * 3 != 21
print 7 * 3 == 21

# Add your own code and notes here

print "Example 1: Greater-than and less-than comparisons"
print 2 > 1
print 1 > 2
print 5 < 20
print 100 < 19


print "Example 2: Equality and non-equality comparisons"
print 5 == 5
print "hello" == "hello"
print 5 == 10
print 5 == '5' # what do you think will happen here?
print 7 != 10
print 7 != 7


print "Example 3: A demo of what you are about to learn"
if 3 < 5:
    print "Three is definitely smaller than 5!"

if 10 > 20: 
    print "Did you know that 10 is greater than 20!?"
else:
    print "20 is greater than 10"

# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

def bigger(a,b):
	if a > b:   # I failed this part due to missing semicolon 
		return a
	else:
		return b

print bigger(3,2)

#print bigger(2,7)
#>>> 7

#print bigger(3,2)
#>>> 3

#print bigger(3,3)
#>>> 3

# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'


def is_friend(name):
	## return True
	#else:
	#	return False
##!!Above I tried to do it by returning True and False, below it how to do it with a boolean return

	return name[0] == 'D'
		

print is_friend('Diane')
#>>> True

print is_friend('Fred')
#>>> False

# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

def is_friend(name):
	#if name[0] == 'D':
	#	return True
	#if name[0] == 'N':
	#	return False
##!! With or opeartor included below
	return name[0] == 'D' or name[0] == 'N'

print is_friend('Diane')
#>>> True

#print is_friend('Ned')
#>>> True

print is_friend('Moe')
#>>> False


# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(a,b,c):
	if a > b:
		if a > c:
			return a
		else:
			return c
	else:
			if b > c:
				return b
			else:
				return c

print biggest(3, 6, 9)
#>>> 9

#print biggest(6, 9, 3)
#>>> 9

#print biggest(9, 3, 6)
#>>> 9

#print biggest(3, 3, 9)
#>>> 9

#print biggest(9, 3, 9)
#>>> 9


