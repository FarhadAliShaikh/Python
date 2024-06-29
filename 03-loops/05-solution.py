string = "strings"

for char in string:
    if string.count(char) == 1:
        print(char)
        exit()

print("All chars of string are repeated")
        