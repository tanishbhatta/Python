arr = [12,34,56,42]
print("[", end="")
for i in arr:
    if i!=arr[-1]:
        print(i, end=", ")
    else:
        print(i, end="]")

print(arr)