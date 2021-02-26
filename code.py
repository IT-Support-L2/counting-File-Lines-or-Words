# counting words

with open("file.txt", 'r') as f:
    content = f.read()
    words_list = content.split()
    num_words = len(words_list)
    print(num_words)

# counting lines using len method

num_lines = len(open("file.txt").readlines())
print(num_lines)

# counting lines using counter

with open('file.txt', 'r') as f:
    content = f.readlines()
    num_lines = 0
    for _ in content:
        num_lines += 1
    print(num_lines)

# visualizing first 30 characters of a file

with open("file.txt", 'r') as f:
    content = f.read()
    beginning_chars = content[:30]
    print(beginning_chars)

# creating a list with 3rd element of each line

with open("file.txt", 'r') as f:
   l = []
   content = f.read()
   n = content.splitlines()
   for i in n:
      if i.isspace() == True or i == '':
         n.remove(i)
   print(n)
   for line in n:
      m = line.split()
      for word in m:
         if m.index(word) == 2:
            l.append(word)
   print(l)

# shortest frequency dictionary count

s = 'Python is fun'
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
print(d)


# useful lambda, list comprehension, zip and filter examples

L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]
L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2)) if x1 > 10 and x2 < 5]
print(L3)



l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
opposites = list(filter(lambda x: (len(x[0]) > 3 and len(x[1]) > 3), zip(l1, l2)))   
print(opposites)



lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
map_testing = map(lambda s: "Fruit: " + s, lst_check)
print(map_testing)



countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
b_countries = filter(lambda word: "B" in word, countries)
print(b_countries)
