# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
   return day == 'Saturday' or day == 'Sunday'

    
print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False

# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

def countdown(n):
	while n > 0:
		print n
		n = n-1
	print "Blastoff!"  #I need to pay attention to indentation, originally this was directly
						#under n = n-1 and it printed blastoff after each countdown

countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!

# Write code for the function random_noun, which takes in no inputs but outputs 
# one of two nouns randomly. Use the randint function to generate a number 
# from 0-1 and return a noun depending on whether the number is equal to 0 or 1. 
# Feel free to experiment with different nouns, but for submission purposes return 
# the string "sofa" if the number is 0, else return "llama".

from random import randint

def random_noun(noun):
	random_num = randint(0,1)
	if random_num == 0:
		return "sofa"
	else:
		return "llama"

# Write code for the function random_verb, which takes in no inputs but outputs 
# one of two verbs randomly. Use the randint function to generate a number from 0-1 
# and return a verb depending on whether the number is equal 0 or 1. Feel free to 
# experiment with different verbs, but for submission purposes return the string "run"
# if the number is 0, else return "kayak".

from random import randint

def random_verb():
    random_verb = randint(0,1)
    if random_verb == 0:
    	return run
    else:
    	return kayak

## Madlibs take 1

# Write code for the function word_transformer, which takes in a string word as input. 
# If word is equal to "NOUN", return a random noun, if word is equal to "VERB", 
# return a random verb, else return the first character of word. 

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
    	return random_noun()
    if word == "VERB":
    	return random_verb()
    else: return word[0:]

