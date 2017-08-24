#Question 2, Zehao Ba (B00732676)
import random

def compute(g, secret_key, p):
    result = int(g**secret_key % p)
    return result

print "Please input the p: "
p = int(raw_input())
print "Please input the g: "
g = int(raw_input())

sa = random.randint(0,100000)
sb = random.randint(0,100000)
print "random key of Alice(SA) is", sa
print "random key of Bob(SB) is", sb

ta_1 = compute(g, sa, p)
ta_2 = compute(g, sb, p)
TA_1 = compute(ta_2, sa, p)
TA_2 = compute(ta_1, sb, p)

if (TA_1 == TA_2):
    print "The secret key is", TA_1
else:
    print "Can not generate secret key."
