import sys
import NonlinearEquationMethods as nonlinearEq
# import NonlinearSystemsMethods as nonlinearSys
from sympy import pprint
from sympy import sympify

bisectionName = []
with open("./namesBisection.txt","r") as txt:
    for line in txt: bisectionName.append(line.rstrip())

linearIterationsName = []
with open("./namesLinearIterations.txt","r") as txt:
    for line in txt: linearIterationsName.append(line.rstrip())

newtonsName = []
with open("./namesNewtons.txt","r") as txt:
    for line in txt: newtonsName.append(line.rstrip())

secantName = []
with open("./namesSecant.txt","r") as txt:
    for line in txt: secantName.append(line.rstrip())

regulaFalsiName = []
with open("./namesRegulaFalsi.txt","r") as txt:
    for line in txt: regulaFalsiName.append(line.rstrip())

# nonlinearEqName = ["1", "equation", "single equation", "non-linear equation", "nonlinear equations", "equação não-linear", "equação", "equação não linear"]
# nonlinearSysName = ["2", "non-linear system", "nonlinear system", "sistema não-linear", "sistema de equações não-lineares", "sistema de equações não lineares", "sistema não linear", "non-linear system of equations", "nonlinear system of equations"]

no = ["no", "não", "n", "false", "falso", "negative", "negativo", "denied", "nein",""]
yes = ["yes", "y", "sim", "ja", "ya", "si", "positivo", "true", "verdadeiro"]
exitNames = ["exit", "exit()", "0", "close", "leave"]

# while True:
#     print("\nThe avaliable types for numerical analysis are:")
#     print("1. Non-Linear Equation")
#     print("2. Non-Linear System of Equations\n")

#     slctdType = input("Select the desired type: ").lower
#     while True:
#         if nonlinearEqName.count(slctdType) > 0:
#             slctdType = "nonlinear equation"
#             break
#         elif nonlinearSysName.count(slctdType) > 0:
#             slctdType = "nonlinear sys"
#             break
#         else: slctdType = input("Invalid input, try again. Select the desired type: ").lower()

