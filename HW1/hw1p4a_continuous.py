from gurobipy import *
import numpy as np
import csv

with open('problem_4_data.csv', mode='w') as problem_4_data:
    p4_writer = csv.writer(problem_4_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    p4_writer.writerow(["Rows", "Columns", "Avg Obj Val", "Avg RT", "Iterations"])
    #Define Proportions


    # m=[10,20,50,100,500,1000,10000]
    # n=[10,20,50,100,1000,10000]
    """
    m == 10000 and n == 10000 were not used due to time constraints
    """
    m=[10,20,50,100,500,1000]
    n=[10,20,50,100,1000]

    for r in m:
        for c in n:

            outDict = {}

            for i in range(10):
                i += 1

                # Create A
                A = np.random.rand(r,c)*1000
                # Create b
                b = np.random.randint(0,1000,r)
                # Create cost function
                cost = np.random.randint(0,1000,c)
                # Create dictionary for output

                try:

                    # Create my model
                    m = Model('hw1p4a')
                    m.setParam('TimeLimit',120, 0) # Sets time limit to 2 minutes
                    m.setParam('OutputFlag', 0) # Mutes output
                    
                    # Create my variables
                    x = m.addVars(c, vtype= GRB.CONTINUOUS)
                    
                    # Create objective function expression
                    expression = quicksum(np.transpose(cost)[j]*x[j] for j in range(c))

                    #Set objective function
                    m.setObjective(expression, GRB.MINIMIZE)

                    # Add regular constraints
                    m.addConstrs(
                        (quicksum(A[i,j] * x[j] for j in range(c))
                            >= b[i]
                        for i in range(r)))

                    # Optimize model
                    m.optimize()

                    # Append results to output dictionary
                    outDict[i] = (m.objVal, m.runTime)

                except GurobiError as e:
                    print('Error code ' + str(e.errno) + ": " + str(e))

                except AttributeError:
                    print('Encountered an attribute error')

            average_objVal = float(sum(v[0] for v in outDict.values()))/float(len(outDict))
            average_runTime = float(sum(v[1] for v in outDict.values()))/float(len(outDict))
            print(
                    "Rows: " + str(r) + 
                    ", Cols: " + str(c) +
                    ", Avg Obj: " + str(average_objVal) +
                    ", Average RT: " + str(average_runTime) +
                    ", Iterations: " + str(10) + "\n"
                    )
            p4_writer.writerow([str(r), str(c), str(average_objVal), str(average_runTime), str(10)])
