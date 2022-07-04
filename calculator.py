def main():
    #write your code here

    n1= input("Enter first number: ")
    n2= input("Enter second number: ")
    operation= input("Choose the operation (+, -, /, *): ")

    if n1.isdigit() and n2.isdigit():
        n1= int(n1)
        n2= int(n2)
        operation= operation
    else:
        print("the numbers were invalid")
        return n1, n2, operation

    if operation == "+":
        sum= n1 + n2
        print(f"The answer is : {sum}")
    elif operation == "-":
        sub= n1 - n2
        print(f"The answer is : {sub}")
    elif operation == "/":
        div= n1 / n2
        print(f"The answer is : {div}")
    elif operation == "*" or operation == "x":
        mul= n1 * n2
        print(f"The answer is : {mul}")
    else: 
        print("operation is not valid")






if __name__ == '__main__':
    main()