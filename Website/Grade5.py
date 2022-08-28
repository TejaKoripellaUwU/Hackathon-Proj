import random
from fractions import Fraction

people=["James", "Sally", "Bob", "Sam", "Rachel", "Michael", "Laura", "Alex"]
objects=["marbles", "pens", "books", "water bottles", "pieces of trash", "pencils", "dollars", "papers"]

def multiplyDecimals(num):
    problems = []
    solutions = []
    used = []

    for i in range(1, num+1):
        num1=random.randint(1, 10)
        num2=random.randint(1, 10)
        while ([num1, num2] in used):
            num2=random.randint(1, 10)
            num1=random.randint(1, 10)
        used.append([num1, num2])
        problem = str(i) + ") Multiply: " + str(num1/10) + " * "  + str(num2/10) + " = "
        solution = str(i) + ") " + str(num1/10) + " * "  + str(num2/10) + " = " + str(round((num1/10) * (num2/10), 2))
        problems.append(problem)
        solutions.append(solution)
    return problems, solutions

def multDigitMultiplication(num):
    problems=[]
    solutions=[]
    used=[]
    for i in range(1, num+1):
        num1=random.randint(100, 300)
        num2=random.randint(11, 99)
        while ([num1, num2] in used):
            num2 = random.randint(1, 10)
            num1 = random.randint(1, 10)
        used.append([num1, num2])
        problem=str(i) + ") Multiply: " + str(num1) + " * " + str(num2) + " = "
        solution=str(i) + ") " + str(num1) + " * " + str(num2) + " = " + str(num1*num2)
        problems.append(problem)
        solutions.append(solution)
    return problems, solutions

def dividingFractions(num):
    problems = []
    solutions = []
    used = []
    for i in range(1, num + 1):
        num1 = random.randint(1, 9)
        den1 = random.randint(1, 9)
        num2=random.randint(1, 9)
        den2=random.randint(1, 9)
        while ([num1, num2, den1, den2] in used):
            num1 = random.randint(1, 9)
            den1 = random.randint(1, 9)
            num2 = random.randint(1, 9)
            den2 = random.randint(1, 9)
        used.append([num1, num2, den1, den2])
        problem = str(i) + r") Divide: $ \displaystyle  \frac{" + str(num1) + "}{" + str(den1) + r"} \div  \frac{" + str(num2) + "}{" +str(den2) + "} " + r"\\ $"
        s = str(Fraction(num1 * den2, num2 * den1))
        if ("/" in list(s)):
            solution = str(i) + r") $ \displaystyle  \frac{" + str(num1) + "}{" + str(
                den1) + r"} \div  \frac{" + str(num2) + "}{" + str(den2) + "} = " + \
                r" $ \displaystyle \frac{" + str(s[0:s.index("/")]) + "}{" + str(s[s.index("/")+1:len(s)]) + "} " + r"\\ $"
        else:
            solution=str(i) + r") $ \displaystyle \frac{" + str(num1) + "}{" + str(den1) + r"} \div  \frac{" + str(num2) + "}{" +str(den2) + "} = " + str(s) +r"\\ $"

        problems.append(problem)
        solutions.append(solution)
    return problems, solutions

def multDecByNum(num):
    problems = []
    solutions = []
    used = []

    for i in range(1, num + 1):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        while ([num1, num2] in used):
            num2 = random.randint(1, 10)
            num1 = random.randint(1, 10)
        used.append([num1, num2])
        problem = str(i) + ") Multiply: " + str(num1/10) + " * " + str(num2) + " = "
        solution = str(i) + ") " + str(num1 / 10) + " * " + str(num2) + " = " + str(round((num1 / 10) * (num2), 2))
        problems.append(problem)
        solutions.append(solution)
    return problems, solutions

def addDec(num):
    problems = []
    solutions = []
    used = []

    for i in range(1, num + 1):
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        while ([num1, num2] in used):
            num2 = random.randint(1, 1000)
            num1 = random.randint(1, 1000)
        used.append([num1, num2])
        n1=random.choice([10, 100])
        n2=random.choice([10, 100])
        problem = str(i) + ") Add: " + str(num1 / n1) + " + " + str(num2 / n2) + " = "
        solution = str(i) + ") " + str(num1 / n1) + " + " + str(num2 / n2) + " = " + str(round((num1 / n1) + (num2 / n2), 2))
        problems.append(problem)
        solutions.append(solution)
    return problems, solutions

def subDec(num):
    problems = []
    solutions = []
    used = []

    for i in range(1, num + 1):
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        n1 = random.choice([10, 100])
        n2 = random.choice([10, 100])
        while ([num1, num2] in used or ((num1/n1)-(num2/n2)<0)):
            num2 = random.randint(1, 1000)
            num1 = random.randint(1, 1000)
            n1 = random.choice([10, 100])
            n2 = random.choice([10, 100])
        used.append([num1, num2])

        problem = str(i) + ") Subtract: " + str(num1 / n1) + " - " + str(num2 / n2) + " = "
        solution = str(i) + ") " + str(num1 / n1) + " - " + str(num2 / n2) + " = " + str(round((num1 / n1) - (num2 / n2), 2))
        problems.append(problem)
        solutions.append(solution)
    return problems, solutions

def multiDigitDiv(num):
    problems = []
    solutions = []
    used = []
    for i in range(1, num + 1):
        num1 = random.randint(1, 9)
        num2 = random.randint(11, 50)
        while ([num1, num2] in used):
            num2 = random.randint(1, 9)
            num1 = random.randint(11, 50)
        used.append([num1, num2])
        problem = str(i) + ") Divide: " + str(num1*num2) + " / " + str(num1) + " = "
        solution = str(i) + ") " + str(num1*num2) + " / " + str(num1) + " = " + str(num2)
        problems.append(problem)
        solutions.append(solution)
    return problems, solutions

def roundingDec(num):
    problems = []
    solutions = []
    used = []

    for i in range(1, num + 1):
        num1 = random.randint(1, 700)
        while ([num1] in used):
            num1 = random.randint(1, 700)
        used.append([num1])
        n1 = random.choice([1000, 10000])
        n2=random.choice(["tenth", "hundredth", "thousandth"])
        if (n2=="tenth"):
            s=round(num1/n1, 1)
        elif (n2=="hundredth"):
            s=round(num1/n1, 2)
        else:
            s=round(num1/n1, 3)
        problem = str(i) + ") Round to the nearest " + n2 + ": " +  str(num1/n1)
        solution = str(i) + ") " + str(num1/n1) + " rounded to the nearest " + n2 + " = " + str(s)
        problems.append(problem)
        solutions.append(solution)
    return problems, solutions

functions=[["Multiplying Decimals", multiplyDecimals(30), 0, 0], ["Multi-Digit Multiplication", multDigitMultiplication(30), 0, 0],
            ["Multi-Digit Division", multiDigitDiv(30), 0, 0], ["Dividing Fractions", dividingFractions(30), 1, 1], ["Multiplying Decimals by Numbers", multDecByNum(30), 0, 0],
            ["Adding Decimals", addDec(30), 0, 0], ["Subtracting Decimals", subDec(30), 0, 0], ["Rounding Decimals", roundingDec(30), 0, 0]]