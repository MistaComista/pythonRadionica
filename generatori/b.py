def range(n):
    r=[]
    i=0
    while i!=n:
        r.append(i)
        i+=1
    return r


# for i in range(20):
#     if i == 10:
#         break
#     print(i)


class Range:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.n:
            raise StopIteration()
        else:
            print("generating {}".format(self.i))
            self.i += 1
            return self.i - 1

i = Range(10).__iter__()

def f():
 for i in Range(10):
     if i == 5:
         break
     print(i)

import dis
dis.dis(f)

i = Range(10).__iter__()
while True:
    try:
        print(next(i))
    except StopIteration:
        break

print("---")

def range():
    i = 0
    while True:
        yield i
        i += 1

import math
from itertools import islice
for i in islice(filter(lambda x: x > 0, map(lambda x: math.sin(x), range())), 10):
    print(i)

# x=range(10)
# print(dir(x))

#print(list(islice((math.sin(x) for x in range() if math.sin(x) > 0),10)))
