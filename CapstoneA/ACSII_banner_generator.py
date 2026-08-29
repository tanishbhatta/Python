## ACSII Banner - Capstone 2 (Tanish Bhatta)

print("ASCII Banner Generator".center(45, "-"))
word = input("\nEnter your word: ")
padding = 8

fill_length = 2*padding + len(word)
borderlength = fill_length + 2

#printout
print(f"""\n
{"#" * borderlength}
#{" ":^{fill_length}}#
#{word:^{fill_length}}#
#{" ":^{fill_length}}#
{"#" * borderlength}
""")
