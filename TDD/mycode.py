def main():
    
    logic = input('Enter logic: ')
    num1, opperation, num2 = logic.split(" ")
    num1 = int(num1)
    num2 = int(num2)
    
    if opperation == "+":
        print(f"Your answer is {add(num1, num2)}")

    elif opperation == "-":
        print(f"Your answer is {sub(num1, num2)}")

    elif opperation == "*":
        print(f"Your answer is {multiply(num1, num2)}")

    elif opperation == "/":
        print(f"Your answer is {divide(num1, num2)}")

    else:
        print("Invalid opperation.")


def add(num1, num2):
    try:
        return num1 + num2
    except ValueError:
        pass

def sub(num1, num2):

    try:
        return num1 - num2
    except ValueError:
        pass

def multiply(num1, num2):
    try:
        return num1 * num2
    except ValueError or TypeError:
        pass

def divide(num1, num2):
    try:
        total = num1/ num2
        return round(total, 2)
    except ZeroDivisionError:
        return "Invalid"
if __name__ == "__main__":
    main()