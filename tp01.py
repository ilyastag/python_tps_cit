firstname=""
lastname=""
age=0

# use print,input
# cast value from String to int
# use try except to treat issu
# use while
# use function and list

def work():
    firstname=input("Enter your first name: ")
    lastname=input("Enter your last name: ")
    flag=True
    # "12hh3"
    while flag==True:
        try:
            age=int(input("Enter your age: "))
            flag=False
        except ValueError as v:
            print("Valeur n'est pas valide")  
            print(v)  

    if age>= 17 :
        print("Tu es grand")
    else:
        print("Tu es encore petit")


# use dictionary for Map One Value to Another
def work2():
    firstname=input("Enter your first name: ")
    lastname=input("Enter your last name: ")
    flag=True
    # "12hh3"
    while flag==True:
        try:
            age=int(input("Enter your age: "))
            flag=False
        except ValueError as v:
            print("Valeur n'est pas valide")  
            print(v)  
    #return [firstname,lastname,age]
    #return {'fname':firstname,'lname':lastname,'age':age}
    

def work3():
    firstname=input("Enter your first name: ")
    lastname=input("Enter your last name: ")
    flag=True
    # "12hh3"
    while flag==True:
        try:
            age=int(input("Enter your age: "))
            flag=False
        except ValueError as v:
            print("Valeur n'est pas valide")  
            print(v)  
    return {"fname":firstname,"lname":lastname,"age":age}

