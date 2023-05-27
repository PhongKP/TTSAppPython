#1A)
# 3 Vi Du: Tu Dien, Danh Ba DT, Danh Ba user

# 2A)
def cau2A():
    d = {'b':200,'a':100,'c':1}
    print(d['a'])
    print(d.get('e',None))
    print(len(d))
    print(d.keys())
    print(d.values())
    print(d.pop('b'))
    print(d)

# 3A)
def cau3Aa():
    d = {'b':200,'a':100,'c':1}
    d['b'] = - d['b']
    print(d)

def cau3Ab():
    d = {'b':200,'a':100,'c':1}
    d.update({'e':500})
    print(d)

def cau3Ac():
    d = {'b':200,'a':100,'c':1}
    d.pop('b')
    print(d)

def cau3Ad():
    d = {'b':200,'a':100,'c':1}
    for k in sorted(d):
        print (k,d[k])
        
# 1B)
def cau1B():
    s = set()
    for k in range(1,201):
        s.add(k)
    print(s)

def isprime(k):
    if k<2:
        return False
    for i in range(2,k):
        if (k%i==0):
            return False
    return True

def cau2B():
    s = set()
    for i in range(10,2000):
        if (isprime(i)):
            s.add(i)
    print(sorted(s))

def giao (s,k):
    newArr = set()
    for i in s:
        if i in k:
            newArr.add(i)
    if (len(newArr)==0):
        return -1
    return newArr

def hoi (s,k):
    return s.union(k)

def diff (s,k):
    return s.difference(k)

def symtis_diff (s,k):
    z = s.symmetric_difference(k)
    return z

def cau3B():
    import random
    set1= set()
    set2 = set()
    for i in range(10):
        k = random.randint(10,2000)
        set1.add(k)
    for i in range(15):
        k = random.randint(10,2000)
        set2.add(k)
    print(diff(set1,set2))
    print(symtis_diff(set1,set2))

def cau4B():
    dir = {}
    lit = list()
    sopt = int(input("Nhap so phan tu: "))
    for i in range(sopt):
        value = input()
        dir.update({i:value})
    for i in dir.values():
        if i not in lit:
            lit.append(i)
    print(lit)

def cau5B():
    dir = {}
    sopt = int(input("Nhap so phan tu: "))
    for i in range(sopt):
        value = input()
        dir.update({i:value})
    for i in dir.values():
        if i >= max(dir.values()):
            print(i)

def cau6B():
    dir = {}
    sopt = int(input("Nhap so phan tu: "))
    for i in range(sopt):
        value = int(input())
        dir.update({value:i})
    for index,i in enumerate(sorted(dir.keys(),reverse=True)):
        if (index == 0 or index == 1):
            print(i)
cau6B()
        