
# DATA STRUCTURES AND ALGORITHMS PRACTICE, 
# WRITE THE TEST CASES FOR AN EXTRA CHALLENGE!!!


# Description:
# A grid is a perfect starting point for many games (Chess, battleships, Candy Crush!).
# Making a digital chessboard I think is an interesting way of visualising how loops can work together.
# Your task is to write a function that takes two integers rows and columns and returns a chessboard pattern as a two dimensional array.
# So chessBoard(6,4) should return an array like this:

# [
#     ["O","X","O","X"],
#     ["X","O","X","O"],
#     ["O","X","O","X"],
#     ["X","O","X","O"],
#     ["O","X","O","X"],
#     ["X","O","X","O"]
# ]
# And chessBoard(3,7) should return this:

# [
#     ["O","X","O","X","O","X","O"],
#     ["X","O","X","O","X","O","X"],
#     ["O","X","O","X","O","X","O"]
# ]
# The white spaces should be represented by an: 'O'
# and the black an: 'X'

# The first row should always start with a white space 'O'

def chessBoard(rows, columns):
    pass


# __________________________________________________________________________________


# You will be given an array and a limit value. You must check that all values in 
# the array are below or equal to the limit value. If they are, return true. Else, return false.
# You can assume all values in the array are numbers.

# def basic_test_cases():
#         tests = (
#             ([[66, 101] ,200], True),
#             ([[78, 117, 110, 99, 104, 117, 107, 115] ,100], False),

def arrayLimit(arr,limit):
    pass


# ________________________________________________________________________________________________________



# Description:
# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
# Note: anagrams are case insensitive
# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

# Examples
# "foefet" is an anagram of "toffee"

# "Buckethead" is an anagram of "DeathCubeK"

def is_anagram(test, original):
    pass


# _________________________________________________________________________________________________________________


# Description:
# Your task is to write a function which returns the sum of a sequence of integers.
# The sequence is defined by 3 non-negative values: begin, end, step.
# If begin value is greater than the end, your function should return 0. If end is not the result of an integer number of steps, then don't add it to the sum. See the 4th example below.

# Examples

# 2,2,2 --> 2
# 2,6,2 --> 12 (2 + 4 + 6)
# 1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
# 1,5,3  --> 5 (1 + 4)

def sequence_sum(begin_number, end_number, step):
    pass

# ___________________________________________________________________________________________________


# Description:
# Given a list of integers, determine whether the sum of its elements is odd or even.

# Give your answer as a string matching "odd" or "even".

# If the input array is empty consider it as: [0] (array with a zero).

# Examples:
# Input: [0]
# Output: "even"

# Input: [0, 1, 4]
# Output: "odd"

# Input: [0, -1, -5]
# Output: "even"

def odd_or_even(arr):
    pass

# __________________________________________________________________________________________


# Description:
# Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?

# Examples:

# input:    output:
# 0    ->   0
# 2    ->   5
# 3    ->   5
# 12   ->   15
# 21   ->   25
# 30   ->   30
# -2   ->   0
# -5   ->   -5
# etc.
# Input may be any positive or negative integer (including 0).
# You can assume that all inputs are valid integers.

def round_to_next5(n):
    pass

# __________________________________________________________________________________

# Description:
# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def filter_list(l):
    'return a new list with the strings filtered out'
    pass

# __________________________________________________________________________________


# Description:
# Python dictionaries are inherently unsorted. So what do you do if you need to sort the contents of a dictionary?

# Create a function that returns a sorted list of (key, value) tuples (Javascript: arrays of 2 items).

# The list must be sorted by the value and be sorted largest to smallest.

# Examples
# sort_dict({3:1, 2:2, 1:3}) == [(1,3), (2,2), (3,1)]
# sort_dict({1:2, 2:4, 3:6}) == [(3,6), (2,4), (1,2)]

def sort_dict(d):
    return []
sort_dict({1:3,2:2,3:1})

# ______________________________________________________________________________________________________________

# WRITE TEST CASES FOR THESE