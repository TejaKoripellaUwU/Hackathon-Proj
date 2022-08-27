import random
from fractions import Fraction
import numpy
import math

def identifyingPlaceValue(probs):
    problems=[]
    solutions=[]
    
    return problems,solutions

# DONE
def roundingNums(probs):
    problems=[]
    solutions=[]
    for prob in range(0,probs):
        placeValues=[10,100,1000]
        thing = random.randint(0,9999)
        if thing >= 1000:
            sheet = random.randint(-3,-1)
        elif thing>=100:
            sheet = random.randint(-2,-1)
        else:
            sheet = -1
        problems.append(str(prob+1)+ ") Round "+str(thing)+" to the nearest "+str(placeValues[abs(sheet)-1]))
        solutions.append(str(prob+1) + ") " + str(round(thing,sheet)))
    return problems,solutions

#DONE
def dividingNums(probs):
    problems=[]
    solutions=[]
    for prob in range(0,probs):
        answer = random.randint(0,4)
        num2 = random.randint(2,20)
        remainder = random.randint(0,num2-1)
        num1 = num2*answer+remainder
        problems.append(str(prob+1)+ ") What is "+str(num1)+" divided by "+str(num2)+" use the remainder in your answer")
        solutions.append(str(prob+1) + ") " + str(answer)+" remainder: "+ str(remainder))
    return problems,solutions


def primeComposite(probs):
    problems=[]
    solutions=[]
    for prob in range(0,probs):
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
            return prime_list,compList

        pOrC = random.randint(0,1)
        if pOrC == 0:
            primes,composites = primesInRange(0,90)
            randprime = primes[random.randint(0,len(primes)-1)]
            primes.remove(primes[random.randint(0,len(primes)-1)])
            problems.append(str(prob+1)+") Is " + str(randprime) + " prime or composite?")
            solutions.append(str(prob+1) + ") prime")
        else:
            primes,composites = primesInRange(0,90)
            randComposite = composites[random.randint(0,len(composites)-1)]
            composites.remove(composites[random.randint(0,len(composites)-1)])
            problems.append(str(prob+1) + ") Is " + str(randComposite) + " prime or composite?") 
            solutions.append(str(prob+1) + ") composite")
    return problems,solutions



def compareFractions(probs):
    problems=[]
    solutions=[]
    used = []
    for prob in range (0, probs):
        operations = [">","<","="]
        operation = 0
        frac1Num = random.randint(1,20)
        frac1Den = random.randint(2,20)
        frac2Num = random.randint(1,20)
        frac2Den = random.randint(2,20)
        frac1 = Fraction(frac1Num,frac1Den)
        frac2 = Fraction(frac2Num, frac2Den)
        while ([frac1,frac2] in used):
            frac1 = Fraction(frac1Num,frac1Den)
            frac2 = Fraction(frac2Num, frac2Den)
        used.append([frac1,frac2])
        if frac1>frac2:
            operation = 0
        elif frac1<frac2:
            operation = 1
        elif frac1==frac2:
            operation = 2
        problems.append(str(prob+1)+") Place one of the following in the black >,<,= " + str(frac1Num) + "/" + str(frac1Den) +"___"+ str(frac2Num)+"/"+ str(frac2Den))
        solutions.append(str(prob+1)+") "+ operations[operation])
    return problems,solutions

def addFrac(probs):
    problems=[]
    solutions=[]
    used = []
    for prob in range(0,probs):
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
        problems.append(str(prob+1)+") add the following fractions: " + str(frac1Num) + "/" + str(frac1Den) + " + " + str(frac2Num) + "/" + str(frac2Den))
        solutions.append(str(prob+1)+") " + str((frac1+frac2).numerator) + "/" + str((frac1+frac2).denominator))
    return problems,solutions

print(addFrac(10))

def multiplyFrac():
    problems=[]
    solutions=[]
    return problems,solutions
def decToFrac():
    problems=[]
    solutions=[]
    return problems,solutions
def Area():
    problems=[]
    solutions=[]
    return problems,solutions
def Time():
    problems=[]
    solutions=[]
    return problems,solutions