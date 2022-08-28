import random
from fractions import Fraction
import math
#I NEVER WANT TO LOOK AT A FRACTION EVER AGAIN
people=["James", "Sally", "Bob", "Sam", "Rachel", "Michael", "Laura", "Alex"]
objects=["marbles", "pens", "books", "water bottles", "pieces of trash", "pencils", "dollars", "papers"]
fractionObjects=["of a pizza", "of a pie", "of a cake", "liters of juice", "of a lasagna", "of a tree", "of a piece of wood"]
actions=["slept", "swam", "hiked", "played video games", "read", "watched TV", "baked cookies", "sold potatoes"]
g4Functions=[['Rounding Numbers', 'roundingNums'], ['Dividing Numbers', 'dividingNums'],
           ['Prime and Composite Numbers', 'primeComposite'], ['Comparing Fractions', 'compareFractions'],
           ['Adding and Subtracting Fractions', 'addSubFrac'], ['Multiplying Fractions', 'multiplyFrac'],
           ['Converting Decimals to Fractions', 'decToFrac'], ['Area', 'Area'], ['Converting Time', 'Time']]


# DONE + DONE
def roundingNums(amt):
    problems=[]
    solutions=[]
    for i in range(1 ,amt + 1):
        placeValues=[10,100,1000]
        number = random.randint(0,9999)
        if number >= 1000:
            sheet = random.randint(-3,-1)
        elif number>=100:
            sheet = random.randint(-2,-1)
        else:
            sheet = -1
        if(i < 26):
            problem=str('{0}). Round {1} to the nearest {2}s place.'.format(i, number, placeValues[abs(sheet)-1]))
            solution=str('{0}). {1}'.format(i, round(number,sheet)))
        else:
            person=random.choice(people)
            thing=random.choice(objects)
            problem=str('{0}). {1} has {2} {3}. What is {2} {3} rounded to the nearest {4}s place?'.format(i, person, number, thing, placeValues[abs(sheet)-1]))
            solution=str('{0}). {1} {2}.'.format(i, round(number,sheet), thing))

        problems.append(problem)
        solutions.append(solution)
    return problems,solutions

#DONE + DONE
def dividingNums(amt):
    problems=[]
    solutions=[]
    used=[]
    for i in range(1, amt + 1):
        answer = random.randint(0, 4) #resultant
        num2 = random.randint(2, 20) #divisor
        remainder = random.randint(0, num2 - 1)
        num1 = num2 * answer + remainder #starting whole number
        while([answer, num2, num1, remainder] in used):
            answer = random.randint(0, 4)
            num2 = random.randint(2, 20)
            remainder = random.randint(0, num2 - 1)
            num1 = num2 * answer + remainder
        used.append([answer, num2, num1, remainder])
        if (i < 26):
            problem = str('{0}). What is {1} divided by {2}? Use the remainder in your answer'.format(i, num1, num2))
            solution = str('{0}). {1} remainder {2}'.format(i, answer, remainder))
        else:
            person = random.choice(people)
            thing = random.choice(objects)
            problem = str('{0}). {1} has {2} {3}. {1} then gives {4} people an equal amount of {3}. If {1} kept the remainder, how many {3} would {1} have left?'.format(i, person, num1,thing, num2))
            solution = str('{0}). {1} would have {2} {3} left.'.format(i, person, remainder, thing))
        problems.append(problem)
        solutions.append(solution)

    return problems,solutions

