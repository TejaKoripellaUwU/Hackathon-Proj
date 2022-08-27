import random

people=["James", "Sally", "Bob", "Sam", "Rachel", "Michael", "Laura", "Alex"]
objects=["marbles", "pens", "books", "water bottles", "pieces of trash", "pencils", "dollars", "papers"]

def comparingTwoDigitNums(num):
    problems=[]
    solutions=[]
    used=[]
    for i in range(1, num+1):
        num1=random.randint(1, 99)
        num2=random.randint(1, 99)
        while ([num1, num2] in used):
            num1 = random.randint(1, 99)
            num2 = random.randint(1, 99)
        used.append([num1, num2])
        if (i<26):
            problem=str(i) + ") Fill in the blank with <, >, or =: " + str(num1) +\
                    " _______ " + str(num2)
            if (num1<num2):
                solution=str(i) + ") " + str(num1) + " < " + str(num2)
            elif (num1>num2):
                solution=str(i) + ") " + str(num1) + " > " + str(num2)
            else:
                solution=str(i) + ") " + str(num1) + " = " + str(num2)
        else:
            person1 = random.choice(people)
            person2 = random.choice(people)
            while (person1 == person2):
                person1 = random.choice(people)
                person2 = random.choice(people)
            object=random.choice(objects)
            problem=str(i) + ") " + person1 + " has " + str(num1) + " " + object + ". " + str(person2) + \
                    " has " + str(num2) +  " " + object + ". Who has more " + object + "?"
            if (num1<num2):
                solution=str(i) + ") " + person2 + " has more " + object + "."
            elif (num1>num2):
                solution=str(i) + ") " + person1 + " has more " + object + "."
            else:
                solution=str(i) + ") " + "They have the same amount of " + object + "."
        problems.append(problem)
        solutions.append(solution)

    return problems, solutions

def addingNumsWithin20(num):
    problems = []
    solutions = []
    used = []

    for i in range(1, num+1):
        num1=random.randint(1, 70)
        op=random.choice(['+', '-'])
        if (op=='+'):
            num2=num1+random.randint(1, 20)
        else:
            num2=num1=random.randint(1, 20)

        while ([num1, num2] in used):
            num1 = random.randint(1, 70)
            op = random.choice(['+', '-'])
            if (op == '+'):
                num2 = num1 + random.randint(1, 20)
            else:
                num2 = num1 = random.randint(1, 20)
        used.append([num1, num2])
        if (i<26):
            problem=str(i) + ") " + str(num1) + " + " + str(num2) + " = "
            solution=str(i) + ") " + str(num1) + " + " + str(num2) + " = " + str(num1 + num2)
        else:
            person1 = random.choice(people)
            person2 = random.choice(people)
            while (person1 == person2):
                person1 = random.choice(people)
                person2 = random.choice(people)
            object=random.choice(objects)
            problem=str(i) + ") " + person1 + " has " + str(num1) + " " + object + ". " + str(person2) + \
                    " has " + str(num2) +  " more " + object + " than " + person1 + ". How many " + object \
                    + " does " + person2 + " have?"
            solution=str(i) + ") " + person2 + " has " + str(num1 + num2) + " " + object + "."
        problems.append(problem)
        solutions.append(solution)
    return problems, solutions

def addingNumsWithin20(num):
    problems = []
    solutions = []
    used = []

    for i in range(1, num+1):
        num1=random.randint(1, 70)
        op=random.choice(['+', '-'])
        if (op=='+'):
            num2=num1+random.randint(1, 20)
        else:
            num2=num1=random.randint(1, 20)

        while ([num1, num2] in used):
            num1 = random.randint(1, 70)
            op = random.choice(['+', '-'])
            if (op == '+'):
                num2 = num1 + random.randint(1, 20)
            else:
                num2 = num1 = random.randint(1, 20)
        used.append([num1, num2])
        if (i<26):
            problem=str(i) + ") " + str(num1) + " + " + str(num2) + " = _______"
            solution=str(i) + ") " + str(num1) + " + " + str(num2) + " = " + str(num1 + num2)
        else:
            person1 = random.choice(people)
            person2 = random.choice(people)
            while (person1 == person2):
                person1 = random.choice(people)
                person2 = random.choice(people)
            object=random.choice(objects)
            problem=str(i) + ") " + person1 + " has " + str(num1) + " " + object + ". " + str(person2) + \
                    " has " + str(num2) +  " more " + object + " than " + person1 + ". How many " + object \
                    + " does " + person2 + " have?"
            solution=str(i) + ") " + person2 + " has " + str(num1 + num2) + " " + object + "."
        problems.append(problem)
        solutions.append(solution)
    return problems, solutions

def subtractingNumsWithin20(num):
    problems = []
    solutions = []
    used = []

    for i in range(1, num+1):
        num1=random.randint(21, 99)
        num2=random.randint(1, 20)

        while ([num1, num2] in used):
            num1 = random.randint(21, 99)
            num2=random.randint(1, 20)
        used.append([num1, num2])
        if (i<26):
            problem=str(i) + ") " + str(num1) + " - " + str(num2) + " = _______"
            solution=str(i) + ") " + str(num1) + " - " + str(num2) + " = " + str(num1 - num2)
        else:
            person1 = random.choice(people)
            person2 = random.choice(people)
            while (person1 == person2):
                person1 = random.choice(people)
                person2 = random.choice(people)
            object=random.choice(objects)
            problem=str(i) + ") " + person1 + " has " + str(num1) + " " + object + ". " + str(person2) + \
                    " has " + str(num2) +  " less " + object + " than " + person1 + ". How many " + object \
                    + " does " + person2 + " have?"
            solution=str(i) + ") " + person2 + " has " + str(num1 - num2) + " " + object + "."
        problems.append(problem)
        solutions.append(solution)
    return problems, solutions

