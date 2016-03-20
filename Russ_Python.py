# Lesson 2.1: Introduction to Serious Programming

# Programming is grounded in arithmetic, so it's important
# to know how programming languages do simple math.
# Thankfully, Python follows the same math rules people do.
# See if you can predict the output of this code.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4180729266/m-48652460

print 3
print 1 + 1

# Add your own code and notes here
# Different examples of python code
# print 52 * 3 + 12 * 9
# print (52 * 3) + (12 * 9)
# print 52 * (3 + 12) * 9
# Calculate the # of seconds in a year "print 365 * 24 * 60 * 60"
#Write a python program that prints out the number of minutes in seven weeks
print 7 * 7 * 24 * 60

# Write python code to determine how far light travels in centimeters in one nanosecond
# speed of light = 299792458 meters per sec
# meter = 100 centimeters
# nanosecond is 1/1000000000
print 299792458 * 100 * 1.0 / 1000000000


speed_of_light = 299792458 #meters per second
print speed_of_light * 100
billionth = 1.0 / 1000000000
nanostick = speed_of_light * billionth * 100 #in centimeters
print nanostick

speed_of_light
cycles_per_second = 2700000000.0 #2.7 ghz
cycle_distance = speed_of_light / cycles_per_second

cycles_per_second = 2800000000.0 # 2.8 ghz
print cycle_distance
cycle_distance = speed_of_light / cycles_per_second
print cycle_distance

minutes = 30

minutes = minutes + 1

# Write python code that defines the variable
# age to be your age in years, and then prints
# out the number of days you have been alive.
age=37
print age * 365
#Strings
print 'Hello'
print "Hello"
hello = "Howdy"
name = 'Russ'
# Adding several exclamation points by multiplying
print "Hello " + name + '!' *5
# Intexing strings sample print name [0] = R
print name [0]

# Selecting Subsequences
word = 'assume'
print word[3]
print word[4:6]
print word[4:]
print word[:2]

# Write Python code that prints out Udacity (with a capital U),
# given the definition of s below.
s = 'audacity'
print 'U' + s[2:] # starting at 2 because we need a capital U that we need to print manually

#Find strings in strings
pythagoras = 'There is geometry in the humming of the strings, there is music in the spacing of spheres'
print pythagoras.find('string')
print pythagoras[40:]
print pythagoras.find('T')
print pythagoras.find('sphere')
# This segment is just a chance for you to play around with
# finding strings within strings. Read through the code and
# press Test Run to see what it does. Is there anything
# interesting or unexpected?
print "Example 1: Finding substrings in a string"
print "test".find("te")
print "test".find("st")
print "test"[2:]

print "Example 2: Finding substrings in a string which is stored as a variable"
my_string = "test"
print my_string.find("te")
print my_string.find("st")
print my_string[2:]

print "Example 3: Printing out everything after a certain substring"
my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
favorite_color = my_string[color_start_location:]
print favorite_color # oops, this line prints out 'color: ' as well...
print favorite_color[7:] # this fixes it!

print "Example 4: Other interesting things about string.find()..."
print "text".find("text") # prints 0
print "text".find("Text") # prints -1
print "text".find("")     # prints 0
print "text".find(" ")    # prints -1

# Write Python code that prints the # of hours in 7 weeks
hours_in_day = 24
days_in_week = 7
print hours_in_day * days_in_week

# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.
print s[0:5] + t[6:]
# or if you are a Python Guru
print s[:-2] + t[-3:]

# Insert the proper slicing indices for the substring variable 
# so that the slice is a string that contains everything after "A NOUN". 
# For example, if we wanted to store everything after "went", the returned 
# string would be equal to sentence[11:].
sentence = "A NOUN went on a walk."
substring = sentence[6:]
print substring

# Use string slicing to store everything before "NOUN" in substring1,
# everything after "NOUN" and before "VERB" in substring2, and everything after "VERB" 
# in substring3.

sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]
print substring1
print substring2
print substring3

# Set noun_replacement and verb_replacement to your own noun and verb strings. 
# Then, concatenate the variables substring1-3, noun_replacement, and 
# verb_replacement and assign the result to the variable new_sentence so that 
# it's in the same order as the variable sentence.

sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[0:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]

noun_replacement = "dude" # your noun here
verb_replacement = "run" # your verb here

new_sentence = "A dude went on a walk. It can run really fast"
# your code here
print substring1 + noun_replacement + substring2 + verb_replacement + substring3


# Mary is a world class spy with different aliases across the world.

# Mary is known as Randa in America. 
# But in Europe, her alias Randa has another alias known as Katie.
# In Asia, the alias Katie has another alias known as Salwa.
# In Australia, the alias Salwa is known as Kathleen.
# In South America, the alias Kathleen is known as the alias Gabriel.

