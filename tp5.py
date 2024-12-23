import functools

""" v = lambda x,y,z: x*2 - y*3 + z*5

print(v(3,2,0))


lista=[(2,3,9),(2,3,9),(2,3,9),(2,3,9),(2,3,9)]

g=map(lambda x:x[0]+x[1]+x[2],lista)
print(list(g)) """


#lista=[12,2,7,-12,77,12,0,-33]
lista=[2*x+1 for x in range(31)] 
print(lista)


""" g=filter(lambda x: -3<x[0]<18 ,lista)
print(list(g)) """

d= functools.reduce(lambda x,y: x-y,lista)
print(d)

