import re
text="DevOps123"
if re.match(r'^[A-Za-z0-9]+$',text):
         print("Alphanumeric string")
else:
         print("Not Alphanumeric string")
