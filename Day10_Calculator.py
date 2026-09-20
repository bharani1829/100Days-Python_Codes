art ='''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |             Mini Project : Calculator
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''


print(art)

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


def first_operation():
    n1 =  float(input("Enter First Number : "))
    operator = input("Select the required operation \n+\n-\n*\n/\n select one : ")
    n2 = float(input("Enter your Next Number : "))
    return calc_dict[operator](n1,n2)

def second_operation(result):
    n1 = result
    operator = input("Select the required operation \n+\n-\n*\n/\n select one : ")
    n2 = float(input("Enter your Next Number : "))
    return calc_dict[operator](n1,n2)


calc_dict = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide
}


result = first_operation()
print(result)
calc_over = True

while True:
    again = input("If you want to perform operation with previous result (type y) or to start new operation (type n) or to exit (type q)").lower()
    if again == 'y':
        print(second_operation(result))
    elif again == 'n':
       print(first_operation())
    elif again == 'q':
        calc_over = False