def missingNumber(num):
    problems = []
    solutions = []
    used = []

    for i in range(1, num+1):
        num1=random.randint(1, 45)
        num2=random.randint(46, 90)

        while ([num1, num2] in used):
            num1 = random.randint(1, 45)
            num2=random.randint(45, 90)
        used.append([num1, num2])
        if (i<26):
            problem=str(i) + ") Fill in the blank: " + str(num1) + " + ________" + " = " + str(num2)
            solution=str(i) + ") " + str(num1) + " + " + str(num2-num1) + " = " + str(num2)
        else:
            person1 = random.choice(people)
            person2 = random.choice(people)
            while (person1 == person2):
                person1 = random.choice(people)
                person2 = random.choice(people)
            object=random.choice(objects)
            problem=str(i) + ") " + person1 + " has " + str(num1) + " " + object + ". " + str(person2) + \
                    " has an unknown number of " + object + ". In total, they have " + str(num2) + " " + object \
                    + ". How many " + object + " does " + person2 + " have?"
            solution=str(i) + ") " + person2 + " has " + str(num2 - num1) + " " + object + "."
        problems.append(problem)
        solutions.append(solution)
    return problems, solutions

def addingThreeNumbers(num):
    problems = []
    solutions = []
    used = []

    for i in range(1, num + 1):
        num1 = random.randint(2, 20)
        num2=random.randint(2, 20)
        num3=random.randint(2, 20)


        while ([num1, num2, num3] in used):
            num1 = random.randint(2, 20)
            num2 = random.randint(2, 20)
            num3 = random.randint(2, 20)
        used.append([num1, num2, num3])
        if (i < 26):
            problem = str(i) + ") " + str(num1) + " + " + str(num2) + " + " + str(num3) + " = ____"
            solution = str(i) + ") " + str(num1) + " + " + str(num2) + " + " + str(num3) + " = " + str(num1 + num2+num3)
        else:
            person1 = random.choice(people)
            person2 = random.choice(people)
            person3=random.choice(people)
            while (person1 == person2 or person1==person3 or person2==person3):
                person1 = random.choice(people)
                person2 = random.choice(people)
                person3=random.choice(people)
            object = random.choice(objects)
            problem = str(i) + ") " + person1 + " has " + str(num1) + " " + object + ". " + str(person2) + \
                " has " + str(num2) + " " + object + ". " + person3 + " has " + str(num3) + " " + object \
                + ". How many " + object + " do they have in all?"
            solution = str(i) + ") " + person1 + ", " + person2 + ", and " + person3 + " have a total of " \
                + str(num1+num2+num3) + " " + object + "."
        problems.append(problem)
        solutions.append(solution)
    return problems, solutions

def beforeAfter(num):
    problems = []
    solutions = []
    used = []

    for i in range(1, num + 1):
        num1 = random.randint(10, 150)
        num2=random.randint(1, 10)
        before=random.choice(["before", "after"])

        while ([num1, num2, before] in used):
            num1 = random.randint(10, 150)
            num2 = random.randint(1, 10)
            before = random.choice(["before", "after"])
        used.append([num1, num2, before])

        if (before=="before"):
            sol=num1-num2
        else:
            sol=num2+num1

        problem = str(i) + ") What number comes " + str(num2) + " " + before + " " + str(num1) + "?"
        solution = str(i) + ") " + str(sol) + " comes " + str(num2) + " " + before + " " + str(num1) + "."

        problems.append(problem)
        solutions.append(solution)
    return problems, solutions

def basicPlaceValue(num):
    problems = []
    solutions = []
    used = []

    for i in range(1, num + 1):
        num1 = random.randint(2, 10)
        num2 = random.randint(2, 9)

        while ([num1, num2] in used):
            num1 = random.randint(2, 10)
            num2 = random.randint(2, 9)
        used.append([num1, num2])

        problem = str(i) + ") What number is equivalent to " + str(num1) + " tens and " +  str(num2) + " ones?"
        solution = str(i) + ") " + str(num1*10 + num2) + " is equivalent to  " + str(num1) + " tens and " + str(num2) + " ones."

        problems.append(problem)
        solutions.append(solution)
    return problems, solutions

def breakingApartNums(num):
    problems = []
    solutions = []
    used = []

    for i in range(1, num + 1):
        num1 = random.randint(1, 45)
        num2 = random.randint(1, 45)

        while ([num1, num2] in used):
            num1 = random.randint(1, 45)
            num2 = random.randint(1, 45)
        used.append([num1, num2])

        problem = str(i) + ") Break apart the solution of " + str(num1) + " + " + str(num2) \
            + " into tens and ones"
        solution = str(i) + ") " + str(num1) + " + " + str(num2) + " is equivalent to " + str(int((((num1+num2)-((num1+num2)%10))/10))) + \
            " tens " + str((num1+num2)%10) + " ones."
        problems.append(problem)
        solutions.append(solution)
    return problems, solutions

def main():
    #problems, solutions=comparingTwoDigitNums(30)
    #problems, solutions=addingNumsWithin20(30)
    #problems, solutions = subtractingNumsWithin20(30)
    #problems, solutions=missingNumber(30)
    #problems, solutions=addingThreeNumbers(30)
    #problems, solutions=beforeAfter(30)
    #problems, solutions=basicPlaceValue(30)
    problems, solutions=breakingApartNums(30)
    for i in problems:
        print(i)
    for i in solutions:
        print(i)
main()