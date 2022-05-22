

even = {2,4,6,8}
prime = {2,3,5,7,11}

print(even,prime)

# Union |
print(prime|even)
# Intersection &
print(prime&even)
# difference -
print(prime-even)

a = int(input('Please enter your age: '))

if a <= 18:
    print('you are under age')
elif a <= 60:
    print('you are adult')
elif a <= 100:
    print('you are super senior')
else:
    print('Please enter valid value')

a = [1,2,3,4,5,6]
b = []
c = []
for i in a:
    if i>=6:
        break

    if i%2==0:
        b.append(i)
    else:
        if i == 5:
            continue
        c.append(i)
        
print(a,b,c)


for i in (1,2,3,4,5):
    print(i)
else:
    # break
    print("the loop wasn't interrupted")


number = 5
for i in range(1,5):
    if i == number:
        break
else:
    print("Number is not found")

for i in range(1,7):
    if i == number:
        continue
    print(i)

count=6
while(count<6):
    if i==count:
        print(count)
        break
    count+=1
else:
    print("the loop wasn't intterrupted")


# help()

import math
print(math.pi)
print(math.sqrt(49))
print(math.pow(7,2))
