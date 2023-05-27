# Phần A
# 1)
L = [2,4,9,3,5]
def cau1A ():
    print(L[2])
    print(L[-1])
    print(len(L))
    print(L[0:2])
    print(0 in L)
    print(L + [24,1,4])
    print(tuple(L))

# 2)
# a)
def cau2aA():
    L[0] = -L[0]
    print(L)

# b)
def cau2bA():
    L.append(20)
    print(L)

# c)
def cau2cA():
    L.insert(3,0)
    print(L)

# d)
def cau2dA():
    for i in range(len(L)):
        if (i == 4):
            L.remove(L[i])
    print(L)

# e)
def cau2eA():
    L.extend([0,0,0])
    print(L)

# f)
def cau2fA():
    L.sort(reverse=True)
    print(L)

# Phần B
# 1)
A = ['3','27','5','123','9','1']

def stringCMP():
    A.sort(key= str, reverse=False)
    print(A)

def intCMP():
    A.sort(key = int,reverse=False)
    print(A)

# 2)
B = [12,24,35,70,88,120,155]
def delIndex1():
    for i,x in enumerate(B):
        if (i == 1) or (i == 2):
            B.remove(x)
    for i,x in enumerate(B):
        if (i == 1) or (i == len(B)-1):
            B.remove(x)
    print(B)

def delIndex2():
    arr = [B[i] for i in range(len(B)) if i == 0 or i == 4 or i == 5]
    print(arr)

# 3)
C = [1,2,3,1,2,5,6,7,8]

def xoaTrung1():
    arr = []
    for i in C:
        if i not in arr:
            arr.append(i)
    arr.sort()
    print(arr)

def xoaTrung2():
    print(sorted(set(C),key=C.index))

# 4)
D = [1,1,1,1,2,2,2,2,3,3,4,5,5]

def demTrung1():
    arr = []
    for i in D:
        if (i not in arr):
            arr.append(i)
    
    items_cnt = []
    for i in arr:
        cnt = 0
        for j in D:
            if (i == j):
                cnt += 1
        items_cnt.append(cnt)
    
    dict = {}
    for i in range(len(arr)):
        dict[arr[i]] = items_cnt[i]

    for key,value in dict.items():
        print(key,":",value)

def demTrung2():
    from collections import Counter
    counts = dict(Counter(D))
    capTrung = {key:value for key,value in counts.items() if value >= 1}
    print(capTrung)

# 5)
def inputa():
    arr = []
    x = int(input("Nhập số phần tử của: "))
    for i in range(x):
        val = input("Nhập giá trị a[{}]: ".format(i+1))
        arr.append(val)
    print(arr)

def inputb():
    arr = []
    i = 0
    while (True):
        val = int(input("Nhập giá trị a[{}]: ".format(i+1)))
        arr.append(val)
        i += 1
        if (val == -1):
            break
    print(arr)

# Bài 6
E = [1,1,2,3,5,8,13,21,34,55,89]
F = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def listChunga ():
    arr = []
    for i in range(len(E)):
        for j in range(len(F)):
            if (E[i] == F[j] and E[i] not in arr):
                arr.append(F[j])
    print(arr)

def listChungb ():
    arr = []
    for i in F:
        if i in E:
            arr.append(i)
    print(arr)