while True:
    print("\nThe avaliable methods for non-linear equation's analysis are:")
    print("1. Bisection Method")
    print("2. Linear Iterations Method")
    print("3. Newton's Method")
    print("4. Secant Method")
    print("5. Regula Falsi Method\n")

    method = input("Select the desired method: ").lower()
    while True:
        if bisectionName.count(method) > 0:
            method = "bisection"
            break
        elif linearIterationsName.count(method) > 0:
            method = "linear iterations"
            break
        elif newtonsName.count(method) > 0:
            method = "newton's"
            break
        elif secantName.count(method) > 0:
            method = "secant"
            break
        elif regulaFalsiName.count(method) > 0:
            method = "regula falsi"
            break
        elif exitNames.count(method) > 0:
            print()
            sys.exit()
        else: method = input("Invalid input, try again. Select the desired method: ").lower()

    print("\n::: " + method.capitalize() + " method selected.")

    if method != "linear iterations":
        fun = input("\nEnter function f(x) = ")
        while True:
            try: fun = sympify(fun)
            except: fun = input("Invalid input, try again. Enter function f(x) = ")
            else: 
                print("\n::: f(x) = ")
                pprint(fun)
                break
    else:
        fun = input("\nEnter function psi(x) = ")
        while True:
            try: fun = sympify(fun)
            except: fun = input("Invalid input, try again. Enter function psi(x) = ")
            else: 
                print("\n::: psi(x) = ")
                pprint(fun)
                break

        confirmConv = input("\nConfirm that the result converge for this psi(x)? ")
        while True:
            if yes.count(confirmConv):
                confirmConv = True
                break
            elif no.count(confirmConv):
                confirmConv = False
                break
            else: confirmConv = input("Invalid input, try again. Confirm that the result converge for this psi(x)? ")

    if method == "bisection" or (method == "linear iterations" and confirmConv):
        print("\nConsidering the interval [a,b], enter:")
        a = input("a = ")
        while True:
            try: a = float(a)
            except: a = input("Invalid input, try again. a = ")
            else: break
        b = input("b = ")
        while True:
            try: b = float(b)
            except: b = input("Invalid input, try again. b = ")
            else: 
                print("\n::: Interval [%.3f, %.3f]." % (a, b))
                break

    if method != "bisection":
        x_0 = input("\nEnter x_0 = ")
        while True:
            try: x_0 = float(x_0)
            except: x_0 = input("Invalid input, try again. x_0 = ")
            else: break

        if method == "secant" or method == "regula falsi":
            x_1 = input("\nEnter x_1 = ")
            while True:
                try: x_1 = float(x_1)
                except: x_1 = input("Invalid input, try again. x_1 = ")
                else: 
                    print("\n::: x_0 = %f ; x_1 = %f." % (x_0, x_1))
                    break

        else: print("\n::: x_0 = %f." % x_0)

    error = input("\nEnter the desired error margin: ")
    while True:
        if no.count(error) > 0: 
            error = False
            break
        else:
            try: error = float(sympify(error))
            except: error = input("Invalid input, try again. Enter the desired error margin: ")
            else:
                if error >= 1 or error == 0: error = input("Invalid input, the error margin must be less than 1. Try again: ")
                else: break

    maxIterations = input("\nEnter the maximum number of iterations desired: ")
    while True:
        if no.count(maxIterations) > 0: 
            maxIterations = False
            break
        try: maxIterations = int(sympify(maxIterations))
        except: maxIterations = input("Invalid input, try again. Enter the maximum number of iterations: ")
        else:
            if maxIterations < 1: maxIterations = input("Invalid input, there must be at least 1 iterations. Try again: ")
            else: break

    showLog = input("\nDisplay console log for all values? ")
    while True:
        if yes.count(showLog):
            showLog = True
            showTotalNo = True
            break
        elif no.count(showLog):
            showLog = False

            showTotalNo = input("\nDisplay total number of iterations? ")
            while True:
                if yes.count(showTotalNo):
                    showTotalNo = True
                    break
                elif no.count(showTotalNo):
                    showTotalNo = False
                    break
                else: showTotalNo = input("Invalid input, try again. Display total number of iterations? ")

            break
        else: showLog = input("Invalid input, try again. Display console log for all values? ")

    print("\n")

    if method == "bisection":
        if error and maxIterations: root, precision = nonlinearEq.bisection(fun,a,b,error,maxIterations,displayConsoleLog=showLog,printTotalIterations=showTotalNo)
        elif error: root, precision = nonlinearEq.bisection(fun,a,b,error,displayConsoleLog=showLog,printTotalIterations=showTotalNo)
        elif maxIterations: root, precision = nonlinearEq.bisection(fun,a,b,MAXITER=maxIterations,displayConsoleLog=showLog,printTotalIterations=showTotalNo)
        else: root, precision = nonlinearEq.bisection(fun,a,b,displayConsoleLog=showLog,printTotalIterations=showTotalNo)

    elif method == "linear iterations":
        if confirmConv:
            if error and maxIterations: root, precision = nonlinearEq.linearIterations(fun,x_0,error,maxIterations,confirmConv,a,b,showLog,showTotalNo)
            elif error: root, precision = nonlinearEq.linearIterations(fun,x_0,error,confirmConvergence=confirmConv,infLim=a,supLim=b,displayConsoleLog=showLog,printTotalIterations=showTotalNo)
            elif maxIterations: root, precision = nonlinearEq.linearIterations(fun,x_0,MAXITER=maxIterations,confirmConvergence=confirmConv,infLim=a,supLim=b,displayConsoleLog=showLog,printTotalIterations=showTotalNo)
            else: root, precision = nonlinearEq.linearIterations(fun,x_0,confirmConvergence=confirmConv,infLim=a,supLim=b,displayConsoleLog=showLog,printTotalIterations=showTotalNo)
        else:
            if error and maxIterations: root, precision = nonlinearEq.linearIterations(fun,x_0,error,maxIterations,confirmConv,displayConsoleLog=showLog,printTotalIterations=showTotalNo)
            elif error: root, precision = nonlinearEq.linearIterations(fun,x_0,error,confirmConvergence=confirmConv,displayConsoleLog=showLog,printTotalIterations=showTotalNo)
            elif maxIterations: root, precision = nonlinearEq.linearIterations(fun,x_0,MAXITER=maxIterations,confirmConvergence=confirmConv,displayConsoleLog=showLog,printTotalIterations=showTotalNo)
            else: root, precision = nonlinearEq.linearIterations(fun,x_0,confirmConvergence=confirmConv,displayConsoleLog=showLog,printTotalIterations=showTotalNo)

    elif method == "newton's":
        if error and maxIterations: root, precision = nonlinearEq.newtons(fun,x_0,error,maxIterations,displayConsoleLog=showLog,printTotalIterations=showTotalNo)
        elif error: root, precision = nonlinearEq.newtons(fun,x_0,error,displayConsoleLog=showLog,printTotalIterations=showTotalNo)
        elif maxIterations: root, precision = nonlinearEq.newtons(fun,x_0,MAXITER=maxIterations,displayConsoleLog=showLog,printTotalIterations=showTotalNo)
        else: root, precision = nonlinearEq.newtons(fun,x_0,displayConsoleLog=showLog,printTotalIterations=showTotalNo)

    elif method == "secant":
        if error and maxIterations: root, precision = nonlinearEq.secant(fun,x_0,x_1,error,MAXITER=maxIterations,displayConsoleLog=showLog,printTotalIterations=showTotalNo)
        elif error: root, precision = nonlinearEq.secant(fun,x_0,x_1,error,displayConsoleLog=showLog,printTotalIterations=showTotalNo)
        elif maxIterations: root, precision = nonlinearEq.secant(fun,x_0,x_1,MAXITER=maxIterations,displayConsoleLog=showLog,printTotalIterations=showTotalNo)
        else: root, precision = nonlinearEq.secant(fun,x_0,x_1,displayConsoleLog=showLog,printTotalIterations=showTotalNo)

    elif method == "regula falsi":
        if error and maxIterations: root, precision = nonlinearEq.regulaFalsi(fun,x_0,x_1,error,MAXITER=maxIterations,displayConsoleLog=showLog,printTotalIterations=showTotalNo)
        elif error: root, precision = nonlinearEq.regulaFalsi(fun,x_0,x_1,error,displayConsoleLog=showLog,printTotalIterations=showTotalNo)
        elif maxIterations: root, precision = nonlinearEq.regulaFalsi(fun,x_0,x_1,MAXITER=maxIterations,displayConsoleLog=showLog,printTotalIterations=showTotalNo)
        else: root, precision = nonlinearEq.regulaFalsi(fun,x_0,x_1,displayConsoleLog=showLog,printTotalIterations=showTotalNo)

    print("ROOT:")
    print(f"x = {root:.{precision}f}")
    print("\n___________________________________________________________________________\n")