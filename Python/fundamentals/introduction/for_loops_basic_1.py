for x in range(0,150):
    print(x)

for x in range(5,1000,5):
    print(x)

for x in range(1,100):
    if x%10 == 0:
        print("Coding Dojo")
    elif x%5 == 0:
        print("Coding")
    else:
        print(x)
count = 0
y = 0
while count <= 500000:
    y += count
    count +=1
    if count > 500000:
        break

print(y)

start = 2018
print(start)
while start >= 0:
    start = start -4
    if start<0:
        break
    print(start)

low = 2
high = 15
mult = 4
for i in range(low,high + 1):
    if i % mult == 0:
        print(i)
