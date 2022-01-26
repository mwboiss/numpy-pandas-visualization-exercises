# numpy exercises

# Importing the correct libraries

import numpy as np
import math
import matplotlib as plt

# Using the array below

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# Problem 1: How many negative numbers are there?

# Assigning a variable to the negative numbers in the numpy array
neg = a [a < 0]
neg

# The length of the new variable is how many negative numbers are in the array.
len(neg)

# Problem 2: How many positive numbers are there:

# Assigning a variable to the positive numbers in the numpy array
pos = a[a > 0]
len(pos)

#OR

# Looking at a list that show us which are positive and getting the length of that list
a [a > 0]
len(a[a > 0])

# Problem 3: How many even positive numbers are there?

# Getting a list of booleans that are even and positive and the finding the length

a[(a % 2 == 0) & (a > 0)]
len(a[(a % 2 == 0) & (a > 0)])

# Problem 4: if you were to add 3 to each data point, how many positive numbers would there be?

# Assigning a new array that is the original plus 3 
b = a + 3
b

# Finding the length of the array that are positive 
len(b [b > 0])

# Problem 5: if you squared each number, what would the new mean and standard deviation be?

# Assigning a new array that is the original squared and finding the standard deviation and mean to the new array
b = a ** 2
b.std()
b.mean()

# Problem 6: A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set.

# Looking at the array and its mean
a
a.mean()

# making a new array with the original array minus its mean
a_minus_mean = a - a.mean()
a_minus_mean

# Problem 7: Calculate the z-score for each data point.

# Assessing the orginal array, its mean and standard deviation
a
a.std()
a.mean()

# Assigning the Z score to the new array. Z score is the original value - the mean of the set then divided by the standard deviation
z = (a - a.mean()) / a.std()
z

# Problem 8: Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.

##################################################################################################################################

import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

# Assigning the sum of the list "a" to a variable
sum_of_a = sum(a)
sum_of_a

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

# Assigning the min of the list "a" to a variable
min_of_a = min(a)
min_of_a

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

# Assigning the max of the list "a" to a variable
max_of_a = max(a)
max_of_a

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

# Assigning the mean of list "a" to a variable using the sum variable and the length of the list
mean_of_a = sum_of_a / len(a)
mean_of_a

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

# Assign a variable to 1 so that it does not affect the product i.e. 0 would make the final product 0. Run through the "a" list with a for loop. This multiplies each number to the new product variable. After the for loop runs it produces a number that is all the numbers in the list mulitiplied together, which is the product of that list.
product_of_a = 1
for num in a:
    product_of_a *= num
    
product_of_a

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

# Assign a blank list. Run through the "a" list. As we run through we append the individual number squared to the blank list.
squares_of_a = []
for num in a:
    squares_of_a.append(num**2)
squares_of_a

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

# Assing a blank list. Run through the "a" list. As we run through we append the individual number that when you take the modulo of 2 of that number it does not eaqual to zero.  
odds_in_a = []
for num in a:
    if num % 2 != 0:
        odds_in_a.append(num)
odds_in_a

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

# Same as the problem above except we are pulling the numbers that do not return zero when the modulo operator is applied with a 2
evens_in_a = []
for num in a:
    if num % 2 == 0:
        evens_in_a.append(num)
evens_in_a

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Assigning the list to a numpy array
new_b = np.array(b)

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
sum_of_b

# Since the list of lists is assigned to a numpy array we can use the .sum() and assign it to a new variable
sum_of_b = new_b.sum()
sum_of_b

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
min_of_b

min_of_b = new_b.min()
min_of_b

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = new_b.max()
max_of_b

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
mean_of_b

mean_of_b = new_b.mean()
mean_of_b

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
product_of_b

product_of_b = new_b.prod()
product_of_b

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
squares_of_b

squares_of_b = np.square(new_b)
squares_of_b

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
odds_in_b

odds_in_b = new_b [new_b % 2 != 0]
odds_in_b

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
evens_in_b

evens_in_b = new_b [new_b % 2 == 0]
evens_in_b

# Exercise 9 - print out the shape of the array b.

np.shape(new_b)

# Gives me a tuple with 2,3 which means that there are 2 lists with 3 elements in my array.

# Exercise 10 - transpose the array b.

np.transpose(new_b)

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

new_b.reshape(6)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

new_b.reshape(-1,1)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_c = np.array(c)
new_c

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

new_c.min()

new_c.max()

new_c.sum()

new_c.prod()

# Exercise 2 - Determine the standard deviation of c.

new_c.std()

# Exercise 3 - Determine the variance of c.

new_c.var()

# Exercise 4 - Print out the shape of the array c

print(np.shape(new_c))

# Exercise 5 - Transpose c and print out transposed result.

print(np.transpose(new_c))

# Exercise 6 - Get the dot product of the array c with c. 

np.dot(new_c,new_c)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

c_X_c_sum = np.sum(np.multiply(new_c, new_c.T))
c_X_c_sum

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

c_x_c_prod = np.prod(np.multiply(new_c,new_c.T))
c_x_c_prod


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

new_d = np.array(d)

# Exercise 1 - Find the sine of all the numbers in d

np.sin(new_d)

# Exercise 2 - Find the cosine of all the numbers in d

np.cos(new_d)

# Exercise 3 - Find the tangent of all the numbers in d

np.tan(new_d)

# Exercise 4 - Find all the negative numbers in d

d_neg = new_d [new_d < 0]
d_neg

# Exercise 5 - Find all the positive numbers in d

d_pos = new_d [new_d > 0]
d_pos

# Exercise 6 - Return an array of only the unique numbers in d.

np.unique(new_d)

# Exercise 7 - Determine how many unique numbers there are in d.

len(np.unique(new_d))

# Exercise 8 - Print out the shape of d.

print(np.shape(new_d))

# Exercise 9 - Transpose and then print out the shape of d.

print(np.transpose(np.shape(new_d)))

# Exercise 10 - Reshape d into an array of 9 x 2

new_d.reshape(2,9)

###############################################################################################################################

##### Awesome Bonus For much more practice with numpy, Go to https://github.com/rougier/numpy-100 and clone the repo down to your laptop. Next, go to https://github.com/new to make a new repo. Name it numpy-100, and follow the directions to "push an existing repository from the command line" so that you can push up your changes to your own account.