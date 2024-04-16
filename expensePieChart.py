#Christopher Buzaid
#CS 175L
#expensePieChart

import matplotlib.pyplot as plt
import sys

def main():
    try:
        data = open('expenses.txt', 'r')
        value_list = []
        labels_list = []
        
    except IOError:
        sys.exit('Cannot open expenses file')
        
    for line in data:
        line = line.rstrip('\n')
        label, value  = line.split('\t')
        
        try:
            value = int(value)
            value_list.append(value)
            labels_list.append(label)
            
        except ValueError:
            print(f'Error {label,value}')
            
    plot_pie(value_list, labels_list)
        
            
def plot_pie(value_list, labels_list):
        plt.pie(value_list, labels = labels_list)
        plt.title('Monthly Expenses')
        plt.show()
        
if __name__ == '__main__':
    main()
