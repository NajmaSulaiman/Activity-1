n=input("enter a text")

for i in range (len(n)):
    if("o" in n):
        print(n.replace("o","O"))
    
    elif("a" in n):
        print(n.replace("a","A"))
    elif("u" in n):
        print(n.replace("u","U"))
    elif("i" in n):
        print(n.replace("i","I"))
    elif("e" in n):
        print(n.replace("e","E"))
    
    