#DONE
def primeComposite(amt):
    problems=[]
    solutions=[]
    #moved out of loop :skull:
    def primesInRange(x, y):
        prime_list = []
        compList = []
        for n in range(x, y):
            isPrime = True
            for num in range(2, n):
                if n % num == 0:
                    isPrime = False
            if isPrime:
                prime_list.append(n)
            else:
                compList.append(n)
        return prime_list, compList

    for i in range(1 ,amt + 1):
        pOrC = random.choice(["prime", "composite"])

        if pOrC == "prime":
            primes,composites = primesInRange(1,90)
            randprime = primes[random.randint(0,len(primes)-1)]
            primes.remove(primes[random.randint(0,len(primes)-1)])

            if(i<26):
                problem=str('{0}). Is {1} prime or composite?'.format(i, randprime))
            else:
                person=random.choice(people)
                thing=random.choice(objects)
                problem=str('{0}). {1} has {2} {3}. Do they have a prime or composite amount of {3}?'.format(i, person, randprime, thing))
            solution = str('{0}). Prime.'.format(i))
        else:
            primes,composites = primesInRange(0,90)
            randComposite = composites[random.randint(0,len(composites)-1)]
            composites.remove(composites[random.randint(0,len(composites)-1)])

            if(i<26):
                problem=str('{0}). Is {1} prime or composite?'.format(i, randComposite))
            else:
                person=random.choice(people)
                thing=random.choice(objects)
                problem = str(
                    '{0}). {1} has {2} {3}. Do they have a prime or composite amount of {3}?'.format(i, person, randprime, thing))
            solution = str('{0}). Composite.'.format(i))
        problems.append(problem)
        solutions.append(solution)

    return problems, solutions

#DONE?
def compareFractions(amt):
    problems=[]
    solutions=[]
    used = []
    for i in range (1 ,amt + 1):
        operations = [">","<","="]
        operation = 0
        frac1Num = random.randint(1,20)
        frac1Den = random.randint(2,20)
        frac2Num = random.randint(1,20)
        frac2Den = random.randint(2,20)
        frac1 = Fraction(frac1Num,frac1Den)
        frac2 = Fraction(frac2Num, frac2Den)
        while ([frac1,frac2] in used):
            frac1Num = random.randint(1, 20)
            frac1Den = random.randint(2, 20)
            frac2Num = random.randint(1, 20)
            frac2Den = random.randint(2, 20)
            frac1 = Fraction(frac1Num,frac1Den)
            frac2 = Fraction(frac2Num, frac2Den)
        used.append([frac1,frac2])
        fraction1=str('{0}/{1}'.format(frac1Num, frac1Den))
        fraction2=str('{0}/{1}'.format(frac2Num, frac2Den))
        if frac1>frac2:
            operation = 0
        elif frac1<frac2:
            operation = 1
        elif frac1==frac2:
            operation = 2
        if(i < 26):
            problem=str('{0}). Fill in the blank with >, <, or = {1} ___ {2}'.format(i, fraction1, fraction2))
            solution=str('{0}). {1}'.format(i, operations[operation]))
        else:
            person1=random.choice(people)
            person2=random.choice(people)
            while(person2 == person1):
                person2=random.choice(people)
            thing=random.choice(fractionObjects)
            problem=str('{0}). {1} has {2} {3} while {4} has {5} {3}. Who has more?'.format(i, person1, fraction1, thing, person2, fraction2))
            if(operation==0):
                solution=str('{0}). {1} has more than {2}.'.format(i, person1, person2))
            elif(operation==1):
                solution=str('{0}). {1} has more than {2}.'.format(i, person2, person1))
            else:
                solution=str('{0}). They have the same amount'.format(i))
        problems.append(problem)
        solutions.append(solution)
    return problems,solutions

