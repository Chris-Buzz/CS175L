#Christopher Buzaid
# CS 175L
#AverageFromInput


def main():
    numbers_file = open('numbers.txt', 'r')
    i = 0
    total = 0
    
    for num in (numbers_file):
        num = num.strip()
        i+=1
        total +=  int(num)
        print(f'I read {i} number(s)  Current number is:   {num}  Total is:   {total}')


    print(f'Average: {total / i}')


if __name__ == '__main__':
    main()
