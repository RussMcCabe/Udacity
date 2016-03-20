# Lesson 2.4: While Loops

# Loops are an important concept in computer programming.
# Loops let us run blocks of code many times which can be
# really useful when we have to repeat tasks.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-48686708/m-48480488

def count():
    i = 0
    while i < 10:
        print i
        i = i + 1

count()

# Add your own code and notes here

# This code demonstrates a while loop with a "counting variable"
#i = 0
#while i < 10:
#    print i
#    i = i+1

# This uses a while loop to remove all the spaces from a string of
# text. Can you figure out how it works?
def remove_spaces(text):
    text_without_spaces = '' #empty string for now
    while text != '':
        next_character = text[0]
        if next_character != ' ':    #that's a single space
            text_without_spaces = text_without_spaces + next_character
        text = text[1:]
    return text_without_spaces
print remove_spaces("hello my name is andy how are you?")

# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.
# I was lost on this one, after watching the video I had a few questions why we have N as a 
# variable and then we define i... it makes more sense now sense N is the input

def print_numbers(n):
	i=0
	while i <= n:
		print i
		i = i + 1

print_numbers(3)
#>>> 1
#>>> 2
#>>> 3

## Bug identificaiton of code, the first code is original and the 2nd is the code I fixed

# When I wrote boldwrap, I didn't copy the functionality of the
# bracket function carefully.  Review my code and catch the mistake.

#def bracket(text):
#    return '[' + text + ']'

#def boldwrap(text)
 #   return '<b>' + text + '</b>'

#print boldwrap('This is an important message.')

# When I wrote boldwrap, I didn't copy the functionality of the
# bracket function carefully.  Review my code and catch the mistake.

def bracket(text):
    return '[' + text + ']'

def boldwrap(text): #it was a simple colon that was missing
    return '<b>' + text + '</b>'

print boldwrap('This is an important message.')