#DONE
def addSubFrac(amt):
    problems=[]
    solutions=[]
    used = []
    for i in range(1 ,amt + 1):
        sign = random.choice(["subtract","add"])
        if sign == "add":
            frac1Num = random.randint(1,20)
            frac1Den = random.randint(2,20)
            frac2Num = random.randint(1,20)
            frac2Den = frac1Den
            frac1 = Fraction(frac1Num,frac1Den)
            frac2 = Fraction(frac2Num, frac2Den)
            while ([frac1,frac2] in used):
                frac1Num = random.randint(1,20)
                frac1Den = random.randint(2,20)
                frac2Num = random.randint(1,20)
                frac2Den = frac1Den
                frac1 = Fraction(frac1Num,frac1Den)
                frac2 = Fraction(frac2Num, frac2Den)
            fraction1 = str('{0}/{1}'.format(frac1Num, frac1Den))
            fraction2 = str('{0}/{1}'.format(frac2Num, frac2Den))
            if(i<26):
                problem=str('{0}). Add and simplify the following fractions: {1} + {2}'.format(i, fraction1, fraction2))
                solution=str('{0}). {1}'.format(i, frac1+frac2))
            else:
                person=random.choice(people)
                thing=random.choice(fractionObjects)
                problem=str('{0}). {1} has {2} {3}. {1} then receives another {4} {3}. How much do they have in total?'.format(i, person, fraction1, thing, fraction2))
                solution = str('{0}). {1} {2}.'.format(i, frac1 + frac2, thing))
        else:
            frac1Num = random.randint(1,20)
            frac1Den = random.randint(2,20)
            frac2Num = random.randint(1,frac1Num)
            frac2Den = frac1Den
            frac1 = Fraction(frac1Num,frac1Den)
            frac2 = Fraction(frac2Num, frac2Den)
            while ([frac1,frac2] in used):
                frac1Num = random.randint(1,20)
                frac1Den = random.randint(2,20)
                frac2Num = random.randint(1,frac1Num)
                frac2Den = frac1Den
                frac1 = Fraction(frac1Num,frac1Den)
                frac2 = Fraction(frac2Num, frac2Den)
            fraction1 = str('{0}/{1}'.format(frac1Num, frac1Den))
            fraction2 = str('{0}/{1}'.format(frac2Num, frac2Den))
            if (i < 26):
                problem = str(
                    '{0}). Subtract and simplify the following fractions: {1} + {2}'.format(i, fraction1, fraction2))
                solution = str('{0}). {1}'.format(i, frac1 - frac2))
            else:
                person = random.choice(people)
                thing = random.choice(fractionObjects)
                person = str(
                    '{0}). {1} has {2} {3}. {1} then consumes {4} {3}. How much do they have left?'.format(
                        i, person, fraction1, thing, fraction2))
                solution = str('{0}). {1} {2}.'.format(i, frac1 - frac2, thing))
        problems.append(problem)
        solutions.append(solution)

    return problems,solutions

#DONE
def multiplyFrac(amt):
    problems=[]
    solutions=[]
    used = []
    for i in range (1 ,amt + 1):
        frac1Num = random.randint(2,10)
        frac1Den = random.randint(2,10)
        frac2Num = random.randint(2,10)
        frac2Den = random.randint(2,10)
        frac1 = Fraction(frac1Num,frac1Den)
        frac2 = Fraction(frac2Num, frac2Den)
        while ([frac1,frac2] in used):
            frac1Num = random.randint(2,10)
            frac1Den = random.randint(2,10)
            frac2Num = random.randint(2,10)
            frac2Den = random.randint(2,10)
            frac1 = Fraction(frac1Num,frac1Den)
            frac2 = Fraction(frac2Num, frac2Den)
        fraction1 = str('{0}/{1}'.format(frac1Num, frac1Den))
        fraction2 = str('{0}/{1}'.format(frac2Num, frac2Den))
        problem=str('{0}). Multiply and Simplify the following fractions: {1} x {2}'.format(i, fraction1, fraction2))
        solution=str('{0}). {1}'.format(i, frac1 * frac2))
        problems.append(problem)
        solutions.append(solution)
    return problems,solutions

#DONE
def decToFrac(amt):
    problems=[]
    solutions=[]
    used=[]
    for i in range(1 ,amt + 1):
        toFrac = random.choice([True,False])
        frac1Num = random.randint(2,20)
        frac1Den = random.randint(2,20)
        frac1 = Fraction(frac1Num,frac1Den)
        dec1 = frac1Num/frac1Den
        n = len(str(dec1).split(".")[1])
        while (n>2 or [frac1,dec1] in used):
            frac1Num = random.randint(2,10)
            frac1Den = random.randint(2,10)
            dec1 = frac1Num/frac1Den
            n = len(str(dec1).split(".")[1])
        used.append([frac1, dec1])
        if toFrac:
            problem=str('{0}). Convert the decimal {1} to a fraction'.format(i, dec1))
            solution=str('{0}). {1}'.format(i, frac1))
        else:
            problem = str('{0}). Convert the fraction {1} to a decimal'.format(i, frac1))
            solution = str('{0}). {1}'.format(i, dec1))
        problems.append(problem)
        solutions.append(solution)
    return problems,solutions

