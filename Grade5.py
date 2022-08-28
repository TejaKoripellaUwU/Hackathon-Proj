import numbers
import random; 

def MultiplyDecimals(num): 
    problems = []
    solutions = []
    used = []

    for i in range(1, num+1):
        num1 = random.choice(range(float(0,10)))
        num2 = random.choice(range(float(0,10)))
        num2 = round(num2)
        num1 = round(num1)
        problem = str(num1) + "*"  + str(num2)
        solution = num1 * num2 
        used.append([num1, num2])
        problems.append(problem)
        solutions.append(solution)
    return problems, solutions

def Exponents_sqaure(num):
    problems = []
    solutions = []
    used = []
    for i in range(1, num+1):
        num1 = random.randint(1, 20)
        problem = str(num1) + "^2"
        solution = num1 * num1 
        problems.append(problem)
        solutions.append(solution)
        used.append(num1) 
    return problems,numbers

def Exponents_cubed(num):
    problems = [] 
    solutions = [] 
    used = [] 
    for i in range(1, num+1): 
        num1 = random.randint(1, 20)
        problem = str(num1) + "^2"
        solution = num1 * num1 * num1 
        solutions.append(solution)
        problems.append(problem)
        used.append(num1)       

    return problems, solutions

def Exponents_of_ten(num): 
    problems = [] 
    solutions = [] 
    used = [] 
    for i in range(1, num+1):
        num1 = random.randint(1,10)
        problem = "Convert to a number: 10^" + str(num1) 
        solution = num1
        for g in range(1, num1):
            solution = solution * 10
        used.append(num1)
        problems.append(problem)
        solutions.append(solution)

        
def Adding_Positve_Negative(num):
    problems = [] 
    solutions = [] 
    used = [] 

    for i in range(1, num+1):      
        op1 = random.choice(['+', '-'])
        num1 = random.randint(-100, 100)
        num2 = random.randint(-100, 100)

        problem = str(i) + ") " + str(num) + " " + str(op1) + " " + str(num2)
        if (op1 == '+'):
            solution = num1 + num2
        else: 
            solution = num1 - num2
        used.append([num1, num2])
        problems.append(problem)
        solutions.append(solution)  

    return problems, solutions
            
        
def main(): 
    problems, solutions = Adding_Positve_Negative(5)
    for i in problems: 
       print(i)
    for e in solutions: 
        print(e)
main()
