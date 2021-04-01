import pandas as pd
import os
k=1
while k==1:
    try:
        column_qty = int(input("How many columns do you want to enter? : "))
        k=3
    except ValueError:
        print("Invalid entry. Please enter an integer only.")

column_name = []
table_data = {}
os.system("cls")
i=0
while i<column_qty:
    el = input(f"Enter the name of column {i+1} : ")
    column_name.append(el)
    table_data[el] = []
    i=i+1
os.system("cls")
m=0
ans = 'y'
while ans.lower() == 'y':
    print(f"Enter data for row {m+1}")
    print('-----------------------------')
    for i in range(column_qty):
        data = input(f"{column_name[i]} : ")
        table_data[column_name[i]].append(data)

    ans = input("Do you want to add more data? (y/n) : ")
    os.system("cls")
    m = m+1
os.system("cls")
filename = input("Enter the filename of the spreadsheet : ")
os.system("cls")

df = pd.DataFrame(table_data)
os.system("mkdir output_folder")
df.to_csv(f"./output_folder/{filename}.csv")
os.system("cls")
print("Converted to CSV")