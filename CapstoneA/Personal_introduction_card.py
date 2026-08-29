# Personal Introduction Card - Capstone 1 (Tanish Bhatta)

print("Personal ID Card Generator".center(45, "-"))

insert_date = input("\nWhat is today's date? ")
insert_name = input("What is your name?: ")
insert_age = input("What is your age?: ")
insert_city = input("What city do you live in?: ")

heading = len("Personal Identification Card")
nameP = len(insert_name)
ageP = len(insert_age)
goalP = len(insert_city)

maxi = max(heading, nameP, ageP, goalP)

main_padding = 8
out_of_main = (2 * main_padding) + maxi
borderlength = out_of_main + 2

print("\nID Card of" , insert_name , "as on" , sep=" ", end=f" {insert_date}")
print(f"""\n
{"#" * borderlength}
#{" " * out_of_main}#
#{"Personal Identification Card":^{out_of_main}}#
#{" " * out_of_main}#
#{f" Name: {insert_name}":<{out_of_main}}#
#{f" Age: {insert_age}":<{out_of_main}}#
#{f" City: {insert_city}":<{out_of_main}}#
#{" " * out_of_main}#
{"#" * borderlength}
""") 



