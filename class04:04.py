import re

## create a string object to search

TEXT = "phone: 22-234-888 (234)543-2111 714-501-6611 222,222,2222 my number is 1-800-123-4567"

#create a regex object
regg = re.compile(r'(\d{3}(.|\s{1})(\d{3})(.|\s{1})(\d{4}))')

# create a seach result obj
fullResult = regg.findall(TEXT)

# display each group
for group in fullResult:
    print("{},{},{}".format(group[0],group[2],group[4]))
# create a seach result object
fullResult = regg.search(TEXT)
print(fullResult.group())
