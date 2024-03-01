# Christopher Buzaid
#CS 175L
#Temperature Conversions

def main():
    controlLoop()

def convertToKelvin(fahrenheit):
    kelvin = (fahrenheit - 32) *  5/9 + 273.1
    return(kelvin)
    

def convertToCentigrade(fahrenheit):
    centigrade = (fahrenheit - 32) *  5/9 
    return(centigrade)


def doConversion():
    fahrenheit = getFahrenheit()
    kelvin = convertToKelvin(fahrenheit)
    centigrade = convertToCentigrade(fahrenheit)
    print()
    print(f'Farenheit: {fahrenheit:.1f}\nKelvin: {kelvin: .1f}\nCentigrade: {centigrade: .1f}')
    print()

def repeat():
    how_many = int(input('How many conversions would you like to do this time? '))
    i = 1
    for i in range(how_many):
        doConversion()
        i +=1

def controlLoop():
    answer = input('Do you want to do some conversions(Yes or No)? ')
    answer = answer.upper()
    if answer == 'YES':
        repeat()
    else:
        print('Program Exited')
        pass

def getFahrenheit():
    fahrenheit = float(input('Enter Temperature in fahrenheit: '))
    while fahrenheit <= -50 or fahrenheit >= 130:
            print()
            print('The input temperature is invalid!')
            print()
            fahrenheit = float(input('Please give a temperature between -50 and 130: '))
    return(fahrenheit)

# This code will call the 'main' function if the entire program was run.
if __name__ == '__main__':
    main()
