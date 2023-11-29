try:
    #x=4/0
    #print(x)
    x=4/2
    a=[1,2,3,4,5,6]
    print(a[12])
    #print(y)

except ZeroDivisionError:
    print("you cant divide by zero")
    
    

   
except Exception as exc:
    print("error:",str(exc))
    
except:
    print("something going wrong")
    
    
finally:
    print("Done")
    
    
    

try:
    
    n=input("enter value: ")
    print(int(n))
    

    
except Exception as exc:
    print("error:",type(exc))
    
except:
    print("something going wrong")
    
    
finally:
    print("Done")

