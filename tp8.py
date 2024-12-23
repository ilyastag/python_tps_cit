nombres_pairs=[x for x in range(5,100,3) if x%2==0]


caracteres=[chr(x) for x in range(100) if x%2==0]

code_asscii=[ord(x) for x in " Aabonjour tout le monde"]

def f(x):
    return x**2

nombrescarres=[f(x) for x in range(5,100,3) if x%2==0]
print(nombres_pairs)