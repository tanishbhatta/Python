'''
Write a program that takes a list of target words and a long sentence. Your loop must check each word in the sentence one by one. Find the very first word from the sentence that also exists in your target list, print it, and immediately stop searching.If no words match, print a message saying nothing was found.

Example Inputs & Outputs

Example 1
Target List: ["apple", "banana", "cherry"]
Sentence: "the monkey ate a banana and dropped a cherry"
Output: "banana"
'''
target_array = []

while True:
    target_ask = str(input("Enter the target words (E for exit): ")).strip().lower()
    if target_ask == 'e':
        break
    target_array.append(target_ask)

print("\nTargetted List :-")
for i, wrd in enumerate(target_array):
    print(f"{i+1}. {wrd.title()}")

sent = str(input("\nStart your sentence now\n-> ")).strip()
sent_list = sent.split(' ')
sent_array = [word.strip(',.;:\'"') for word in sent_list]

for i in sent_array:
    if i.lower() in target_array:
        print(i)