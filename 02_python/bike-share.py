## import all necessary packages and functions.
import csv # read and write csv files
from datetime import datetime # operations to parse dates
from pprint import pprint # use to print data structures like dictionaries in
                          # a nicer way than the base print function.

'''
DATA COLLECTION & WRANGLING
'''

def print_first_point(filename):
    """
    This function prints and returns the first data point (second row) from
    a csv file that includes a header row.
    """
    # print city name for reference
	city = filename.split('-')[0].split('/')[-1]
	print('\nCity: {}'.format(city))
    
	with open(filename, 'r') as f_in:
        ## TODO: Use the csv library to set up a DictReader object. ##
        ## see https://docs.python.org/3/library/csv.html           ##
		trip_reader = csv.DictReader(f_in)
        
        ## TODO: Use a function on the DictReader object to read the     ##
        ## first trip from the data file and store it in a variable.     ##
        ## see https://docs.python.org/3/library/csv.html#reader-objects ##
		first_trip = trip_reader.__next__()
        
        ## TODO: Use the pprint library to print the first trip. ##
        ## see https://docs.python.org/3/library/pprint.html     ##
		pprint(first_trip)
        
    # output city name and first trip for later testing
	return (city, first_trip)

# list of files for each city
data_files = ['./data/NYC-CitiBike-2016.csv',
              './data/Chicago-Divvy-2016.csv',
              './data/Washington-CapitalBikeshare-2016.csv',]

# print the first trip from each file, store in dictionary
example_trips = {}
for data_file in data_files:
	city, first_trip = print_first_point(data_file)
	example_trips[city] = first_trip



def duration_in_mins(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the trip duration in units of minutes.
    
    Remember that Washington is in terms of milliseconds while Chicago and NYC
    are in terms of seconds. 
    
    HINT: The csv module reads in all of the data as strings, including numeric
    values. You will need a function to convert the strings into an appropriate
    numeric type when making your transformations.
    see https://docs.python.org/3/library/functions.html
    """
    
	if (city == "Washington"):
		duration = int(datum['Duration (ms)']) / 1000
	elif (city == "Chicago"):
		duration = int(datum['tripduration'])
	elif (city == "NYC"):
		duration = int(datum['tripduration'])
    
	return duration / 60

# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': 13.9833,
	'Chicago': 15.4333,
	'Washington': 7.1231}

for city in tests:
	assert abs(duration_in_mins(example_trips[city], city) - tests[city]) < .001



def time_of_trip(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the month, hour, and day of the week in
    which the trip was made.
    
    Remember that NYC includes seconds, while Washington and Chicago do not.
    
    HINT: You should use the datetime module to parse the original date
    strings into a format that is useful for extracting the desired information.
    see https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    """
    
	if (city == "Washington"):
		date = datetime.strptime(datum['Start date'], '%m/%d/%Y %H:%M')
	elif (city == "Chicago"):
		date = datetime.strptime(datum['starttime'], '%m/%d/%Y %H:%M')
	elif (city == "NYC"):
		date = datetime.strptime(datum['starttime'], '%m/%d/%Y %H:%M:%S')
    
	month = date.month
	hour = date.hour
	day_of_week = date.strftime('%A')
        
	return (month, hour, day_of_week)

# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': (1, 0, 'Friday'),
		'Chicago': (3, 23, 'Thursday'),
		'Washington': (3, 22, 'Thursday')}

for city in tests:
	assert time_of_trip(example_trips[city], city) == tests[city]



