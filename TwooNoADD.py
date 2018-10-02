def increment(number):
   
    
    return number + 1


def add(num1, num2):
  
    #Approach : Using increment()

    if num2 == 0:
        return num1
    else:
        return add(increment(num1), num2 - 1)
        

def main():
    

    number1 = int(input("Enter first number : "))
    
    number2 = int(input("Enter second number : "))
    
    print("Sum : ",add(number1,number2))

if __name__ == "__main__":
    main()