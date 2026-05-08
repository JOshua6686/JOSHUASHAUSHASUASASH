#Duck checker

print("Welcome to the duck checker! This program will check if the word 'duck' is in a paragraph you provide.")
para = input("PLease enter a paragraph: ")

length = len(para)

if str("duck") or "DUCK"  or "Duck" in para:
    print("The paragraph contains the word duck.")
else:
    print("The paragraph does not contain the word duck.")
    para.append("duck" * length)