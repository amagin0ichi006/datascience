dictionary = {}

def create(name, quantity, price):
    print("Creating inventory.....")  
    price *= quantity
    dic = {
        "name": name,
        "quantity": quantity,
        "price": price
    }
    dictionary[name] = dic
    print(dictionary)


def add(name,quantity):
    print("Adding to the inventory....")
    dictionary.get(name)['name'] == name
    dictionary.get(name)["quantity"]+= quantity
    price = quantity * dictionary.get(name)["price"]
    dictionary.get(name)["price"] += price
    print(dictionary)
    

        

def find(name):
    find = dictionary.get(name)
    print(find)

    
def update(name):
    if dictionary.get(name)['name'] == name:
        print("Updating...")
        dictionary.get(name)["name"] = input("add a name ")
        dictionary.get(name)["quantity"]= int(input("Add a number "))
        dictionary.get(name)["price"] = int(input("Update price.. "))
        print(dictionary)
    else:
        print("FAILED")
    
def delete(name):
    if dictionary.get(name)['name'] == name:
        del dictionary[name]
        print(dictionary)
    else:
        print("Failed")

def yeild():
    #return total stock
    print(dictionary)

def remove(name,quantity,price):
    dictionary.get(name)["name"] == name
    dictionary.get(name)["quantity"] -= quantity
    price = quantity * price#we need its original price
    dictionary.get(name)["price"] -= price
    print(dictionary)






create("apple", 1,2)
create("banana",1,9)
add("apple",2)
remove("apple",2,2)
