#Files, Modules, Tuples


'''
PART 1: Tuples
'''

def hours2days(total_hours):
     return total_hours // 24, total_hours % 24

print(hours2days(24)) # 24 hours is one day and zero hours
print(hours2days(25)) # 25 hours is one day and one hour



'''
PART 2: Default Arguments
'''

def print_list(l, numbered=False, bullet_character ='-'):
    '''Prints a list on multiple lines, with numbers or bullets
    Arguments:
    l: The list to print
    numbered: set to True to print a numbered list
    bullet_character: The symbol placed before each list element. This is
                      ignored if numbered is True.
    '''
    for index, element in enumerate(l):
        if numbered:
            print("{}: {}".format(index+1, element))
        else:
            print("{} {}".format(bullet_character, element))

print_list(["cats", "in", "space"])
print_list(["cats", "in", "space"], True)



'''
PART 4: Reading Files
'''

def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    with open(filename) as f:
        #use the for loop syntax to process each line
        for line in f:
            #and add the actor name to cast_list
            cast_list.append(line.split(',')[0])
    return cast_list

create_cast_list('flying_circus_cast.txt')



'''
PART 6: Standard Library
'''

# TODO: print e to the power of 3 using the math module
import math
print(math.pow(math.e,3))


# Use an import statement at the top
from random import randint as rand

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password(word_list):
    w1 = rand(0,len(word_list)-1)
    w2 = rand(0,len(word_list)-1)
    w3 = rand(0,len(word_list)-1)
    return word_list[w1] + word_list[w2] + word_list[w3]

print(generate_password(word_list))