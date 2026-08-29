"""
Multiplication Table - Capstone 6 (Tanish Bhatta)
Structure reference: ┌ ┐ └ ┘ ─ │


"""
from math import sqrt

#Title
print("Multiplication Table Generator".center(45, '-'))

#Ask
while True:
    raw_num = input("\nGenerate multiplication table of the number: ").strip()
    
    if raw_num.isdigit(): 
        num = int(raw_num)
        break
    print("\n\tInvalid token: Enter an integer")

while True:
    raw_multiple = input("Number of multiplies: ").strip()

    if raw_multiple.isdigit():
        multiple = int(raw_multiple)
        break
    print("\n\tInvalid token: Enter an integer")

#Assigning values
unsure_count1 = len(f"Multiplication Table of {num}")
unsure_count2 = len(f"{num} x {multiple} = {num*multiple}")

sure_count = max(unsure_count1, unsure_count2)

list_of_num_multiple = []
const = 0
padding = 4
empty_padding = sure_count + padding
allign = empty_padding//3

#Appending list as per need
while const < multiple:
    list_of_num_multiple.append(num)

    const += 1

const = 0

#Header
print(f"┌{'─' * empty_padding}┐")
print(f"│{f"Multiplication Table of {num}":^{empty_padding}}│")
print(f"│{'─' * empty_padding}│")

#Table
for index, numfac in enumerate(list_of_num_multiple):

    result = numfac*(index+1)

    result_root = sqrt(result)
    
    if result_root == int(result_root):
        print(f"│{num:^{allign}} x {index+1:^{allign-3}} = {str(result) + "*":^{allign-3}}│")
    else:
        print(f"│{num:^{allign}} x {index+1:^{allign-3}} = {str(result):^{allign-3}}│")

    const += 1

#Footer
print(f"└{'─' * empty_padding}┘")
