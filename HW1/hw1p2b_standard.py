from gurobipy import *

try:

    # Create my model
    m = Model('hw1a1b_standard')

    # Create my variables
    x = m.addVars(2, vtype= GRB.CONTINUOUS,  name=['x1','x2'],lb = 0.0)
    s = m.addVars(1, vtype= GRB.CONTINUOUS, name=['s'],lb = 0.0)

    # Set an objective function
    m.setObjective(x[0]+x[1], GRB.MINIMIZE)

    # Add regular constraints
    m.addConstr(-x[0]+x[1]+s[0] == 4)
    m.addConstr(-2*x[0]+5*x[1] == 30)

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