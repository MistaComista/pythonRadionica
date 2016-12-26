from os import listdir
from os.path import isdir, join

def walk(path):
    dirs = [path]
    while dirs:
        d = dirs.pop()
        yield d
        subdirs = [join(d,f) for f in listdir(d) if isdir(join(d, f))]
        dirs.extend(subdirs)


# nemogucnost ranog izlaska i stack overflow
def recwalk(path, f):
    f(path)
    subdirs = [join(path,c) for c in listdir(path) if isdir(join(path, c))]
    for s in subdirs:
       recwalk(s, f)

for i in walk("D:\\pythonRadionica"):
    if "generatori" in i:
        break
    print(i)




