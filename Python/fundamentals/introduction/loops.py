for x in range(0,10,2):
    print(x)

for y in range (5,1,-3):
    print(y)

for z in 'Hello':
    print(z)

my_list = ["abc", 123, "xyz"]
for i in range(0,len(my_list)):
    print(i, my_list[i])

count = 0
while count <= 5:
     print("looping - ", count)
     count += 1 

for val in "string":
    if val == "i":
        break
    print(val)

for val in "string":
    if val == "i":
        continue
    print(val)