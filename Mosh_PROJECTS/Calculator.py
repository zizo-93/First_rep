#Create funtctions for each operator (addition,divsion,etc..).
#(get an input of two numbers and one operator from the user).
#use flow controll to run the correct function and execute it.
#have an error handaling logic, takes care of divison of 0 etc. 

# def addition():


def inputting():
    def get_valid_digit(prompt):
        while True:
            try:
                val = int(input(prompt))
                if 1 <= val <= 9:  # Change to 0 <= val <= 9 if 0 should be allowed
                    return val
                print("Error: Input must be a positive single digit (1-9).")
            except ValueError:
                print("Error: Input must be a valid integer.")

    number_1 = get_valid_digit('Please input one single digit numbers: ')
    number_2 = get_valid_digit('Please input another single digit numbers: ')
    
    while True:
        operator = input('Please select one operator (+, -, *, /): ')
        if operator in ['+', '-', '*', '/']:
            break
        print("Error: Invalid operator. Please choose from +, -, *, or /.")
        
    return number_1, number_2, operator



def calculating(number_1, number_2, operator):
    if operator == '/':
        print(number_1/number_2)

    elif operator == '*':
        print(number_1 * number_2)
        
    elif operator == '+':
        print(number_1 + number_2)

    else:
        print(number_1 - number_2)

def last_question():
    redo = input('go again or no (y/n)?: ').lower()
    return redo
       



while True:

    number_1, number_2, operator = inputting()

    calculating(number_1, number_2, operator)

    redo = last_question()
    
    if redo == 'y':
        continue 
    else:
        break

