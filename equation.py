
def alphaDepth(LHS, RHS, result):
    for n in range(len(RHS)):
        if RHS[n].isalpha():
            if RHS[n] == LHS:
                print('infinite loop')
                return 'error'

            elif LHS not in eqDict:
                print('Variable not found')
                return 'error'

            elif RHS[n] in pruner:
                result += pruner[RHS[n]]

            else:
                result += alphaDepth(RHS[n], eqDict[RHS[n]], 0)

        else:
            result += int(RHS[n])

    pruner[LHS] = result
    return result

testEq = ['offset = 4 + random + 1', 'location = 1 + origin + offset', 
          'origin = 3         + 5', 'random = 2']

eqDict = {}

# Breaking down the strings into something machine readable
for n in range(len(testEq)):
    # eqDict[LHS] = RHS
    LHS = testEq[n].split(' =')[0]
    RHS = testEq[n].split(' =')[1]
    RHS = RHS.replace('+', ' ')
    RHS = RHS.split()
    eqDict[LHS] = RHS


# Depth First Search Approach
eqStack, ans, pruner = sorted(list(eqDict.keys())), [], {}

while(eqStack):
    eqAns = alphaDepth(eqStack[0], eqDict[eqStack[0]], 0)
    if eqAns == 'error':
        print('equation name encountered')
        break
    else:
        ans.append(eqStack[0] + ' = ' + str(eqAns))

    eqStack.pop(0)

print(ans)