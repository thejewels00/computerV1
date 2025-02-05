import sys
import re

coefficient = {'a': 0, 'b': 0, 'c': 0}
deg = 0
def extract_coefficient(eq, sign):
    global coefficient
    global deg
    
    terms = re.findall(r'([+-]?\s*\d*\.?\d+)\s*\*\s*X\^(\d+)', eq)
    for term in terms:
        value, power = term
        value = float(value.replace(" ", ""))
        power = int(power)
        if power > deg:
            deg = power
        
        if power == 0:
            coefficient['c'] += sign * value
        elif power == 1:
            coefficient['b'] += sign * value
        elif power == 2:
            coefficient['a'] += sign * value
        else:
            print("The polynomial degree is strictly greater than 2, I can't solve.")
            sys.exit(1)

        



def format_number(value):
    if value.is_integer():
        return str(int(value))
    else:
        return str(value)
    
def operation_printing(value):
    if value >= 0:
        print("+ ", end="")

def parsing(equation):
    global coefficient

    eq = equation.split("=")
    if len(eq) != 2:
        print("Error: Invalid equation")
        sys.exit(1)

    extract_coefficient(eq[0], 1)
    extract_coefficient(eq[1], -1)


def printing_equation():
    global coefficient

    print("Reduced form: ", end="")
    if coefficient['a'] != 0:

        print(f"{coefficient['a']} * X^2 ", end="")
    if coefficient['b'] != 0:
        if coefficient['a'] != 0:
            operation_printing(coefficient['b'])

        print(f"{coefficient['b']} * X ", end="")
    if coefficient['c'] != 0:
        if coefficient['a'] != 0 or coefficient['b'] != 0:
            operation_printing(coefficient['c'])
        print(f"{coefficient['c']} = 0")
    else:
        print("= 0")


    print("Polynomial degree: ", deg)


def making_solution():
    global coefficient
    global deg

    if deg == 0:
        if coefficient['c'] == 0:
            print("All real numbers are solution")
        else:
            print("No solution")
    elif deg == 1:
            print(f"The solution is: - {coefficient['c']}  / {coefficient['b']} ")
            print(f"{format_number(-coefficient['c'] / coefficient['b'])}")
    else:
        print("let's solve the equation we need to calculate Delta = b^2 - 4ac : ")
        delta = coefficient['b'] ** 2 - 4 * coefficient['a'] * coefficient['c']
        if delta > 0:
            print("Discriminant (delta) is strictly positive, the two solutions are: ")
            print(f"{format_number((-coefficient['b'] - delta ** 0.5) / (2 * coefficient['a']))}")
            print(f"{format_number((-coefficient['b'] + delta ** 0.5) / (2 * coefficient['a']))}")
        elif delta == 0:
            print("Discriminant (delta) is equal to zero, the solution is: ")
            print(f"{format_number(-coefficient['b'] / (2 * coefficient['a']))}")
        else:
            print("Discriminant (delta) is strictly negative, the two solutions but in Complex numbers :( ")
            # print(f"{format_number(-coefficient['b'] / (2 * coefficient['a']))} - i * {format_number(abs(delta) ** 0.5 / (2 * coefficient['a']))}")
            # print(f"{format_number(-coefficient['b'] / (2 * coefficient['a']))} + i * {format_number(abs(delta) ** 0.5 / (2 * coefficient['a']))}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments")
        sys.exit(1)
    equation = sys.argv[1]
    parsing(equation)
    print(coefficient)
    printing_equation()
    making_solution()

    
