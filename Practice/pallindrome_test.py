def pallindrom(string):
    rev=""
    for letter in string:
        rev=letter+rev
    if rev == string:
        return True
    else:
        return False

print(pallindrom("carrace"))