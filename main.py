# Sapir Natanov 322378068.
# Dor Maudi 207055138.

def is_prime(value):
    """
    the functions get a number and check if it is a prime number.
    :param value: an integer value to be checked.
    :return: whether it is a prime number or not.
    """
    if value <= 1:
        return False
    if value <= 3:
        return True
    if value % 2 == 0 or value % 3 == 0:
        return False
    i = 5
    while i * i <= value:
        if value % i == 0 or value % (i + 2) == 0:
            return False
        i += 6
    return True


def factorSum(num):
    """
    the functions get a number and return the sum of the factor.
    :param num: integer value to be factored.
    :return: the sum of the factors.
    """
    primes = set()
    i = 2
    if num == 1:
        return 1
    while num > 1 and i < num + 1:
        if num % i == 0:
            if is_prime(i):
                primes.add(i)
                num /= i
                i = 1
        i += 1
    return sum(primes)


def onlyPositive(f):
    """
    the functions get a function that takes a number and returns only a positive number.
    :param f: a function that takes 1 argument.
    :return: a lambda that returns the positive number.
    """
    return lambda z: f(abs(z))


def f1(x):
    return x + 1


def interceptPoint(tupA, tupB):
    """
    the functions get two tuples and returns the intercept of the two tuples.
    :param tupA: a tuple with numbers.
    :param tupB: a tuple with numbers.
    :return: the intercept of the two tuples.
    """
    if tupA[0] - tupB[0] == 0 and tupA[1] - tupB[1] != 0:
        return "None"
    elif tupA[0] - tupB[0] == 0 and tupA[1] - tupB[1] == 0:
        return "None"
    else:
        tempA = -1 * (tupA[0] - tupB[0])
        tempB = tupA[1] - tupB[1]
        x = tempB / tempA
        y = tupA[0] * x + tupA[1]
        return x, y


def printNumbers(x, y, z):
    """
    the function gets three numbers and prints all the numbers that are between them and different from z.
    :param x: integer to start the test from.
    :param y: integer to end the test from.
    :param z: integer a number to avoid printing.
    :return: prints all numbers except z.
    """
    if y == x:
        print(y)
        return

    if x < y:
        printNumbers(x, y-1, z)
    elif x > y:
        printNumbers(x, y+1, z)

    if y != z:
        print(y)


def listProduct(listA, listB):
    """
    the function takes two lists and returns the new list that contains all the numbers in the first list
    amount of times in the second list.
    :param listA: a list of numbers that are going to be repeated.
    :param listB: a list of numbers that are telling how many times to repeat.
    :return: a new list with the numbers from the first list the amount of times in the second list.
    """
    list = []
    for i in range(len(listA)):
        for j in range(listB[i]):
            list.append(listA[i])
    return list

def analyze(gradeStr):
    """
    the function takes a string of numbers and get all the grades that are greater or equal to 85.
    :param gradeStr: a string containing grades.
    :return: a number the represents the amount of numbers greater or equal to 85.
    """
    counter = 0
    grades = []
    for i in gradeStr.split(", "):
        grades.append(float(i))

    for i in range(len(grades)):
        if grades[i] >= 85:
            counter += 1
    return counter


if __name__ == '__main__':
    # question 1.
    prime_sum = factorSum(60)
    print("Question 1:")
    print(f"Sum of the prime numbers: {prime_sum}\n")

    # question 2.
    print("Question 2:")
    g = onlyPositive(f1)
    print(g(-2), "\n")

    # question 3.
    print("Question 3:")
    print("Intercept: ", interceptPoint((5, 4), (5, 4)), "\n")

    # question 4.
    print("Question 4:")
    printNumbers(2, -3, -1)

    # question 5.
    print("Question 5:")
    print(listProduct([1, 2, 3], [0, 1, 2]), '\n')

    # question 6.
    print("Question 6:")
    print(analyze("45, 65, 70.4, 82.6, 20.1, 90.8, 76.1, 67.1, 79.9, 85.1"))
