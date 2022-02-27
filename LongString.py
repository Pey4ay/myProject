import random
import string

mind = int(input('Enter the minimum word length:'))
maxd = int(input('Enter the maximum word length:'))
k = int(input('Enter the number of rows:'))

name = str(input('Enter the file name:'))

f = open(name + '.txt', 'a')

for i in range(k):
    per = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(mind, maxd)))
    f.write(per+'\n')
    if i == k:
        f.write(per)
f.close()