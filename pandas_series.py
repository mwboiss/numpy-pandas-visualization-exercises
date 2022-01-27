# Exercises Part I
# Use Series attributes and methods to explore your fruits Series.
# Make a file named pandas_series.py or pandas_series.ipynb for the following exercises.
# Use pandas to create a Series named fruits from the following list:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
fruits

# Problem 1: Determine the number of elements in fruits.

fruits.size

# Problem 2: Output only the index from fruits.

fruits.index

# Problem 3: Output only the values from fruits.

fruits.values

# Problem 4: Confirm the data type of the values in fruits.

fruits.dtype

# Problem 5: Output only the first five values from fruits. Output the last three values. Output two random values from fruits.

fruits.head(5)
fruits.tail(3)
fruits.sample(2)

# Problem 6: Run the .describe() on fruits to see what information it returns when called on a Series with string values.

fruits.describe()

# Problem 7: Run the code necessary to produce only the unique string values from fruits.

fruits.unique()

# Problem 8: Determine how many times each unique string value occurs in fruits.

fruits.value_counts()

# Problem 9: Determine the string value that occurs most frequently in fruits.

fruits.value_counts().nlargest(n=1)

# Problem 10: Determine the string value that occurs least frequently in fruits.

fruits.value_counts().nsmallest(n=1)

# Exercises Part II
# Explore more attributes and methods while you continue to work with the fruits Series.
# Problem 1: Capitalize all the string values in fruits.

print(fruits.str.upper())

# Problem 2: Count the letter "a" in all the string values (use string vectorization).

fruits.str.count('a').sum()

# Problem 3: Output the number of vowels in each and every string value.

fruits_df = pd.DataFrame(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

vowels = 'aeiouy'

vowel_count = pd.DataFrame([sum(1 for letter in fruit if letter in vowels) for fruit in fruits])
vowel_count

fruits_df.insert(1,'vowel_count',vowel_count)
fruits_df

# Problem 4: Write the code to get the longest string value from fruits.

fruits [fruits.str.len() == max(fruits.str.len())]

# Problem 5: Write the code to get the string values with 5 or more letters in the name.

fruits [fruits.str.len() >= 5]

# Problem 6: Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.

fruits[fruits.apply(lambda n: n.count('o') >= 2)]

# Problem 7: Write the code to get only the string values containing the substring "berry".

fruits[fruits.apply(lambda n: n.findall('berry'))]
fruits[fruits.str.findall('berry')]

# Problem 8: Write the code to get only the string values containing the substring "apple".

# Problem 9: Which string value contains the most vowels?

# Exercises Part III
# Use pandas to create a Series named letters from the following string. The easiest way to make this string into a Pandas series is to use list to convert each individual letter into a single string on a basic Python list.


    'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'

# Problem 1: Which letter occurs the most frequently in the letters Series?

# Problem 2: Which letter occurs the Least frequently?

# Problem 3: How many vowels are in the Series?

# Problem 4: How many consonants are in the Series?

# Problem 5: Create a Series that has all of the same letters but uppercased.

# Problem 6: Create a bar plot of the frequencies of the 6 most commonly occuring letters.

# Use pandas to create a Series named numbers from the following list:


    ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

# Problem 1: What is the data type of the numbers Series?

# Problem 2: How many elements are in the number Series?

# Problem 3: Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.

# Problem 4: Run the code to discover the maximum value from the Series.

# Problem 5: Run the code to discover the minimum value from the Series.

# Problem 6: What is the range of the values in the Series?

# Problem 7: Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.

# Problem 8: Plot the binned data in a meaningful way. Be sure to include a title and axis labels.

# Use pandas to create a Series named exam_scores from the following list:


    [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]

# Problem 1: How many elements are in the exam_scores Series?

# Problem 2: Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.

# Problem 3: Plot the Series in a meaningful way and make sure your chart has a title and axis labels.

# Problem 4: Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.

# Problem 5: Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.

# Problem 6: Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.

# More Practice
# Revisit the exercises from https://gist.github.com/ryanorsinger/f7d7c1dd6a328730c04f3dc5c5c69f3a.

# After you complete each set of Series exercises, use any extra time you have to pursue the challenge below. You can work on these in the same notebook or file as the Series exercises or create a new practice notebook you can work in a little every day to keep your python and pandas skills sharp by trying to solve problems in multiple ways. These are not a part of the Series exercises grade, so don't worry if it takes you days or weeks to meet the challenge.

# Challenge yourself to be able to...

# solve each using vanilla python.

# solve each using list comprehensions.

# solve each by using a pandas Series for the data structure instead of lists and using vectorized operations instead of loops and list comprehensions.