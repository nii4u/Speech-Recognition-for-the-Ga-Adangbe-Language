

f = open("./Session1.txt", "r")
lines = f.readlines()
result=open("Session1.txt", "w")

for line in lines:
    line = '##'+ line
    result.write(line)
result.close()
