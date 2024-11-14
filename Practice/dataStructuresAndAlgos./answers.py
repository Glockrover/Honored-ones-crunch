def chess_board(rows, columns):
    board = []
    for row in range(rows):
        if row % 2:
            board.append(["X" if not column % 2 else "O" for column in range(columns)])
        else:
            board.append(["O" if not column % 2 else "X" for column in range(columns)])
    return board



print(chess_board(2,6))

# _____________________________________________________________________________________________


def small_enough(array, limit):
    for number in array:
        if number > limit: return False
    return True

# _________________________________________________________________________________________________


def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())


# _________________________________________________________________________________________________


def sequence_sum(begin_number, end_number, step):
    return sum(i for i in range(begin_number, end_number+1, step))

# OR
# RECURSSIVELY
def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    
    if begin_number==end_number:
        return end_number
    else:
        return begin_number + sequence_sum(begin_number+step,end_number,step)
    
# _______________________________________________________________________________________________________

def oddOrEven(arr):
    """determine whether a given list of numbers is odd or even"""
    if sum(arr) % 2 == 0:
        return "even"
    else:
        return "odd"
    
    # OR WITHOUT USING BUILT-IN SUM FUNC

def odd_or_even(arr):
    if len(arr) == 0:
        return 'even'
    if len(arr) == 1 and arr[0] == 0:
        return 'even'
    sum = 0
    for x in range(0,len(arr)):
        sum+=arr[x]
    if sum % 2 == 0:
        return 'even'
    else:
        return 'odd'


# ____________________________________________________________________________________

# recursivelly
def round_to_next5(n):
    return n if n%5 == 0 else round_to_next5(n+1)

# OR
def round_to_next5(n):
    while n%5!=0:
        n+=1
    return n

# __________________________________________________________________________________

def filter_list(l):
    new_list =[]
    for x in l:
        if type(x) == int:
            new_list.append(x)
    return new_list

# ________________________________________________________________________________

def sort_dict(d):
    sor = sorted(d.values(), reverse=True)
    new_list = []

    for num in sor:
        for key, value in d.items():
            if num == value:
                new_list.append((key, value))
                
    return new_list

# or

def sort_dict(d):
  return sorted(d.items(), key=lambda x: x[1], reverse=True)

# ___________________________________________________________________________________