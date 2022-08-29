import random
import numpy as np
people=["James", "Sally", "Bob", "Sam", "Rachel", "Michael", "Laura", "Alex"]
objects=["marbles", "pens", "books", "bottles", "toys", "pencils", "dollars", "papers"]



def solveBasicEq(num):
    used=[]
    problems=[]
    solutions=[]

    for i in range(1, num+1):

        problem=str(i) + ") "
        sol=random.randint(1, 9)
        m=random.randint(1, 9)
        n = random.randint(1, 9)
        while([sol, m, n] in used):
            sol = random.randint(1, 9)
            m = random.randint(1, 9)
            n = random.randint(1, 9)
        res=sol
        if (m==1):
            problem+="x"
        else:
            problem+=str(m) + "x"
        res*=m
        op=random.choice([" + ", " - "])

        problem += op + str(n) + " = "

        if (op==" + "):
            res+=n
            x=" getting "
        else:
            res-=n
            x=" losing "
        if (i < 26):
            problem+=str(res)
            solution=str(i) + ") x=" + str(sol)
        else:
            person1=random.choice(people)
            object=random.choice(objects)
            problem=str(i) + ") " + person1 + " had an unknown number of " + object + ". They got " + str(m) + \
                    " times as many " + object + " before" + x + str(n) + " more. In total, they now have " + \
                    str(res) + " " + object + ". How many objects did " + person1 + " start with?"
            solution=str(i) + ") " + person1 + " started with " + str(sol) + " " + object + "."
        problems.append(problem)
        solutions.append(solution)
    return problems, solutions



def facBasic(num):
    problems=[]
    solutions=[]
    used=[]
    for i in range(1, num+1):
        num1 = random.randint(-10, 10)
        num2 = random.randint(-10, 10)

        while (num1 == 0 or [num1, num2] in used or num2==0):
            num1 = random.randint(-10, 10)
            num2 = random.randint(-10, 10)
        x = num1 + num2

        y = num1 * num2
        if (x < 0):
            p1 = "- " + str(abs(x)) + "x "
        else:
            p1 = "+ " + str(x) + "x "
        if (y < 0):
            p2 = "- " + str(abs(y))
        else:
            p2 = "+ " + str(y)

        if (num1 < 0):
            s1 = "(x - " + str(abs(num1)) + ")"
        else:
            s1 = "(x + " + str(num1) + ")"
        if (num2 < 0):
            s2 = "(x - " + str(abs(num2)) + ")"
        else:
            s2 = "(x + " + str(num2) + ")"
        if (x == 0):
            p1 = ""

        problems.append(str(i) + ') Factorize: $x^2$ ' + str(p1) + str(p2))
        solutions.append(str(i) + ') ' + str(s1) + str(s2))

    return problems, solutions

def facAdvanced(num):
    problems=[]
    solutions=[]
    used=[]


    for i in range(1, int(num) + 1):
        num = random.randint(-6, 6)
        n3 = random.randint(-6, 6)
        num1 = random.randint(-10, 10)
        num2 = random.randint(-10, 10)
        while (num1 == 0 or num2==0 or num==0 or n3==0 or [num1, num2, num, n3] in used):
            num = random.randint(-6, 6)
            n3 = random.randint(-6, 6)
            num1 = random.randint(-10, 10)
            num2 = random.randint(-10, 10)

        x = (num1 * n3) + (num * num2)

        y = num1 * num2

        if (x < 0):
            p1 = "- " + str(abs(x)) + "x "
        else:
            p1 = "+ " + str(x) + "x "
        if (y < 0):
            p2 = "- " + str(abs(y))
        else:
            p2 = "+ " + str(y)

        if (num1 < 0):
            s1 = "(" + str(num) + "x- " + str(abs(num1)) + ")"
        else:
            s1 = "(" + str(num) + "x + " + str(num1) + ")"
        if (num2 < 0):
            s2 = "(" + str(n3) + "x - " + str(abs(num2)) + ")"
        else:
            s2 = "(" + str(n3) + "x + " + str(num2) + ")"
        if (x == 0):
            p1 = ""

        problems.append(str(i) + ') Factorize: $' + str(num * n3) + 'x^2$ ' + str(p1) + str(p2))
        solutions.append(str(i) + ') ' + str(s1) + str(s2))
    return problems, solutions

def solvingIneq(num):
    problems=[]
    solutions=[]
    used=[]
    for i in range(1, num+1):
        solution = random.randint(1, 9)

        text = str(i) + ') Solve: '
        mult = random.randint(-9, 9)
        while mult == 0:
            mult = random.randint(-9, 9)
        num1 = random.randint(1, 9)
        op = random.choice(['+', '-'])
        sign = random.choice(['<', '>', '$\leq$', '$\geq$'])

        if op == '+':
            x = mult * solution + num1
        if op == '-':
            x = mult * solution - num1
        text = text + str(mult) + 'x ' + op + ' ' + str(num1) + ' ' + sign + ' ' + str(x)

        if mult < 0 and sign == '<':
            newsign = '>'
        elif mult < 0 and sign == '>':
            newsign = '<'
        elif mult < 0 and sign == '$\leq$':
            newsign = '$\geq$'
        elif mult < 0 and sign == '$\geq$':
            newsign = '$\leq$'
        else:
            newsign = sign
        problems.append(text)
        solutions.append(str(i) + ') x' + newsign + str(solution))
    return problems, solutions

def linearEq(num):
    problems=[]
    solutions=[]
    used=[]
    for i in range(1, num+1):
        num1=random.randint(-10, 10)
        num2=random.randint(-10, 10)
        while (num2==num1 or num1==0):
            num1 = random.randint(-10, 10)
            num2 = random.randint(-10, 10)
        problem=str(i) + ") Find the equation of the line with the points (0, " + str(num2) + "), (" + str(round((-1*(num2/num1)), 2)) + ", 0). Round your slope to the nearest whole number:" + "\n" "\n" + r"\begin{tikzpicture} " + "\n" +r"\begin{axis}[xmin=-10, xmax=10, ymin=-10, ymax=10, axis x line=middle, axis y line=middle]"
        problem+=r"\addplot[domain=-10:10]{" + str(num1)+"*x+" + str(num2) + r"};" + "\n" + r"\addplot[mark=*] coordinates {(0," + str(num2) + ")};"+"\n" +\
                    r"\addplot[mark=*] coordinates {(" + str(round((-1*(num2/num1)),2))+",0)};"+"\n" + "\end{axis}" + "\n" + "\end{tikzpicture}"
        problems.append(problem)
        solutions.append(str(i) + ") y=" + str(num1) + "x + " + str(num2) )
    return problems, solutions



functions = [["Solving Basic Algebraic Equations", solveBasicEq(30), 0, 0], ["Solving Inequalities", solvingIneq(30), 0, 0],
             ["Factoring Basic Quadratic Equations", facBasic(30), 0, 0],
             ["Factoring Advanced Quadratic Equations", facAdvanced(30), 0, 0], ["Finding the Equation of a Line", linearEq(10), 1, 0]]