#after observing list you sadly can't really make use of it in this scenario as anyway you try to use it seems to just leads to it considering the whole thing as a zero
#actually thats why we have for loops
list = []
def create(name,number,mail):
        item = name,number,mail
        for x in item:
                list.append(x)
        print(list[0])

create("alamin",123,"juiz@mail")

def add(name,number,mail):
        if list[0] == name:
                print("This name has already been added")
        else:
                item = name,number,mail
                for x in item:
                        list.append(x)
        print(f"{name} has been added")
        print(list)

add("fatima", 234567,"muiz@mail")

add("test",123,"gmail")
    
def find(name):
        z = -1
        for i in list:
                z +=1
                if name == i:
                        print("it has been found")
                        print(f"{list[z]}, {list[z+1]}, {list[z+2]}")
                        break
                elif name != i:
                        pass 
                else:
                        print("You inputed wrong")      



def update(name):
        z = -1
        for i in list:
                z+=1
                if name == i:
                        list[z+1] = int(input("Number: "))
                        list[z+2] = input("email: ")
                        print(list)
                        break
                else:
                        print("Contact name not found")

#update("alamin")

def delete(name):
        z = -1
        for i in list:
                z+=1
                if name == i:
                        list.pop(z)
                        list.pop(z+1)
                        list.pop(z-0)
                else:
                        pass
        print(list)


#bitch done haah uh ah hu huyeah