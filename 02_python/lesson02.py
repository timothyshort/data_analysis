#Basics of functions, variables, conditionals
#Part 2
def population_density(population, land_area):
    return population/land_area

def readable_timedelta(days):
	  #returns the number of days in format of weeks and days
	  return '{} week(s) and {} day(s)'.format(int(days/7), days%7)

#Part 3
def which_prize(points):
	#returns a message with the prize based on point value
    if (points <= 50):
        prize = 'wooden rabbit'
    elif (points <= 150):
        return "Oh dear, no prize this time."
    elif (points <= 180):
        prize = "wafer-thin mint"
    elif (points <=200):
        prize = "penguin"
    return "Congratulations! You have won a {}!".format(prize)

#Part 9
 def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        side_area += 2 * top_area
        return side_area
    else:
        return 3.14 * radius ** 2

#Part 13
def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating

def convert_to_numeric(num):
    #Converts and returns input to a number
    return float(num)
    
def sum_of_middle_three(num1, num2, num3, num4, num5):
    #Finds the sum of middle 3 numbers (throws out highest and lowest numbers)
    min_rating = min(num1, num2, num3, num4, num5)
    max_rating = max(num1, num2, num3, num4, num5)
    total_rating = num1 + num2 + num3 + num4 + num5
    return total_rating - min_rating - max_rating

def score_to_rating_string(rating_number):
	#Converts numeric score to a rating message
    if (rating_number < 1):
        return "Terrible"
    elif (rating_number < 2):
        return "Bad"
    elif (rating_number < 3):
        return "OK"
    elif (rating_number < 4):
        return "Good"
    else:
        return "Excellent" 
  