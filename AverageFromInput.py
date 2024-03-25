#Christopher Buzaid
# CS 175L
#AverageFromInput Exception Handling


def main():
    i = 0
    total = 0
    import sys
    
    try:
        numbers_file = open('numbers.txt', 'r')
    except IOError:
            sys.exit('File not found: numbers.txt - exiting')
            
    for num in (numbers_file):
        num = num.strip()
        try:
            i+=1
            total +=  int(num)
            print(f'I read {i} number(s)  Current number is:   {num}  Total is:   {total}')
        except ValueError:
            print( f'Bad data: {num} skipping')
            i -= 1

    print(f'Average: {total / i}')


if __name__ == '__main__':
    main()
