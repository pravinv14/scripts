#  This script will get 10 rows of data from employee_table.xlsx file into csv txt or json file based on your input
#  it needs to have employee_table.xlsx file in correct path to work
#  Usage : python table_to_csv_txt_json.py arg[1] arg[2]
#  arg[1] can be one of txt, csv, json
#  arg[2] can be any filename


import pandas as pd
import sys
import os.path
import json

# Data preparation
un = os.environ.get("USERNAME")
filepath = "C:/Users/" + un + "/Desktop/"
filename = filepath + "employee_table.xlsx"
csvFile = filepath + "data_in_csv.csv"
df1 = pd.read_excel(filename, sheet_name='Employee', index=None)
df2 = pd.read_excel(filename, sheet_name='Department', index=None)
df = pd.merge(df1, df2, on='Dept No', how='left')       # merged data can be used in csv file
df.reset_index(inplace=True, drop=True)

def gen_csv():
    df.sample(10).to_csv(filepath + 'data_in_csv.csv', index=False)

def to_csv(fType, fName):
    print(f'Creating csv file in {filepath}')
    df.sample(10).to_csv(filepath + fName + '.' + fType, index=False)
    print(f'file available at {filepath}{fName}.{fType}')

def to_txt(fType,fName):
    print(f"Creating txt file in {filepath}")
    gen_csv() if not os.path.isfile(csvFile) else print(f'File {filename} already exist using that!')
    dept = {}                                               #  empty dictionary for grouping common lines
    sys.stdout = open(filepath + fName + '.' + fType, 'w')  #  writing to file
    with open(csvFile) as csv_file:
        csv_file = csv_file.readlines()
        for line in csv_file[1:]:                           #  removing first line
            cel = line.split(',')                           #  seperating each line using comma
            if cel[8] in dept:                              #  condition to check if dept name is in empty dict
                dept[cel[8]].append([cel[0], cel[1]])       #  if yes append dept name and emp id and emp name
            else:
                dept[cel[8]] = [[cel[0], cel[1]]]           #  dict key equating to value (list of list)
    for k, v in dept.items():
        print('Department Name:', k)
        for i in v:
            print(f'Emp_ID: {i[0]} Emp_name: {i[1]}')

def to_json(fType,fName):
    print(f"Creating json file in {filepath}")
    gen_csv() if not os.path.isfile(csvFile) else print(f'File {filename} already exist using that!')
    sys.stdout = open(filepath + fName + '.' + fType, 'w')
    dept = {}                                               #  empty dictionary for grouping common lines
    with open(csvFile) as csv_file:
        csv_file = csv_file.readlines()
        for line in csv_file[1:]:
            cel = line.split(',')
            if cel[8] in dept:
                dept[cel[8]].append({"Emp No": cel[0],
                                     "Emp Name": cel[1],
                                     "Job": cel[2],
                                     "Manager": cel[3],
                                     "HireDate": cel[4],
                                     "Salary": cel[5],
                                     "Commenced": cel[6],
                                     "Dept No": cel[7],
                                     "Location": cel[9][:-1]})
            else:
                dept[cel[8]] = [{"Emp No": cel[0],
                                 "Emp Name": cel[1],
                                 "Job": cel[2],
                                 "Manager": cel[3],
                                 "HireDate": cel[4],
                                 "Salary": cel[5],
                                 "Commenced": cel[6],
                                 "Dept No": cel[7],
                                 "Location": cel[9][:-1]}]
        jFile = json.dumps(dept, indent=4)			             
    with open(filepath + fName + '.' + fType, 'w', encoding='utf=8') as outFile:
        outFile.write(jFile)


def process():
    """
    program uses sys.argv with try except block for producing output in csv, txt, json file format
    """
    fType = sys.argv[1]
    fName = sys.argv[2]
    if fType == 'csv':
        to_csv(fType, fName)
    elif fType == 'txt':
        to_txt(fType, fName)
    elif fType == 'json':
        to_json(fType, fName)
    else:
        print("Require FileType(csv, txt, json) to write")


if __name__ == "__main__":
    try:
        process()
    except FileNotFoundError as err:
        print(f'File {filename} not found! \n {err}') 
    except (IndexError, OSError) as err:
        print(f'Need FileName as second argument to write output \n\n Error {err} ')
