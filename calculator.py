def calculator():
    while True:
        print()
        print('What would you like to do?')
        print('  Type 1 to Add')
        print('  Type 2 to Subtract')
        print('  Type 3 to Multiply')
        print('  Type 4 to Divide')
        print('  Type 5 to Quit')
        response = input('Option: ')
        if response == '1':
            number1 = input('Number 1: ')
            number2 = input('Number 2: ')
            print(f'{number1} + {number2} = {int(number1) + int(number2)}')
        elif response == '2':
            number1 = input('Number 1: ')
            number2 = input('Number 2: ')
            print(f'{number1} - {number2} = {int(number1) - int(number2)}')
        elif response == '3':
            number1 = input('Number 1: ')
            number2 = input('Number 2: ')
            print(f'{number1} x {number2} = {int(number1) * int(number2)}')
        elif response == '4':
            number1 = input('Number 1: ')
            number2 = input('Number 2: ')
            print(f'{number1} / {number2} = {int(number1) / int(number2)}')
        elif response == '5':
            break
        else:
            print(f'Unrecognized response: {response}')



if __name__ == '__main__':
    calculator()
