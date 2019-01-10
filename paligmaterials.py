#Lielaakaa un mazaakaa skaitlja aprekjinashana peec izveidotaa masiiva

from sys import maxsize
x = []

while True:
    y = input("Input number:")
    if y == "done":
        break
    try:
        x.append(int(y))
    except:
        try:
            x.append(float(y))
        except:
            continue

N = len(x)
smallest = maxsize
largest = x[0]

for i in range(N):
    if x[i] > largest:
        largest = x[i]
    if x[i] < smallest:
        smallest = x[i]

print("Number array: ",x)
print("Largest input number is ", largest)
print("Smallest input number is ", smallest)


#Videejaa aritmeetiskaa aprekjinashana peec izveidotaa masiiva

avg = 0
for i in range(N):
    avg = avg + x[i]

avg = avg/N

print("Average value of number array is: ", avg)


#Sakartota saraksta izveidoshana peec izveidotaa masiiva

newx = sorted(x)
newnewx = sorted(newx, reverse = True)


print("Sorted array: ", newx)
print("Sorted array: ", newnewx)
