import re

list = ["cat", "dog", "horse", "mouse"]

regg = re.compile(r'^.')

for name in list:
    if(regg.findall(name)):
        print(name)
    else:
        print("Not Match")

print('\n\n')
print(regg.findall(list[0]))
print(re.match(regg, list[0]))
print(re.match(regg, list[1]).group())