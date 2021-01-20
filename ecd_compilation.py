import math

a = {}
with open('conf-1.cd.bil.txt','r') as f:
    line = f.readlines()
    for i in line:
        readline = i.split()
        a[readline[0]] = readline[1]

b = {}
for i in a:
    b[1239.85/float(i)] = a[i]

def gauss(w, wi, FWHM = 0.3):
    c = float(FWHM/1.3862943611199)
    power = float(-math.pow((w-wi)/c, 2) * 0.5)
    g = float(math.pow(math.e, power) * 0.39894228040143/c)
    return g

print(gauss(6.9,7))
print(gauss(7.1,7))
print(gauss(6.8,7))
print(gauss(7.2,7))