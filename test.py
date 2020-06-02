import re


file = open("kris.txt", mode="w")
file.write("Hello Kris")
file.close()

line = "Cats are sma23rter than dogs"

res = re.compile(r'^e\S(.*\S)t')

matchObj = re.search(res, line, re.M|re.I)
print(matchObj)
#print(len(line))
#print(matchObj.span())
#print(matchObj.group())
