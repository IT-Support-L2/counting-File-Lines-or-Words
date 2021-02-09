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
