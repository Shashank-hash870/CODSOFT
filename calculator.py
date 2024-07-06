# Calculator operations
def add(num1, num2):
    return num1 + num2  

def subtract(num1, num2):
   return num1 - num2

def multiply(num1, num2):
   return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        print("Cannot divide by 0!")
        return None
    return num1 / num2

# Operation functions dict  
operations = {
    1: add,
    2: subtract, 
    3: multiply,
    4: divide 
}

def calculate():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
  
    choice = input_number("Enter choice(1-4): ")

    num1 = input_number("Enter first number: ")
    num2 = input_number("Enter second number: ")

    func = operations.get(choice)
    if func:
        result = func(num1, num2)
        if result is not None:
            print(result) 
    else:
        print("**Invalid operatio**n\n")
        calculate()
   
def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("**Invalid input**\nPlease enter a number")
            continue
               
calculate()