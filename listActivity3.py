counter = []
x = [1, 2, 3, 4, 5, 6]

def main():
    
    countInputs(counter)
    printCounters(counter, x)

def countInputs(counter):
    while True:
        n = input("enter a number (1-6) or Q=for stop: ")
        if n != "Q":
            counter.append(int(n))
        else:
            break
    

def printCounters(counter, x):
    for i in x:
        #print("{}: {}".format(i, counter.count(i)))
        print(i," : " ,counter.count(i))
        
        


main()

