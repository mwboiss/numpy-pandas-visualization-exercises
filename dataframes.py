# Dataframes Exercises

from pydataset import data
import pandas as pd
import numpy as np

# Problem 1: Copy the code from the lesson to create a dataframe full of student grades.

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

print(df)
# A) Create a column named passing_english that indicates whether each student has a passing grade in english.

df['passing_english'] = df.english > 70

print(df)

# B) Sort the english grades by the passing_english column. How are duplicates handled?

df.sort_values(by='passing_english')

print(df)

###### Rows are sorted by the passing_enlish column first and then they are sorted by the index in ascending order. #######

# C) Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)

df.sort_values(by= ['passing_english','name'])

print(df)

# D) Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.

df.sort_values(by= ['passing_english','english'])

print(df)

# E) Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.

df['overall_grade'] = (df.english + df.math + df.reading) / 3

print(df)

# Problem 2: Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:

mpg = data('mpg')
data('mpg', show_doc=True)

# A) How many rows and columns are there?

############ From show_doc: 234 rows and 11 columns ###########

# B) What are the data types of each column?

mpg.dtypes

######### Returns the below columns with their types.##########
# manufacturer     object
# model            object
# displ           float64
# year              int64
# cyl               int64
# trans            object
# drv              object
# cty               int64
# hwy               int64
# fl               object
# class            object

# C) Summarize the dataframe with .info and .describe

mpg.info()
mpg.describe()

# D) Rename the cty column to city.

mpg = mpg.rename(columns={'cty': 'city'})

print(mpg)

# E) Rename the hwy column to highway.

mpg = mpg.rename(columns={'hwy': 'highway'})

print(mpg)

# F) Do any cars have better city mileage than highway mileage?

mpg [mpg.city > mpg.highway]

####### Above code returns an empty dataframe. So no there should not be any cars that have better city milage than highway milage.

# G) Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.

mpg['milage_difference'] = mpg.highway - mpg.city

print(mpg)

# H) Which car (or cars) has the highest mileage difference?

mpg.sort_values(by='milage_difference', ascending = False)

######## There were two cars with the highest difference:

    # Honda Civic in row 107
    # Volkswagen New Beetle in row 223

# I) Which compact class car has the lowest highway mileage? The best?

mpg [mpg['class'] == 'compact'].sort_values(by='highway')

######### Compact class car with the lowest highway milage: Volkswagen Jetta in row 220

mpg [mpg['class'] == 'compact'].sort_values(by='highway', ascending=False)

######### Compact class car with the highest highway milage: Volkswagen Jetta in row 213

# J) Create a column named average_mileage that is the mean of the city and highway mileage.

mpg['average_milage'] = (mpg.city + mpg.highway) / 2

print(mpg)

# K) Which dodge car has the best average mileage? The worst?

mpg[mpg.manufacturer == 'dodge'].sort_values(by='average_milage',ascending=False)

######### Dodge car with the best average milage: Dodge Caravan in row 38 

mpg[mpg.manufacturer == 'dodge'].sort_values(by='average_milage')

######### Dodge car with the best average milage: Dodge Ram 1500 Pickup in row 70

# Problem 3: Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:


Mammals = data('Mammals')
data('Mammals', show_doc=True)

# A) How many rows and columns are there?

######## show_docs shows: 107 rows and 4 columns

# B) What are the data types?

Mammals.dtypes

####### Column types are below

# weight      float64
# speed       float64
# hoppers        bool
# specials       bool

# C) Summarize the dataframe with .info and .describe

Mammals.info()
Mammals.describe()

# D) What is the the weight of the fastest animal?

Mammals.sort_values(by='speed', ascending=False)

######## The fastest animal's weight is 55 Kg in row 53

# E) What is the overal percentage of specials?

specials_true_percentage = Mammals['specials'] [Mammals['specials'] == True].count() / Mammals['specials'].count()

specials_true_percentage

# F) How many animals are hoppers that are above the median speed? What percentage is this?

##### returns the median speed of all animals
median_speed = Mammals['speed'].median()
median_speed

##### returns a dataframe with just animals that have a True hoppers value
hopper_animals = Mammals [Mammals['hoppers'] == True]
hopper_animals

##### returns a list of animals that have a True hoppers value and have a speed value above the median speed value of all animals
hopper_animals_above_median_speed = hopper_animals [Mammals['speed'] > median_speed]
hopper_animals_above_median_speed

print(f'The number of animals that are hoppers and have a speed above the median speed is {len(hopper_animals_above_median_speed)}.\nThis is {round(len(hopper_animals_above_median_speed) / len(Mammals) * 100, 2)} percent of the total number of animals.')