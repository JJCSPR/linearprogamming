from gurobipy import *

try:

    # Create my model
    m = Model('hw1p5a')

    # Create my variables
    q = m.addVars(2, vtype= GRB.CONTINUOUS, name=['qa','qb'])

    # Set an objective function
    m.setObjective(30*q[0]+45*q[1], GRB.MAXIMIZE)

    # Add regular constraints
    m.addConstr(72*q[0] + 120*q[1] <= 60000)
    m.addConstr(1.2*q[0] + 1.4 * q[1] <= 800)

    # Add non-negativity constraints
    m.addConstrs((q[i] >= 0 for i in range(2)))

    # Optimize model
    m.optimize()

    for v in m.getVars():
        print('%s %g' % (v.varName, v.x))

    print('Obj: %g' % m.objVal)

except GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')