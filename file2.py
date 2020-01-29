# Andrew Sala
# 3B

with open('story.txt') as f:
    story = f.readlines()

print('First line')
print(story[0])
print('Last line')
print(story[len(story)-1])

print('Even lines')
for i,j in enumerate(story):
    if i % 2 != 0:
        print(j)

print('Odd lines')
for i,j in enumerate(story):
    if i % 2 == 0:
        print(j)


with open('names.txt') as f:
    name_list = f.readlines()

def printnames():
    for i in name_list:
        print(i, end='')

printnames()

print('\nName that starts with I')
for i in name_list:
    if i.lower().startswith('i'):
        print(i)


def sort_names():
    names_sorted = sorted(name_list)
    with open("names_sorted.txt", 'w') as f:
        for i in names_sorted:
            f.write(i)


sort_names()

def addname(name):
   # name_list.append('{}\n'.format(name))
    with open('names.txt', 'a') as f:
        f.write('{}\n'.format(name))


addname('Kevin')

sort_names()
