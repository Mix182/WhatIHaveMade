import os

count = int(input("type count:\n"))
adding = ""

for i in range(count):
    adding = adding + "."

with open("list.txt" ,"w") as f:
    f.write("[")
    for i in range(count):
        f.write("\"" + adding + "\",\n \t\t\t")
        
    f.write("]")