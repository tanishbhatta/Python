"""
Currency Converter - Capstone 4 (Tanish Bhatta)
- ┌ ┐ └ ┘ ─ │

"""

print("Currency Converter".center(45, "-"))

word_length = len("Currency Table")
padding = 30
inborder_length = word_length + 2*padding

choose = input("""\n
What is your currency?
1. US Dollar
2. Indian Rupee
3. AUS Dollar
4. Nepalese Rupee
-> """)

if choose == "1":
    currency = float(input("\nUS Dollar (USD) = $"))

    print(f"""
    ┌{"─" * inborder_length}┐
    │{"Currency Table":^{inborder_length}}│
    │{"─" * inborder_length}│
    │{"Indian Rupee (INR)":^{inborder_length//2}}│{"₹" + f"{currency/96.34:.2f}":^{inborder_length//2-1}}│
    │{"─" * inborder_length}│
    │{"AUS Dollar (AUD)":^{inborder_length//2}}│{"$" + f"{currency/1.4:.2f}":^{inborder_length//2-1}}│
    │{"─" * inborder_length}│
    │{"Nepalese Rupee (NPR)":^{inborder_length//2}}│{"रु " + f"{currency/153.79:.2f}":^{inborder_length//2}}│
    └{"─" * inborder_length}┘
    """)
elif choose == "2":
    currency = float(input("\nIndian Rupee (INR) = ₹"))

    print(f"""
    ┌{"─" * inborder_length}┐
    │{"Currency Table":^{inborder_length}}│
    │{"─" * inborder_length}│
    │{"US Dollar (USD)":^{inborder_length//2}}│{"$" + f"{currency/96.34:.2f}":^{inborder_length//2-1}}│
    │{"─" * inborder_length}│
    │{"AUS Dollar (AUD)":^{inborder_length//2}}│{"$" + f"{currency/68.71:.2f}":^{inborder_length//2-1}}│
    │{"─" * inborder_length}│
    │{"Nepalese Rupee (NPR)":^{inborder_length//2}}│{"रु " + f"{currency*1.6:.2f}":^{inborder_length//2}}│
    └{"─" * inborder_length}┘
    """)   
elif choose == "3":
    currency = float(input("\nAUS Dollar (AUD) = $")) 

    print(f"""
    ┌{"─" * inborder_length}┐
    │{"Currency Table":^{inborder_length}}│
    │{"─" * inborder_length}│
    │{"Indian Rupee (INR)":^{inborder_length//2}}│{"₹" + f"{currency*68.71:.2f}":^{inborder_length//2-1}}│
    │{"─" * inborder_length}│
    │{"US Dollar (USD)":^{inborder_length//2}}│{"$" + f"{currency/1.4:.2f}":^{inborder_length//2-1}}│
    │{"─" * inborder_length}│
    │{"Nepalese Rupee (NPR)":^{inborder_length//2}}│{"रु " + f"{currency*110.16:.2f}":^{inborder_length//2}}│
    └{"─" * inborder_length}┘
    """)
elif choose == "4":
    currency = float(input("\nNepalese Rupee (NPR) = रु "))

    print(f"""
    ┌{"─" * inborder_length}┐
    │{"Currency Table":^{inborder_length}}│
    │{"─" * inborder_length}│
    │{"Indian Rupee (INR)":^{inborder_length//2}}│{"₹" + f"{currency/1.6:.2f}":^{inborder_length//2-1}}│
    │{"─" * inborder_length}│
    │{"AUS Dollar (AUD)":^{inborder_length//2}}│{"$" + f"{currency/110.16:.2f}":^{inborder_length//2-1}}│
    │{"─" * inborder_length}│
    │{"US Dollar (USD)":^{inborder_length//2}}│{"$ " + f"{currency/153.79:.2f}":^{inborder_length//2-1}}│
    └{"─" * inborder_length}┘
    """)
else:
    exit() 