x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finis')

if x == 5:
    print('Equals 5')
if x > 3:
    print('Ģreater than 3')
if x > 5 :
    print('Ģreater than 5')
if x >= 5:
    print('Ģreater than or Equals')



if x <6:
    print('Less than 6')
if x <= 5:
    print('Less than or Equals 5')
if x!= 6:
    print('Not equal 6')
if x == 5:
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x == 6:
    print('Is 6')
    print('Is Still 6')
    print('Third 6')
print('Afterwards 6')

x = 5
if x > 2:
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

for i in range(5):
    print(i)
    if i > 2:
        print('Bigger than 2')
    print('Done with i',i)
print('All Done')

x = 42
if x > 1:
    print('More than one')
    if x < 100:
        print('Less than 100')
print('All done')

x = 4
if x > 2:
    print('Bigger')
else:
    print('Smaller')
print('All done')

if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
print('All done')

if x < 2:
    print('Bellow 2')
elif x >= 2:
    print('Two or more')
else:
    print('Something else')

astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)


astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)

rawstr = input('Ēnter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')
