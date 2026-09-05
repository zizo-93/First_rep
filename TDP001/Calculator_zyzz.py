
print('\n Welcome to the calculator!')

operators = ['+', '-', '/', '*']
numbers = [range(0-10)]

def get_digit(num_1, num_2):  

    while True:
        try:
            num_1 = int(input('Select a positive single digit number: '))
            num_2 = int(input('Select another positive single digit number: '))
        except ValueError:
            print('invalid input, please fill in the correct input')  
            continue
        break 
    
        
get_digit(num_1, num_2)

def get_operator(operator):
    while True:
        operator = input('Select an operator (+, -, /, *)')
        if operator not in operators:
            print('Please select an correct operator.')
            continue
        break

get_operator()

def calculation(num_1, num_2, operator):
    if operator == '+':
        num_1 + num_2
    elif operator == '-':
        num_1 - num_2
    elif operator == '/':
        num_1 / num_2
    else:
        num_1 * num_2





        

    
            

