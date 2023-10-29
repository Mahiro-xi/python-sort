import sys
a = sys.argv
fields = a[1].split(",")
for i in range(len(fields)):
    fields[i] = int(fields[i])
print("asc or dsc")
if input() == "asc":
    fields.sort()
else:
    fields.sort(reverse=True)
for x in range(len(fields)):
    print(fields[x],end="")