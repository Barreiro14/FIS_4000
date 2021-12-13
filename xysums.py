from values import Values

def xValues(n):
    Values()
    x = 0
    for element in Values()[0]:
        x = x + element**n
    return x

def xyValues(n):
    Values()
    xy = 0
    i = 0
    while i < len(Values()[1]):
        xy = xy + Values()[1][i]*(Values()[0][i]**n)
        #print("t es: ", Values[0][i])
        #print("y es: ", Values[1][i])
        #print("ty es: ", )
        i = i + 1

    return xy

'''
Test area
xyValues(1)
'''    
