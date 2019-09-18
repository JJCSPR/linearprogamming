from gurobipy import *

try:

    # Create my model
    m = Model('hw1a1b_regular')

    # Create my variables
    x1 = m.addVar(name="x1",lb = -GRB.INFINITY, ub = 0.0)
    x2 = m.addVar(name="x2",lb = 0.0)

    # Set an objective function
    m.setObjective(x1-x2, GRB.MAXIMIZE)

    # Add regular constraints
    m.addConstr(x1+x2 <= 4)
    m.addConstr(2*x1+5*x2 == 30)

    # Optimize model
    m.optimize()

    print(' worked')
    for v in m.getVars():
        print('%s %g' % (v.varName, v.x))

    print('Obj: %g' % m.objVal)

except GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')