import re

email="neeraja@123"
pattern=r"(?=.*[A-Za-z])(?=.*[!@#$%^&*])(?=.*[0-9]).{8,}$"

print(re.findall(pattern,email))
res=re.match(pattern,email)
if res:
    print("password Found")
else:
    print("password Not Found")