def thing():
    print('Hello')
    print('Fun')

thing()
print('Zip')
thing()

x = 5
print('Hello')

def print_lyrics():
    print('Es atkal te, ye, čau.')
    print('man arī patīk gulēt')

print('Yo')
x = x + 2
print(x)
print_lyrics()

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
greet('en')
greet('es')
greet('fr')

print('en')

def greet():
     return"Hello"
print(greet(),"Glenn")
print(greet(),"Sally")

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('en'),'Glenn')
print(greet('es'),'Sally')
print(greet('fr'),'Michael')

def addtwo(a,b):
    added = a + b
    return added
x = addtwo(3,5)
print(x)


hrs = input('Enter Hours:')
fhrs = float(hrs)
pay = input('Enter Rate:')
fpay = float(pay)
if fhrs > 40:
    ohrs = fhrs - 40
    opay = fpay*1.5
    print(40*10+ohrs*opay)
    