def type_of_user(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the type of system user that made the
    trip.
    
    Remember that Washington has different category names compared to Chicago
    and NYC. 
    """
    
    if (city == "Washington"):
        wash_user_type = datum['Member Type']
        if wash_user_type == "Registered":
            user_type = "Subscriber"
        elif wash_user_type == "Casual":
            user_type = "Customer"
    elif (city == "Chicago"):
        user_type = datum['usertype']
    elif (city == "NYC"):
        user_type = datum['usertype']
    
    return user_type


# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': 'Customer',
		'Chicago': 'Subscriber',
		'Washington': 'Registered'}

for city in tests:
	assert type_of_user(example_trips[city], city) == tests[city]



def condense_data(in_file, out_file, city):
    """
    This function takes full data from the specified input file
    and writes the condensed data to a specified output file. The city
    argument determines how the input file will be parsed.
    
    HINT: See the cell below to see how the arguments are structured!
    """
    
	with open(out_file, 'w') as f_out, open(in_file, 'r') as f_in:
        # set up csv DictWriter object - writer requires column names for the
        # first row as the "fieldnames" argument
		out_colnames = ['duration', 'month', 'hour', 'day_of_week', 'user_type']        
		trip_writer = csv.DictWriter(f_out, fieldnames = out_colnames)
		trip_writer.writeheader()
        
        ## TODO: set up csv DictReader object ##
		trip_reader = csv.DictReader(f_in)

        # collect data from and process each row
		for row in trip_reader:
            # set up a dictionary to hold the values for the cleaned and trimmed
            # data point
			new_point = {}

            ## TODO: use the helper functions to get the cleaned data from  ##
            ## the original data dictionaries.                              ##
            ## Note that the keys for the new_point dictionary should match ##
            ## the column names set in the DictWriter object above.         ##
			new_point['duration'] = duration_in_mins(row, city)
			new_point['month'] = time_of_trip(row, city)[0]
			new_point['hour'] = time_of_trip(row, city)[1]
			new_point['day_of_week'] = time_of_trip(row, city)[2]
			new_point['user_type'] = type_of_user(row, city)

            ## TODO: write the processed information to the output file.     ##
            ## see https://docs.python.org/3/library/csv.html#writer-objects ##
			trip_writer.writerow(new_point)

# Run this cell to check your work
city_info = {'Washington': {'in_file': './data/Washington-CapitalBikeshare-2016.csv',
						'out_file': './data/Washington-2016-Summary.csv'},
			'Chicago': {'in_file': './data/Chicago-Divvy-2016.csv',
						'out_file': './data/Chicago-2016-Summary.csv'},
			'NYC': {'in_file': './data/NYC-CitiBike-2016.csv',
						'out_file': './data/NYC-2016-Summary.csv'}}

for city, filenames in city_info.items():
	condense_data(filenames['in_file'], filenames['out_file'], city)
	print_first_point(filenames['out_file'])



'''
EXPLORATORY DATA ANALYSIS
'''


def number_of_trips(filename):
    """
    This function reads in a file with trip data and reports the number of
    trips made by subscribers, customers, and total overall.
    """
	with open(filename, 'r') as f_in:
        # set up csv reader object
		reader = csv.DictReader(f_in)
        
        # initialize count variables
		n_subscribers = 0
		n_customers = 0
        
        #duration variables
		total_duration = 0
		d_over_thirty = 30
        
        #duration variables by customer
		d_subscriber = 0
		d_customer = 0
        
        # tally up ride types
		for row in reader:
		if row['user_type'] == 'Subscriber':
				n_subscribers += 1
				d_subscriber += float(row['duration'])
			else:
				n_customers += 1
				d_customer += float(row['duration'])
            
			total_duration += float(row['duration'])
			if float(row['duration']) >= 30:
				d_over_thirty += 1
        
        # compute total number of rides
		n_total = n_subscribers + n_customers
        
        # return tallies as a tuple
		return(n_subscribers, n_customers, n_total,
			total_duration, d_over_thirty,
			d_subscriber, d_customer, )

## Modify this and the previous cell to answer Question 4a. Remember to run ##
## the function on the cleaned data files you created from Question 3.      ##

data_file_chicago = './data/Chicago-2016-Summary.csv'
data_file_nyc = './data/NYC-2016-Summary.csv'
data_file_washington = './data/Washington-2016-Summary.csv'

chicago = number_of_trips(data_file_chicago)
nyc = (number_of_trips(data_file_nyc))
washington = (number_of_trips(data_file_washington))

print("CHICAGO")
print(" Subscribers: {}".format(chicago[0]))
print(" Customers: {}".format(chicago[1]))
print(" Total: {}".format(chicago[2]))

print("NYC")
print(" Subscribers: {}".format(nyc[0]))
print(" Customers: {}".format(nyc[1]))
print(" Total: {}".format(nyc[2]))

print("WASHINGTON")
print(" Subscribers: {}".format(washington[0]))
print(" Customers: {}".format(washington[1]))
print(" Total: {}".format(washington[2]))

#Define sets
most_trips = max(chicago[2], nyc[2], washington[2])
most_subscribers = max(chicago[0]/chicago[2], nyc[0]/nyc[2], washington[0]/washington[2])
most_short_term = max(chicago[1]/chicago[2], nyc[1]/nyc[2], washington[1]/washington[2])

#Find city with most trips
if (most_trips == chicago[2]):
	city_most_trips = "Chicago", chicago[2]
elif (most_trips == nyc[2]):
	city_most_trips = "NYC", nyc[2]
elif (most_trips == washigton[2]):
	city_most_trips = "Washington", washington[2]
    
#Find cith with highest proportion of subscribers
if (most_subscribers == chicago[0]/chicago[2]):
	city_most_subscribers = "Chicago", chicago[0]/chicago[2]
elif (most_subscribers == nyc[0]/nyc[2]):
	city_most_subscribers = "NYC", nyc[0]/nyc[2]
elif (most_subscribers == washington[0]/washington[2]):
	city_most_subscribers = "Washington", washington[0]/washington[2]

#Find cith with highest proportion of short-term customers
if (most_short_term == chicago[1]/chicago[2]):
	city_most_short_term = "Chicago", chicago[1]/chicago[2]
elif (most_short_term == nyc[1]/nyc[2]):
	city_most_short_term = "NYC", nyc[1]/nyc[2]
elif (most_short_term == washington[1]/washington[2]):
	city_most_short_term = "Washington", washington[1]/washington[2]

print("\nSTATISTICAL ANALYSIS")
print(" City with most trips: {} | {} trips".format(
	city_most_trips[0], city_most_trips[1]))
print(" City with highest proportion of subscribers: {} | {}".format(
	city_most_subscribers[0], city_most_subscribers[1]))
print(" City with highest proportion of short-term customers: {} | {}".format(
	city_most_short_term[0], city_most_short_term[1]))


## Use this and additional cells to answer Question 4b.                 ##
##                                                                      ##
## HINT: The csv module reads in all of the data as strings, including  ##
## numeric values. You will need a function to convert the strings      ##
## into an appropriate numeric type before you aggregate data.          ##
## TIP: For the Bay Area example, the average trip length is 14 minutes ##
## and 3.5% of trips are longer than 30 minutes.                        ##

avg_duration_chicago = chicago[3] / chicago[2]
durations_over_thirty_proportion_chicago = chicago[4] / chicago[2]

avg_duration_nyc = nyc[3] / nyc[2]
durations_over_thirty_proportion_nyc = nyc[4] / nyc[2]

avg_duration_washington = washington[3] / washington[2]
durations_over_thirty_proportion_washington = washington[4] / washington[2]

print("CHICAGO Ride Duration:")
print(" Average Duration: {} mins".format(avg_duration_chicago))
print(" Proportion of rides longer than 30 minutes: {}".format(
    durations_over_thirty_proportion_chicago))

print("NYC Ride Duration:")
print(" Average Duration: {} mins".format(avg_duration_nyc))
print(" Proportion of rides longer than 30 minutes: {}".format(
    durations_over_thirty_proportion_nyc))

print("WASHINGTON Ride Duration:")
print(" Average Duration: {} mins".format(avg_duration_washington))
print(" Proportion of rides longer than 30 minutes: {}".format(
    durations_over_thirty_proportion_washington))

## Use this and additional cells to answer Question 4c. If you have    ##
## not done so yet, consider revising some of your previous code to    ##
## make use of functions for reusability.                              ##
##                                                                     ##
## TIP: For the Bay Area example data, you should find the average     ##
## Subscriber trip duration to be 9.5 minutes and the average Customer ##
## trip duration to be 54.6 minutes. Do the other cities have this     ##
## level of difference?                                                ##

print("CHICAGO Average Duration by Customer")
print(" Subscribers: {} mins".format(chicago[5] / chicago[0]))
print(" Customer: {} mins".format(chicago[6] / chicago[0]))
print("NYC Average Duration by Customer")
print(" Subscribers: {} mins".format(nyc[5] / nyc[0]))
print(" Customer: {} mins".format(nyc[6] / nyc[0]))
print("WASHINGTON Average Duration by Customer")
print(" Subscribers: {} mins".format(washington[5] / washington[0]))
print(" Customer: {} mins".format(washington[6] / washington[0]))