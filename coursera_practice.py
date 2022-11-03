""""
int_val = 67
str_val = 'Himark Academy'
flt_val = 87.98

print('The integer hash value is: ' + str(hash(int_val)))
print('The string hash value is: ' + str(hash(str_val)))
print('The float hass value is: ' + str(hash(flt_val)))
"""
import csv

def parse(csvfilename):
    table = []
    with open(csvfilename, "r") as csvfile:
        csvreader = csv.reader(csvfile, skipinitialspace =True)
        for row in csvreader:
            table.append(row)
    return table


def print_table(table):
    for row in table:
        print("{:<19}".format(row[0]), end='')

        for col in row[1:]:
            print("{:>4}".format(col), end='')
        print("", end='\n')

table = parse(r"C:\Users\HP\Desktop\sample1.csv")
print_table(table)