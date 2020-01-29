#Andrew Sala 3B
#part 1
quote = 'Love all, trust a few, do wrong to none \n'

wf = open('quote.txt', 'w')

wf.write(quote)
wf.close()

#part 2

rf = open('quote.txt')
data = rf.read()
print(data)
rf.close()

#part 3
quote2 = 'Cowards die many times before their deaths; the valiant never taste of death but once\n'

af = open('quote.txt', 'a')
af.write(quote2)

af.close()

af = open('quote.txt')
data = af.read()
print(data)
af.close()

#part 4
quote3 = 'An overflow of good converts to bad\n'

def write2file(filename, strObj):
    f = open(filename, 'w')
    f.write(strObj)
    f.close()

def readFile(filename):
    rf = open(filename, 'r')
    data = rf.read()
    print(data)
    rf.close()

write2file('anothaone.txt', quote3)
readFile('anothaone.txt')

#part 5

quote4 = 'Better three hours too soon than a minute too late\n'

def append2file(filename, stringObj):
    ap = open(filename, 'a')
    ap.write(stringObj)
    ap.close()

append2file('anothaone.txt', quote4)
readFile('anothaone.txt')














