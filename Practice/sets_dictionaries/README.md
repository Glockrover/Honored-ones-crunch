# Python Functions for Problem Solving

This repository contains questions for various problem-solving functions in Python. Each function solves a specific problem, and they can be run independently. The functions and examples are explained below.

## Functions

1. **findErrorNums(nums)**: Finds the duplicated and missing numbers in a list.
    - **Example**:
        ```python
        findErrorNums([1, 2, 2, 4])  # Output: [2, 3]
        ```

2. **countPrimeSetBits(left, right)**: Counts numbers in a range with a prime number of set bits in their binary representation.
    - **Example**:
        ```python
        countPrimeSetBits(6, 10)  # Output: 4
        ```

3. **sumIndicesWithKSetBits(nums, k)**: Returns the sum of elements in `nums` where the indices have exactly `k` set bits in binary.
    - **Example**:
        ```python
        sumIndicesWithKSetBits([5, 10, 1, 5, 2], 1)  # Output: 13
        ```

4. **isAlienSorted(words, order)**: Checks if the words are sorted lexicographically in a given alien language order.
    - **Example**:
        ```python
        isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")  # Output: True
        ```

5. **minimizedMaximum(n, quantities)**: Minimizes the maximum number of products allocated to stores.
    - **Example**:
        ```python
        minimizedMaximum(6, [11, 6])  # Output: 3
        ```

6. **longestWord(words)**: Finds the longest word that can be built one character at a time by other words in the list.
    - **Example**:
        ```python
        longestWord(["w", "wo", "wor", "worl", "world"])  # Output: "world"
        ```

7. **twoEditWords(queries, dictionary)**: Finds words in `queries` that can match words in `dictionary` with up to two edits.
    - **Example**:
        ```python
        twoEditWords(["word", "note", "ants"], ["wood", "joke", "moat"])  # Output: ["word", "note"]
        ```

8. **numRollsToTarget(n, k, target)**: Calculates the number of ways to roll `n` dice with `k` faces to get a sum equal to `target`.
    - **Example**:
        ```python
        numRollsToTarget(2, 6, 7)  # Output: 6
        ```

## Running the Tests

To run the tests, make sure you have Python 3 installed, then run:
```bash
python -m unittest test_functions.py
