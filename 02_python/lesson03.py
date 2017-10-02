#Data Structures & Loops

'''
PART 2: Lists
'''

def how_many_days(month_number):
    """Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    return days_in_month[month_number-1]

# This test case should print 31, the number of days in the eighth month, August
print(how_many_days(8))


def find_eclipse):
	eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
	                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
	                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
	                 'March 9, 2016']
	                 
	                 
	# TODO: Modify this line so it prints the last three elements of the list
	print(eclipse_dates[-3:])


def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # TODO: implement this function
    return sorted(input_list, reverse = True)[:3]
                
print(top_three([2,3]))


def median(numbers):
    numbers.sort() #The sort method sorts a list directly, rather than returning a new sorted list
    if (len(numbers) % 2 == 1):
        middle_index = int(len(numbers)/2)
        return numbers[middle_index]
    else:
        middle_index = int(len(numbers)/2)
        return (numbers[middle_index] + numbers[middle_index-1])/2

test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))



'''
PART 4: Loops
'''

def list_sum(input_list):
    sum = 0
    for n in input_list:
        sum+= n
    return sum

#These test cases check the list_sum works correctly
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))


"""Write a function, `tag_count`, that takes as its argument a list
of strings. It should return a count of how many of those strings
are XML tags. You can tell if a string is an XML tag if it begins
with a left angle bracket "<" and end with a right angle bracket ">".
"""
def tag_count(list):
    num_of_tags=0
    for item in list:
        if(item[0] == '<' and item[-1] == '>'):
            num_of_tags+=1
    return num_of_tags


# Test for the tag_count function:
list1 = ['<greeting>', 'Hello World!', '</greeting>']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))


#define the  html_list function#define the html_list function
def html_list(list):
    li_list = '<ul>\n'
    for li in list:
        li_list += ('<li>' + li + '</li>\n')
    li_list += '</ul>'
    return li_list

print(html_list(['first string', 'second string']))


def starbox(width, height):
    """print a box made up of asterisks.

    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    """
    print("*" * width) #print top edge of box
   
    # print sides of box
    for x in range(height-2):
        print("*" + " " * (width-2) + "*") 

    print("*" * width) #print bottom edge of box

# Test Cases
print("Test 1:")
starbox(5, 5) # this prints correctly

print("Test 2:")
starbox(2, 3)  # this currently prints two lines too tall - fix it!


'''
PART 6: Loops
'''


#TODO: Implement the nearest_square function
def nearest_square(limit):
    number = 1;
    while (number**2 < limit):
        number += 1
    return (number-1)**2
    
test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))


def print_headlines(headlines):
    ticker=""
    for headline in headlines:
        ticker+=headline + " "
        if (len(ticker)>140):
            break
    return ticker[0:140]
    

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

# TODO: set news_ticker to a string that contains no more than 140 characters long.
news_ticker = print_headlines(headlines)
print(news_ticker)


'''
PART 8: Sets
'''

 # Define the remove_duplicates function
def remove_duplicates(list):
    new_list = []
    for item in list:
        if new_list.count(item) == 0:
            new_list.append(item)
    return new_list
 
list = ["one", "two", "three", "two"]
print(remove_duplicates(list))


squares = set()

# Note: If you want to call the nearest_square function, you must define
# the function on a line before you call it. Feel free to move this code up!
def nearest_square(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2

# todo: populate "squares" with the set of all of the integers less 
# than 2000 that are square numbers
for n in range(2,2000):
    squares.add(nearest_square(n))
print(squares)


'''
PART 10-11: Dictionaries
'''

population = { 'Shanghai' : 17.8, 'Istanbul' : 13.3, 'Karachi' : 13.0, 'Mumbai' : 12.5 }

from countries import country_list # Note: since the list is so large, it's tidier
                                   # to put in in a separate file. We'll learn more
                                   # about "import" later on.

country_counts = {}
for country in country_list:
    #todo: insert countries into the country_count dict.
    # If the country isn't in the dict already, add it and set the value to 1
    # If the country is in the dict, increment its value by one to keep count
    if country in country_counts:
        country_counts[country] +=1
    else:
        country_counts[country] = 1



def most_prolific(albums):
    max_count=0
    album_years = {}
    for title in albums:
        year = albums[title]
        if (year in album_years):
            album_years[year] += 1
            if album_years[year] > max_count:
                max_count = album_years[year]
        else:
            album_years[year] = 1
    
    for year in album_years:
        if album_years[year] == max_count:
            return year
        
Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}

print(most_prolific(Beatles_Discography))


'''
PART 12
'''

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True


def total_takings(yearly_record):
    sum=0
    for month in yearly_record:
        for amount in yearly_record[month]:
            sum += amount
    return sum
            
monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}
  
print(total_takings(monthly_takings))