import tp01


# use for with range
# use list methods: append, count, reverse and so on
eleves=[]

n=2
for i in range(0,n):
    e=tp01.work3()
    eleves.append(e)

#print(eleves[1]['fname'])
# Hi Mr Nom Prénom, you are Age years old.
v=eleves[1]
print("Hi, Mr",v['lname'],v['fname'],"you are",v['age'],"years old.")

print(f"Hi Mr {v['lname']} {v['fname']}, you are {v['age']} years old.")


