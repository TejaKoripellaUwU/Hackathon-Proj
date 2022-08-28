import random

people=["James", "Sally", "Bob", "Sam", "Rachel", "Michael", "Laura", "Alex"]
objects=["marbles", "pens", "books", "water bottles", "pieces of trash", "pencils", "dollars", "papers"]
g2Functions=[['Adding Two Digit Numbers', 'addProbs'], ['Subtracting Two Digit Numbers', 'subProbs'],
           ['Counting Money', 'moneyProbs'], ['Standard Form', 'standardFormProbs'],
           ['Expanded Form', 'expandedFormProbs'], ['Comparing Two and Three Digit Numbers', 'comparingTwoAndThreeDigitNumsProbs'],
           ['Number Sequences', 'nextInSequenceProbs']]



def addProbs(num):
    problems=[]
    solutions=[]
    used=[]
    for i in range(1, num+1):
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        while ([num1, num2] in used):
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
        used.append([num1, num2])
        if (i<26):
            problem=str('{0}). Find {1} + {2}.'.format(i, num1, num2))
            solution=str('{0}). {1}'.format(i, num1+num2))
        else:
            person1 = random.choice(people)
            object = random.choice(objects)
            problem=str('{0}). {1} has {2} {3}. {1} then makes {4} more. How many total {3} does {1} have?'.format(i, person1, num1, object, num2))
            solution=str('{0}). {1} has {2} {3}.'.format(i, person1, num1 + num2, object))

        problems.append(problem)
        solutions.append(solution)

    return problems, solutions

def subProbs(num):
    problems = []
    solutions = []
    used = []
    for i in range(1, num+1):
        num1 = random.randint(10, 99)
        num2 = random.randint(10, num1)
        while ([num1, num2] in used):
            num1 = random.randint(10, 99)
            num2 = random.randint(10, num1)
        used.append([num1, num2])
        if (i < 26):
            problem = str('{0}). Find {1} - {2}.'.format(i, num1, num2))
            solution = str('{0}). {1}'.format(i, num1-num2))
        else:
            person1 = random.choice(people)
            object = random.choice(objects)
            problem=str('{0}). {1} has {2} {3}. {1} then eats {4} of them. How many {3} does {1} have left?'.format(i, person1, num1, object, num2))
            solution=str('{0}). {1} has {2} {3} left.'.format(i, person1, num1-num2, object))

        problems.append(problem)
        solutions.append(solution)

    return problems, solutions

def moneyProbs(num):
    problems = []
    solutions = []
    used = []
    for i in range(1, num+1):
        if (i < 26):
            randomMax = random.randint(2, 6)
            numQuarters = random.randint(0, min(3, randomMax))
            numNickels = random.randint(0, randomMax - numQuarters)
            numPennies = random.randint(0, randomMax - numQuarters - numNickels)

            while (numPennies + numNickels + numQuarters < 2 and [numQuarters, numNickels, numPennies] in used):
                numQuarters = random.randint(0, min(3, randomMax))
                numNickels = random.randint(0, randomMax - numQuarters)
                numPennies = random.randint(0, randomMax - numQuarters - numNickels)
            used.append([numQuarters, numNickels, numPennies])

            words = str("")
            if(numQuarters>0):  words = str(numQuarters) + " quarters"
            if(numNickels>0):
                if(numQuarters>0):
                    if (numPennies < 1):
                        words = words + " and " + str(numNickels) + " nickels"
                    else:
                       words = words + ", " + str(numNickels) + " nickels"
                else: words = str(numNickels) + " nickels"
            if(numPennies>0):
                if(numQuarters>0 or numNickels>0): words= words + " and " + str(numPennies) + " pennies"
                else: words = str(numPennies) + " pennies"
            problem = str('{0}). What is {1} in cents?'.format(i, words))
            solution = str('{0}). {1} cents.'.format(i, numQuarters*25 + numNickels*5 + numPennies))
        else:
            person1 = random.choice(people)
            person2 = random.choice(people)
            while(person2 == person1):
                person2 = random.choice(people)
            randomMax = random.randint(4, 12)
            totalCoin=0
            while(totalCoin<4):
                quartA = random.randint(0, 3)
                nickA = random.randint(0, randomMax - quartA)
                penA = random.randint(0, randomMax - quartA - nickA)

                quartB = random.randint(0, 3)
                nickB = random.randint(0, randomMax - quartB)
                penB = random.randint(0, randomMax - quartB - nickB)

                totalCoin = quartA + nickA + penA + quartB + nickB + penB

            words1 = str("")
            if (quartA > 0):  words1 = str(quartA) + " quarters"
            if (nickA > 0):
                if (quartA > 0):
                    if(penA < 1):
                        words1 = words1 + " and " + str(nickA) + " nickels"
                    else:
                        words1 = words1 + ", " + str(nickA) + " nickels"

                else:
                    words1 = str(nickA) + " nickels"
            if (penA > 0):
                if (quartA > 0 or nickA > 0):
                    words1 = words1 + " and " + str(penA) + " pennies"
                else:
                    words1 = str(penA) + " pennies"
            words2 = str("")
            if (quartB > 0):  words2 = str(quartB) + " quarters"
            if (nickB > 0):
                if (quartB > 0):
                    if (penB < 1):
                        words2 = words2 + " and " + str(nickB) + " nickels"
                    else:
                        words2 = words2 + ", " + str(nickB) + " nickels"
                else:
                    words2 = str(nickB) + " nickels"
            if (penB > 0):
                if (quartB > 0 or nickB > 0):
                    words2 = words2 + " and " + str(penB) + " pennies"
                else:
                    words2 = str(penB) + " pennies"
            problem=str('{0}). {1} has {2} and {3} has {4}. How much money do they have in total?'.format(i, person1, words1, person2, words2))
            solution=str('{0}). {1} cents.'.format(i, str((quartA+quartB)*25+(nickA+nickB)*5+(penA+penB))))

        problems.append(problem)
        solutions.append(solution)

    return problems, solutions

