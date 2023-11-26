dic={1:"A", 2:"B"}
print(dic.values())
print("the dictionary: ",dic)
#print(dic.get(2,"x"))
#defult if we dont have it in the dictonary
print("defult value: ",dic.get(3,"x"))

#print key
for key in dic:
    print("list of key :",key)
    
#remove
dic.pop(1)
print("dictionary after pop: ",dic)



dic2={1:{"name": "Ali", "age": 23},
      2:{"name": "sara", "age": 24}}
print("dictionary 2: ",dic2)
#to print the name
print("print just the name:")
for key in dic2:
    print(dic2[key]["name"],end=" ")
print()    
#to print the values   
print("print all the values: ")    
for key in dic2:
    for key1 in dic2[key]:
        print(dic2[key][key1],end=" ")
print()          
dec={1:{"name":"john", "age":27, "gender" :"male"},
     2:{"name":"maria", "age":22, "gender" :"female"},
     3:{"name":"sali", "age":23, "gender" :"female"}}
   
for key in dec:
    if (dec[key]["age"] > 22):
        print("name above 22 is :" ,dec[key]["name"])
        

    
    