#WHAT IS THIS
def Area(amt):
    problems=[]
    solutions=[]
    for i in range(1 ,amt + 1):
        problemType = random.choice(["volume", "area", "perimeter"])
        if problemType == "volume":
            shapeType = random.choice(["cube", "rectangularPrism"])
            if shapeType == "cube":
                sideLength1 = random.randint(1,10)
                problem=str('{0}). What is the volume of a cube with a side length of {1}?'.format(i, sideLength1))
                solution=str('{0}). {1}'.format(i, sideLength1**3))
            if shapeType == "rectangularPrism":
                sideLength1 = random.randint(1,10)
                sideLength2 = random.randint(1,10)
                sideLength3 = random.randint(1,10)
                problem=str('{0}). What is the volume of a rectangular prism with side lengths of {1}, {2}, and {3}?'.format(i, sideLength1, sideLength2, sideLength3))
                solution=str('{0}). {1}'.format(i, sideLength1*sideLength2*sideLength3))
        elif problemType == "area":
            shapeType = random.choice(["square", "rectangle", "triangle"])
            if shapeType == "square":
                sideLength1 = random.randint(1,10)
                problem=str('{0}). What is the area of a square with a side length of {1}?'.format(i, sideLength1))
                solution=str('{0}). {1}'.format(i, sideLength1**2))
            elif shapeType =="rectangle":
                sideLength1 = random.randint(1,10)
                sideLength2 = random.randint(1,10)
                while sideLength2 == sideLength1:
                    sideLength2 = random.randint(1,10)
                problem=str('{0}). What is the area of a rectangle with side lengths of {1} and {2}?'.format(i, sideLength1, sideLength2))
                solution=str('{0}). {1}'.format(i, sideLength1*sideLength2))
            else:
                base = random.randint(1,10)
                height = random.randint(1,10)
                problem=str('{0}). What is the area of a triangle with a base of {1} and a height of {2}?'.format(i, base, height))
                solution=str('{0}). {1}'.format(i, int(base*height/2)))
        elif problemType == "perimeter":
            shapeType = random.choice(["square", "rectangle", "triangle"])
            if shapeType == "square":
                sideLength1 = random.randint(1,10)
                problem=str('{0}). What is the perimeter of a square with sidelength of {1}?'.format(i, sideLength1))
                solution=str('{0}). {1}'.format(i, sideLength1*4))
            elif shapeType =="rectangle":
                sideLength1 = random.randint(1,10)
                sideLength2 = random.randint(1,10)
                while sideLength2 == sideLength1:
                    sideLength2 = random.randint(1,10)
                problem=str('{0}). What is the perimeter of a rectangle with side lengths of {1} and {2}?'.format(i, sideLength1, sideLength2))
                solution=str('{0}). {1}'.format(i, sideLength1*2 + sideLength2 * 2))
            else:
                sideLength1 = random.randint(1,10)
                sideLength2 = random.randint(1,10)
                sideLength3 = random.randint(1,10)
                problem=str('{0}). What is the perimeter of a triangle with side lengths of {1}, {2}, and {3}?'.format(i, sideLength1, sideLength2, sideLength3))
                solution=str('{0}). {1}'.format(i, sideLength1+sideLength2+sideLength3))
        problems.append(problem)
        solutions.append(solution)
    return problems,solutions

def Time(amt):
    problems=[]
    solutions=[]
    used = []
    for i in range(1 , amt + 1):
        num1=random.randint(1,15)
        prob=random.choice(['minutes', 'days', 'hours'])
        if [num1, prob] in used:
            num1=random.randint(1,15)
            prob=random.choice(['minutes', 'days', 'hours'])
        used.append([num1, prob])
        if prob=='minutes':
            num=num1*60
            unit='seconds'
        if prob=='days':
            num=num1*24
            unit='hours'
        if prob=='hours':
            num=num1*60
            unit='minutes'
        if (i<26):
            problem=str('{0}). How many {1} is {2} {3}?'.format(i, unit, num1, prob))
            solution=str('{0}). {1} {2}'.format(i, num, unit))
        else:
            person=random.choice(people)
            action=random.choice(actions)
            problem=str('{0}). {1} {2} for {3} {4}. How many {5} did they {2}?'.format(i, person, action, num1, prob, unit))
            solution=str('{0}). {1} {2} for {3} {4}.'.format(i, person, action, num, unit))
        problems.append(problem)
        solutions.append(solution)
    return problems,solutions