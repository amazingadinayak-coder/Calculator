int_1 = int(input(print("This is a caluclator. Please enter 1 number:")))
int_2 = int(input(print("Now enter another number:"))) 
symbol = input(print("Finally, input a symbol to operate:"))
if symbol == "+":
    print(int_1 + int_2)
if symbol == "-":
    print(int_1 - int_2)
if symbol == "/":
    print(int_1 / int_2)
if symbol == "*":
    print(int_1 * int_2)
