from gurobipy import *

try:

    # Create my model
    m = Model('hw1p3a')

    # Create my variables
    s = m.addVars(6, vtype= GRB.CONTINUOUS, name=['B','F','E','P','D','L'])

    #Define duration data
    d = [3,2,3,4,1,2]
    # Set an objective function
    m.setObjective(s[4]+d[4], GRB.MINIMIZE)

    # Add regular constraints
    m.addConstr(s[4] >= s[2]+d[2])
    m.addConstr(s[4] >= s[3]+d[3])
    m.addConstr(s[2] >= s[1]+d[1])
    m.addConstr(s[3] >= s[1]+d[1])
    m.addConstr(s[1] >= s[0]+d[0])
    m.addConstr(s[5] >= s[0]+d[0])

    # Add non-negativity constraints
    m.addConstrs((s[i] >= 0 for i in range(6)))

    # Optimize model
    m.optimize()

    for v in m.getVars():
        print('%s %g' % (v.varName, v.x))

    print('Obj: %g' % m.objVal)

except GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')