fhand = open('mbox.txt')
##print(fhand)

stuff = 'Hello\nWorld!'
##print(stuff)

stuff = 'X\nY'
##print(stuff)

##len(stuff)

xfile = open('mbox.txt')
##for cheese in xfile:
##    print(cheese)

fhand = open('mbox.txt')
count = 0
##for line in fhand:
##    count = count + 1
##print('Line Count:', count)

fhand = open('mbox.txt')
inp = fhand.read()
##print(len(inp))

##fhand = open('mbox.txt')
##for line in fhand:
##   if line.startswith('r'):
##    print(line)

##fhand = open('mbox.txt')
##for line in fhand:
##    line = line.rstrip()
##    if line.startswith('r'):
##        print(line)

fhand = open('mbox.txt')
##for line in fhand:
##    line = line.rstrip()
##    if not line.startswith('r'):
##        continue
##    print(line)


fname = raw_input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('r'):
        count = count + 1
print('There were',count,'subject lines in',fname)

