s0 = (0.5, 0)
s1 = (0.3, 1)
s2 = (0.1, 2)
s3 = (0.1, 3)
simpleSimbol = []
codeSimbol= []
listSimbol = [s0, s1, s2 , s3]

def retiraUltimos (lista):
    sum = lista[2] + lista[3]
    return sum

a = retiraUltimos(listSimbol)
print (a)