def standardFormProbs(num):
    problems = []
    solutions = []
    used = []
    for i in range(1, num+1):
        hundreds = random.randint(0, 9)
        tens = random.randint(0, 9)
        ones = random.randint(0, 9)

        while([hundreds, tens, ones] in used or (hundreds < 1 and tens < 1)):
            hundreds = random.randint(0, 9)
            tens = random.randint(0, 9)
            ones = random.randint(0, 9)
        used.append([hundreds, tens, ones])

        if(hundreds > 0):
            problem=str('{0}). Write {1} hundreds, {2} tens, and {3} ones in standard form.'.format(i, hundreds, tens, ones))
        else:
            problem=str('{0}). Write {1} tens and {2} ones in standard form.'.format(i, tens, ones))
        solution=str('{0}). {1}'.format(i, str(hundreds*100+tens*10+ones)))
        problems.append(problem)
        solutions.append(solution)

    return problems, solutions

def expandedFormProbs(num):
    problems = []
    solutions = []
    used = []
    for i in range(1, num+1):
        hundreds = random.randint(0, 9)
        tens = random.randint(0, 9)
        ones = random.randint(0, 9)

        while ([hundreds, tens, ones] in used or (hundreds < 1 and tens < 1)):
            hundreds = random.randint(0, 9)
            tens = random.randint(0, 9)
            ones = random.randint(0, 9)
        used.append([hundreds, tens, ones])

        problem = str('{0}). What is {1}{2}{3} in expanded form?'.format(i, hundreds, tens, ones))
        solution = str('{0}). {1} hundreds, {2} tens, and {3} ones.'.format(i, hundreds, tens, ones))
        problems.append(problem)
        solutions.append(solution)

    return problems, solutions

def comparingTwoAndThreeDigitNumsProbs(num):
    problems=[]
    solutions=[]
    used=[]
    for i in range(1, num):
        funNumber = random.randint(0, 1)
        if(funNumber < 1):
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
        else:
            num1 = random.randint(100, 999)
            num2 = random.randint(100, 999)

        while ([num1, num2] in used):
            if (funNumber < 1):
                num1 = random.randint(10, 99)
                num2 = random.randint(10, 99)
            else:
                num1 = random.randint(100, 999)
                num2 = random.randint(100, 999)
        used.append([num1, num2])
        if (i<26):
            problem=str(i) + "). Fill in the blank with <, >, or =: " + str(num1) +\
                    " _______ " + str(num2)
            if (num1<num2):
                solution=str(i) + "). " + str(num1) + " < " + str(num2)
            elif (num1>num2):
                solution=str(i) + "). " + str(num1) + " > " + str(num2)
            else:
                solution=str(i) + "). " + str(num1) + " = " + str(num2)
        else:
            person1 = random.choice(people)
            person2 = random.choice(people)
            while (person1 == person2):
                person1 = random.choice(people)
                person2 = random.choice(people)
            object=random.choice(objects)
            problem=str(i) + "). " + person1 + " has " + str(num1) + " " + object + ". " + str(person2) + \
                    " has " + str(num2) +  " " + object + ". Who has more " + object + "?"
            if (num1<num2):
                solution=str(i) + "). " + person2 + " has more " + object + "."
            elif (num1>num2):
                solution=str(i) + "). " + person1 + " has more " + object + "."
            else:
                solution=str(i) + "). " + "They have the same amount of " + object + "."
        problems.append(problem)
        solutions.append(solution)

    return problems, solutions

def nextInSequenceProbs(num):
    problems = []
    solutions = []
    used = []
    for i in range(1, num+1):
        num = random.randint(3, 20)
        num = num * random.choice([-1, 1])
        num1 = random.randint(abs(num) * 3 + 10, 500)
        while([num, num1] in used):
            num1 = random.randint(num * 3 + 10, 500)
        used.append([num, num1])
        num2 = num1 + num
        num3 = num2 + num
        problem=str('{0}). Find the next number in the following pattern: {1}, {2}, {3}, ___'.format(i, num1, num2, num3))
        solution=str('{0}). {1}'.format(i, str(num3 + num)))
        problems.append(problem)
        solutions.append(solution)

    return problems, solutions