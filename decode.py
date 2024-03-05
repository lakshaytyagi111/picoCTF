
# // AUTHOR : P3rryTHEplatipu55
he = "h"
with open("picoCTF/te.txt", "r") as file:
    for line in file:
        deci = int(line.strip())
        string = chr(deci)
        he += string

print(he)
