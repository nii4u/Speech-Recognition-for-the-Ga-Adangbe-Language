
f = open("./Session41.txt", "r")
lines = f.readlines()
result=open("Session41.txt", "w")

for line in lines:
    line = '##'+ line
    result.write(line)
result.close()
