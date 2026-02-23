#Regular Expression
#re.match only check the starting of the string matches or not
import  re
text="My name is sath"
result=re.match("My",text)
if result:
    print("Match Found")
else:
    print("Not Match")
#Output--->Match Found
#search
searchresult=re.search("name",text)
print(searchresult)
#Output--><re.Match object; span=(3, 7), match='name'>
print(searchresult.group())
print(searchresult.start())
print(searchresult.end())
print(re.findall("r.t","rat rit rot"))

print(re.findall("^Sun","Sun day"))
print(re.findall("^Hello", "Hello world"))

print(re.findall("world$", "hello world"))
print(re.findall("[abc]", "apple banana cat"))


email="admin@gmail.com"
if re.match("[A-Za-z]+@",email):
    print("Email Found")
else:
    print("Email Not Found")
# Does the ENTIRE string exactly match the pattern?
# If yes → returns a Match object
# If no → returns None
#d{10} digits which has exact count 10
print(re.fullmatch(r"\d{10}","1234567898"))
print(re.findall(r"\d+","price 50 to 100 range"))

for n in re.finditer(r"\d+","price 50 to 100 range and 100 to 50"):
    print(n.group(),n.start(),n.end())
#Give find data along with start and end indexes
# 50 6 8
# 100 12 15
# 100 26 29
# 50 33 35

text1="admin2@gmail.com"
result3=re.search(r"\w+@\w+\.\w",text)
if result3:
    print("Email Matched")
else:
    print("Email Not Match")
print(re.search(r"\d+", "Age is 25"))

print(re.search(r"^a.*c$", "abnkkkkkknnc"))
# ?=@ loo head assertion
m = re.search(r"\w+(?=@)", "test@gmail.com")
print(m.group())

print(re.search("pyton","Python",re.I))

text2="one\ntwo\nthree"
print(re.findall(r"^t\w+",text2,re.M))
