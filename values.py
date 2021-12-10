def Values():
    y = []
    t = []
    a = []
    with open('data.dat') as f:
        for line in f:
            a.append(float(line.strip()))
        i = 0
        while i < len(a):
            if (i % 2) == 0:
                t.append(a[i])
            else:
                y.append(a[i])
            i = i + 1
        return [t, y]
        

'''
Test area
Values()
'''

