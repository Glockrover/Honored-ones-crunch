def findErrorNums(nums):
    """
    You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

    You are given an integer array nums representing the data status of this set after the error.

    Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

    Example 1:

    Input: nums = [1,2,2,4]
    Output: [2,3]

    Example 2:

    Input: nums = [1,1]
    Output: [1,2]

 

Constraints:

    2 <= nums.length <= 104
    1 <= nums[i] <= 104

    :type nums: List[int]
    :rtype: List[int]

    """
    new = list()
    for i in range(1, len(nums)):
        if i not in new:
            new.append(i)
    print(new)

findErrorNums([1,1])

def countPrimeSetBits(left, right):
    """
    Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

    Recall that the number of set bits an integer has is the number of 1's present when written in binary.

    For example, 21 written in binary is 10101, which has 3 set bits.

 

    Example 1:

    Input: left = 6, right = 10
    Output: 4
    Explanation:
    6  -> 110 (2 set bits, 2 is prime)
    7  -> 111 (3 set bits, 3 is prime)
    8  -> 1000 (1 set bit, 1 is not prime)
    9  -> 1001 (2 set bits, 2 is prime)
    10 -> 1010 (2 set bits, 2 is prime)
    4 numbers have a prime number of set bits.

    Example 2:

    Input: left = 10, right = 15
    Output: 5
    Explanation:
    10 -> 1010 (2 set bits, 2 is prime)
    11 -> 1011 (3 set bits, 3 is prime)
    12 -> 1100 (2 set bits, 2 is prime)
    13 -> 1101 (3 set bits, 3 is prime)
    14 -> 1110 (3 set bits, 3 is prime)
    15 -> 1111 (4 set bits, 4 is not prime)
    5 numbers have a prime number of set bits.

    

    Constraints:

        1 <= left <= right <= 106
        0 <= right - left <= 104



    Args:
        left (int)
        right (int)
    """
    pass


def sumIndicesWithKSetBits(nums,k):
    """
    You are given a 0-indexed integer array nums and an integer k.

    Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits in their binary representation.

    The set bits in an integer are the 1's present when it is written in binary.

    For example, the binary representation of 21 is 10101, which has 3 set bits.

 

    Example 1:

    Input: nums = [5,10,1,5,2], k = 1
    Output: 13
    Explanation: The binary representation of the indices are: 
    0 = 0002
    1 = 0012
    2 = 0102
    3 = 0112
    4 = 1002 
    Indices 1, 2, and 4 have k = 1 set bits in their binary representation.
    Hence, the answer is nums[1] + nums[2] + nums[4] = 13.

    Example 2:

    Input: nums = [4,3,2,1], k = 2
    Output: 1
    Explanation: The binary representation of the indices are:
    0 = 002
    1 = 012
    2 = 102
    3 = 112
    Only index 3 has k = 2 set bits in its binary representation.
    Hence, the answer is nums[3] = 1.

 

    Constraints:

        1 <= nums.length <= 1000
        1 <= nums[i] <= 105
        0 <= k <= 10



    Args:
        nums (List[int])
        k (int)
        return: int
    """
    pass


def isAlienSorted(words, order):
    """
    In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

    Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

    Example 1:

    Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

    Example 2:

    Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
    Output: false
    Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

    Example 3:

    Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
    Output: false
    Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

    

    Constraints:

        1 <= words.length <= 100
        1 <= words[i].length <= 20
        order.length == 26
        All characters in words[i] and order are English lowercase letters.




     Args:
        type words: List[str]
        type order: str
        return type: bool
    """
    pass


def minimizedMaximum(n, quantities):
    """
    You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, where quantities[i] represents the number of products of the ith product type.

    You need to distribute all products to the retail stores following these rules:

    A store can only be given at most one product type but can be given any amount of it.
    After distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given to any store. You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.

    Return the minimum possible x.

 

    Example 1:

    Input: n = 6, quantities = [11,6]
    Output: 3
    Explanation: One optimal way is:
    - The 11 products of type 0 are distributed to the first four stores in these amounts: 2, 3, 3, 3
    - The 6 products of type 1 are distributed to the other two stores in these amounts: 3, 3
    The maximum number of products given to any store is max(2, 3, 3, 3, 3, 3) = 3.

    Example 2:

    Input: n = 7, quantities = [15,10,10]
    Output: 5
    Explanation: One optimal way is:
    - The 15 products of type 0 are distributed to the first three stores in these amounts: 5, 5, 5
    - The 10 products of type 1 are distributed to the next two stores in these amounts: 5, 5
    - The 10 products of type 2 are distributed to the last two stores in these amounts: 5, 5
    The maximum number of products given to any store is max(5, 5, 5, 5, 5, 5, 5) = 5.

    Example 3:

    Input: n = 1, quantities = [100000]
    Output: 100000
    Explanation: The only optimal way is:
    - The 100000 products of type 0 are distributed to the only store.
    The maximum number of products given to any store is max(100000) = 100000.

    

    Constraints:

        m == quantities.length
        1 <= m <= n <= 105
        1 <= quantities[i] <= 105

     Args:
        type n: int
        type quantities: List[int]
        return type: int
    """
    pass


def longestWord(words):
    """
    Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

    If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

    Note that the word should be built from left to right with each additional character being added to the end of a previous word. 

    

    Example 1:

    Input: words = ["w","wo","wor","worl","world"]
    Output: "world"
    Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

    Example 2:

    Input: words = ["a","banana","app","appl","ap","apply","apple"]
    Output: "apple"
    Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

    

    Constraints:

        1 <= words.length <= 1000
        1 <= words[i].length <= 30
        words[i] consists of lowercase English letters.


        :type words: List[str]
        :rtype: str
    """
    pass


def twoEditWords(queries, dictionary):
    """
    You are given two string arrays, queries and dictionary. All words in each array comprise of lowercase English letters and have the same length.

In one edit you can take a word from queries, and change any letter in it to any other letter. Find all words from queries that, after a maximum of two edits, equal some word from dictionary.

Return a list of all words from queries, that match with some word from dictionary after a maximum of two edits. Return the words in the same order they appear in queries.

 

Example 1:

Input: queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
Output: ["word","note","wood"]
Explanation:
- Changing the 'r' in "word" to 'o' allows it to equal the dictionary word "wood".
- Changing the 'n' to 'j' and the 't' to 'k' in "note" changes it to "joke".
- It would take more than 2 edits for "ants" to equal a dictionary word.
- "wood" can remain unchanged (0 edits) and match the corresponding dictionary word.
Thus, we return ["word","note","wood"].

Example 2:

Input: queries = ["yes"], dictionary = ["not"]
Output: []
Explanation:
Applying any two edits to "yes" cannot make it equal to "not". Thus, we return an empty array.

 

Constraints:

    1 <= queries.length, dictionary.length <= 100
    n == queries[i].length == dictionary[j].length
    1 <= n <= 100
    All queries[i] and dictionary[j] are composed of lowercase English letters.


        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
    pass


def numRollsToTarget(n, k, target):
    """
    You have n dice, and each dice has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.

Example 2:

Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:

Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 109 + 7.

 

Constraints:

    1 <= n, k <= 30
    1 <= target <= 1000



    :type n: int
    :type k: int
    :type target: int
    :rtype: int
    """
    pass