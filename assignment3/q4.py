# Zehao Ba B00732676
#Question 4

import math
print 'Please enter the integer message: '
msg = int(raw_input())
print 'Please enter integer e in key(e,n): '
e = int(raw_input())
print 'Please enter integer n in key(e,n): '
n = int(raw_input())

c = int(math.pow(msg,e) % n)
print 'Ciphertext is: ', c

