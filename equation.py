
testEq = ['offset = 4 + random + 1', 'location = 1 + origin + offset', 
          'origin = 3         + 5', 'random = 2']

eqDict = {}

while (testEq):
    LHS = testEq[0].split(' =')[0]
    RHS = testEq[0].split(' =')[1]
    RHS = RHS.replace('+', ' ')
    RHS = RHS.split()
    eqDict[LHS] = RHS
    print(eqDict)
    testEq.remove(testEq[0])

'''
for m in range(len(sumEq)):
    if sumEq[m].isalpha():
        print(sumEq[m])
    else:
        sumEq[m] = int(sumEq[m])

    print(sumEq)
'''
print(eqDict)
