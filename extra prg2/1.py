import re
email=input("Enter Email:")
pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(pattern,email):
         print("Valid Email Address")
else:
         print("Inalid Email Address")
