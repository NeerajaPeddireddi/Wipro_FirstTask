# Question – Assertions & Regular Expression Modifiers
# Topics Covered:Assertions,Regular expression modifiers
# Write a Python program that:
# 1.Validates a strong password using regular expressions with the following rules:
# Minimum 8 characters
# At least one uppercase letter
# At least one lowercase letter
# At least one digit
# At least one special character
import re

password="Nr@123"
pattern="(?=.*[A-Za-z])(?=.*[0-9])(?=.*[@#$%^&*]).{8,}$"
result=re.findall(pattern,password)
if result:
    print("Password Matched")
else:
    print("Password Not Matched")
# 2.Uses lookahead assertions (?=)
Email="rama@gmail.com"
pattern="(?=.*[A-Za-z0-9])(?=.@)(?=.*[A-Za-z])"
result=re.findall(pattern,Email)
if result:
    print("Email Matched")
else:
    print("Email Not Matched")
# 3.Uses regular expression modifiers such as:
# re.IGNORECASE
# re.multiline
# re.DOTAL
print(re.findall("Hello","hello",re.I))
text="Hello\nHi\nHarsh"
print(re.findall(r"^H\w+",text,re.M))
text2="Welcome\nMy world"
print(re.findall(r"W.*d",text2,re.DOTALL))

# 4.Demonstrates how modifiers affect pattern matching with examples
print(re.findall(r"Python","python Python PYTHON",re.IGNORECASE)) #Output-->['python', 'Python', 'PYTHON']
print(re.findall(r"^apple","apple\nbanana\napple\nbanana",re.MULTILINE)) #with multiline search start of all new line gives output-->['apple', 'apple']
print(re.findall(r"^H.*d$","Hello\nWorld",re.DOTALL)) #With dotall we get after \n also output-->['Hello\nWorld']