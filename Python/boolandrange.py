print(bool("True"))
print(bool("False"))
print(bool(""))
for x in range(1,11,2):
    print (x)
print("\n")
for x in range(10,0,-2):
    print(x)
print("nested loop")
for x in range(1,6):
    for y in range (1,x+1):
        print(y,end='')
    print()