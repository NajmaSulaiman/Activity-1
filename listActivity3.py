counter = []
x = [1, 2, 3, 4, 5, 6]

def main():
    count_inputs(counter)
    print_counters(counter, x)

def count_inputs(counter):
    user_input = input("Enter numbers (1-6) separated by spaces and press Enter to finish: ")
    numbers = user_input.split()
    for n in numbers:
        if n:
            counter.append(int(n))
        else:
            break

def print_counters(counter, x):
    for i in x:
        print(i, " : ", counter.count(i))

main()