# You're a spy yourself and you want to be able to print the real name associated with
# all of these alias names to keep track of Mary, but you only know that 
# gabriel = kathleen, and kathleen = salwa, etc..

# Your mission: knowing how each alias relates to each other, assign the variables 
# gabriel, kathleen, salwa, katie, and randa to each other so whenever we print any alias,
# the values for each alias will point to the string "Mary"

# NOTE: We can't simply assign all variables to "Mary".

mary = "Mary"
# Your code goes here
# Mary is known as Randa in America.
mary = "Randa"
# But in Europe, her alias Randa has another alias known as Katie.
randa = "Katie"
# In Asia, the alias Katie has another alias known as Salwa.
katie = "Salwa"
# In Australia, the alias Salwa is known as Kathleen.
salwa = "Kathleen"

# In South America, the alias Kathleen is known as the alias Gabriel, this means that:
gabriel = "Kathleen"
kathleen = "Salwa"

# Test to see if all of these variables will print out the string "Mary"
print gabriel
print kathleen
print salwa
print katie
print randa
print mary

# Are you wondering why there's two ways to make strings 
# (single quotes AND double quotes)?? 
#
# Look at the code on line 11. It uses the single quote ' to 
# create a string. But it also has a double quote " inside of the
# string.

# Would we be able to create a string like the one below if we 
# could only use the double quote " to create strings?

div_with_class = '<div class="concept-description">'
just_the_class = div_with_class[5:-1]
print just_the_class

# Use string sequencing to take the single HTML <div> element
# below (written on one line) and then prints it up as three
# lines. 
# The first line should just be the opening tag: <div>
# The second line should be the text within the div (don't forget to indent)
# The third line should just be the closing tag.

div_element = "<div>I am learning to code!</div>"

opening_tag = div_element[:5] # add the appropriate numbers to each side of the colon
indent      = '    ' # modify this string so that it indents the inner text.
inner_text  = div_element[5:-6] # add the appropriate numbers to each side of the colon
closing_tag = div_element[-6:] # add the appropriate numbers to each side of the colon

print opening_tag
print indent + inner_text
print closing_tag

# I will show you my solution next, but try to figure it out yourself!
#I solved the above issue correctly by using negative indexes

#THIS IS A DIFFICULT PROBLEM, PER THE TEST INSTRUCTIONS!!
# Use the string.find method to locate "NOUN" and "VERB" in the string text
# and store those positions in the variables noun_position and verb_position respectively.
# Review Dave's video on string.find at https://goo.gl/Pde1nZ or visit
# http://www.tutorialspoint.com/python/string_find.htm for more information.

text = """Wow this is a fairly long body of text. Quite a few characters too.
I wonder if the string.find method could help find where NOUN is located.
That way, I could go out and VERB with my friends rather than counting characters
all day long!"""

noun_position = text.find('NOUN')
verb_position = text.find('VERB')
print noun_position
print verb_position
#The above problem caused me some issues because I was stupid and used string.find
#instead of using text.find which was declared earlier! idiot :)

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip' 
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped' 
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped" 

# ENTER CODE BELOW HERE
first_zip=text.find('zip')
print text.find('zip',first_zip+1)

# Let's go over another string method: string.replace. Use this method
# to replace the instance of NOUN with "duck" and VERB with "waddle" in the string
# sentence. For more information, visit http://www.tutorialspoint.com/python/string_replace.htm.

#sentence = "A NOUN went on a walk. They can VERB really well."
#sentence = #fill this in
#sentence = #fill this in

sentence = "A NOUN went on a walk. They can VERB really well."
sentence = sentence.replace("NOUN", "duck")
sentence = sentence.replace("VERB", "waddle")
print sentence


#def say_hello(name):
 #   greeting = "Hello " + name + '!'
  #  return greeting

  
# In the previous example, you saw code that looked like what you see above.
# Look at the first line. In that line, 'name' is a "parameter"
# of the function say_hello

# In the code below, the add_two_numbers function has two parameters.
# What do you think will happen when you press "Test Run"?
# Make a prediction and then press "Test Run"
def add_two_numbers(number_1, number_2):
    return number_1 + number_2

print add_two_numbers(4, 3)
print add_two_numbers(2, 6)
print add_two_numbers(0, 9)

# Once you've pressed Test Run, remove the comment characters from the 
# code below and then make ONE modification so that the function does 
# what the name says it should do.

#def subtract_two_numbers(number_1, number_2):
#    return number_1 + number_2

#print subtract_two_numbers(4, 3)