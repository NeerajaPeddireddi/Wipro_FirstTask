# question – match, search, patterns, meta-characters & special sequences
# topics covered:
# match and search functions, regular expression patterns, meta-characters, special sequences
# 1. uses re.match() to check whether a string starts with a valid employee id in the format emp followed by 3 digits (e.g., emp123)
import re
result1=re.match(r"emp\d{3}$","emp123")
if result1:
    print("match")
else:
    print("not match")
# 2.uses re.search() to find the first occurrence of a valid email address in a given text
text="admin2@gmail.com"
result2=re.search(r"[a-za-z0-9]+@[a-za-z]+\.[a-za-z]{2,}",text)
if result2:
    print("email matched")
else:
    print("email not match")
# 3. demonstrates the use of meta-characters (., *, +, ?) and special sequences (\d, \w, \s) in the patterns
print(re.findall("r.t","rat rit rot"))
print(re.findall(r"ca*t","cat caat caat ct cit"))
print(re.findall(r"ca+t","cat caat caat ct cit"))
print(re.findall("colou?r","color colour colouur"))
print(re.findall(r"\d{2}","price range is from 50 to 100"))
print(re.findall(r"\w","sachin@gmail.com ram_123")) #single char and underscore matched individually and w-[a-za-z0-9]
text1="admin2@gmail.com"
result3=re.search(r"\w+@\w+\.\w",text)
if result3:
    print("email matched")
else:
    print("email not match")

print(re.findall(r"\s","hello\tworld\n friends"))
# 4. prints matched groups using capturing parentheses
text2 = "today date is 2026-01-20"
pattern = r"(\d{4})-(\d{2})-(\d{2})"

match = re.search(pattern, text2)  # use search for group access

if match:
    print("year:", match.group(1))
    print("month:", match.group(2))
    print("day:", match.group(3))
