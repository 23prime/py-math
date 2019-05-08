#########################
# Que-1.1 "Even or Odd" #
#########################
def even_or_odd():
    x = float(input('Enter an integer: '))
    if x.is_integer():
        x = int(x)
        print(x)
        if x % 2 == 0:
            for i in range(4, 21, 2):
                print(i)
        else:
            for i in range(3, 20, 2):
                print(i)
    else:
        print('Error: {} is not integer.'.format(x))


#################################
# Que-1.2 "Make Multiply Table" #
#################################
def multi_table_ex():
    a = float(input('Enter an number: '))
    r = int(input('Enter the size of multi table: '))
    for i in range(1, r + 1):
        print('{} x {} = {}'.format(a, i, a * i))


############################
# Que-1.3 "Unit Converter" #
############################
def print_result(before, before_unit, after, after_unit):
    print('{} {} = {} {}'.format(before, before_unit, after, after_unit))


# Conversion for Km <-> Miles
def km_miles(before_unit):
    before = float(input('Enter distance in {}: '.format(before_unit)))

    if before_unit == 'Miles':
        after_unit = 'Km'
        after = before / 1.609
    else:
        after_unit = 'Miles'
        after = before * 1.609

    print_result(before, before_unit, after, after_unit)


def conv_km_m():
    print('1. Kilometers -> Miles')
    print('2. Miles      -> Kilometers')

    choice = int(input('Which conversions would you like to do?: '))

    if choice == 1:
        km_miles('Km')
    elif choice == 2:
        km_miles('Miles')
    else:
        print('Error: Please enter 1 or 2')
        conv_km_m()


# Conversion for Kg <-> Pounds
def kg_pound(before_unit):
    before = float(input('Enter distance in {}: '.format(before_unit)))

    if before_unit == 'Kg':
        after_unit = 'lb'
        after = before * 2.2046
    else:
        after_unit = 'lb'
        after = before / 2.2046

    print_result(before, before_unit, after, after_unit)


def conv_kg_p():
    print('1. KiloGrams -> Pounds')
    print('2. Pounds    -> KiloGrams')

    choice = int(input('Which conversions would you like to do?: '))

    if choice == 1:
        kg_pound('Kg')
    elif choice == 2:
        kg_pound('lb')
    else:
        print('Error: Please enter 1 or 2')
        conv_kg_p()


# Conversion for Kekvin <-> Celsius
def kelvin_celsius(before_unit):
    before = float(input('Enter distance in {}: '.format(before_unit)))

    if before_unit == 'K':
        after_unit = 'C'
        after = before - 273.15
    else:
        after_unit = 'K'
        after = before + 273.15

    print_result(before, before_unit, after, after_unit)


def conv_k_c():
    print('1. Kekvin  -> Celsius')
    print('2. Celsius -> Kekvin')

    choice = int(input('Which conversions would you like to do?: '))

    if choice == 1:
        kelvin_celsius('K')
    elif choice == 2:
        kelvin_celsius('C')
    else:
        print('Error: Please enter 1 or 2')
        conv_k_c()


# main function of Que-1.3
def unit_conversions():
    print('1. KiloMeters - Miles')
    print('2. KiloGrams  - Pound')
    print('3. Kelvin     - Celsius')

    choice = int(input('Which conversions would you like to do?: '))

    if choice < 1 or 3 < choice:
        print('Error: Please enter 1 or 2 or 3')
        unit_conversions()
    else:
        [conv_km_m(), conv_kg_p(), conv_k_c()][choice - 1]


#################################
# Que-1.4 "Fraction Operations" #
#################################
from fractions import Fraction

def add(x, y):
    print('Result of Addition: {}'.format(x + y))

def sub(x, y):
    print('Result of Subtract: {}'.format(x - y))

def mul(x, y):
    print('Result of Multiply: {}'.format(x * y))

def div(x, y):
    print('Result of Division: {}'.format(x / y))

def frac_operations():
    try:
        x = Fraction(input('Enter first fraction: '))
        y = Fraction(input('Enter second fraction: '))
        operator = input('Operation to perform - Add, Sub, Div, Mul')
        if operator in {'Add', 'add'}:
            add(x, y)
        elif operator in {'Sub', 'sub'}:
            sub(x, y)
        elif operator in {'Mul', 'Mul'}:
            mul(x, y)
        elif operator in {'Div', 'div'}:
            div(x, y)
        else:
            print('Error: Please enter operator Add or Sub or Div or Mul')
    except ValueError:
        print('Error: Please enter fraction')


######################################################################
# Que-1.5 "Multiplication table printer with exit power to the user" #
######################################################################
def multi_tables():
    while True:
        a = float(input('Enter an number: '))
        for i in range(1, 11):
            print('{} x {} = {}'.format(a, i, a * i))
        ans = input('Do you want to exit? [Y/n]')
        if ans in {'Y', 'y', 'Yes', 'YES', 'yes', ''}:
            break
