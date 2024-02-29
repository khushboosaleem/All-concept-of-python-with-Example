def add(a,b):
    print(a+b)



    
    
def sub(a,b):
    return a-b


import csv

def read_file(file_name):
    with open(file_name, newline='') as f:
        read = csv.reader(f, delimiter=' ')
        for row in read:
            print(row)