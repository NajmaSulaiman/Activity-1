
def shape1(x):
    b=int(input("enter number height : "))
    h=int(input("enter number width : "))
    
    traiangle=(b*h)/2
    return traiangle


def shape2(z):
    b=int(input("enter number height : "))
    h=int(input("enter number width : "))
    sqrr=b*h
    return sqrr


def shape3(y):
    n=int(input("enter number radius : "))
    cirle=(22/7)*(n**2)
    return cirle

def shape4(w):
    n=int(input("enter number radius : "))
    h=int(input("enter number height : "))
    cylinder=(2*(22/7)*(n**2))+(2*(22/7)*n*h)
    return cylinder


choose=0
while (choose==choose):
    choose=int(input("enter 1,2,3,4,Q(for quiting): "))
    if(choose==1):
        result =shape1(choose)
        print("the Area of triangle: "+str(result))
    elif(choose==2):
        result =shape2(choose)
        print("the Area of Square: "+str(result))
    elif(choose==3):
        result =shape3(choose)
        print("the Area of cirle:  "+str(result))
    elif(choose==4):
        result =shape4(choose)
        print("the Area of cylinder: "+str(result))
    else:
        print("exit")
        
        
    