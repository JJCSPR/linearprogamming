from gurobipy import *

try:

    # Create my model
    m = Model('hw1p1a_regular')

    # Create my variables
    x = m.addVars(2, vtype= GRB.CONTINUOUS, name=['x1','x2'])

    # Set an objective function
    m.setObjective(x[0]+2*x[1], GRB.MINIMIZE)

    # Add regular constraints
    m.addConstr(x[0]+x[1] >= 10)
    m.addConstr(2*x[0]+5*x[1] <= 40)

    # Add non-negativity constraints
    m.addConstrs((x[i] >= 0 for i in range(2)))

    # Optimize model
    m.optimize()

    for v in m.getVars():
        print('%s %g' % (v.varName, v.x))

    print('Obj: %g' % m.objVal)

except GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')