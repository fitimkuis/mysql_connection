#To be able to read csv formated files, we will first have to import the
#csv module.
import csv

class CSVfile(object):
    def __init__(self):
        self.elist = []

    def read_csv(self):
        path = 'animals.csv'
        
        with open(path, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                self.elist.append(row)
                print row
        return str(self.elist)
        f.close()


read = CSVfile()
b = read.read_csv()
print b



'''
#Robot Framework
*** Settings ***
Library     read_csv.py

*** Testcases ***
CSVRobot
    csv
    
*** Keywords***
csv
    ${val}=     read_csv
    Should Contain      @{val}    dog     List does't contain expected value

*** Variables ***
${val}
'''
