# Phần A
# 1)
import numpy as np
x = np.arange(1,11)

def cau1IA ():
    print(type(x))

def cau2IA ():
    print(x.shape)

def cau3IA ():
    import math
    Y = np.zeros(10,dtype=int)
    Z = np.zeros(10,dtype=int)
    for i in range(0, len(x)):
       Y[i] = math.pi - x[i]
       Z[i] = math.cos(x[i]) - math.sin(x[i])
    print(Y)
    print(Z)

def checkPrime(k):
    if (k<2):
        return 0
    for i in range(2,int(np.sqrt(k))+1):
        if (k%i==0):
            return 0
    return 1

def cau4IA ():
    sole = x[x%2 != 0]
    sochan = x[x%2 == 0]
    prime = np.array([k for k in x if checkPrime(k)])
    print(sole)
    print(sochan)
    print(prime)

def cau5IA ():
    t = np.where(x%2==0,-1,-2)
    print(t)

def IIA ():
    print(x.max())
    print(x.min())
    print(x.argmax())
    print(x.argmin())

def cau1IIIA ():
    a = np.array([1,2,3,2,3,4,3,4,5,6])
    b = np.array([7,2,10,2,7,4,9,4,9,8])
    # Cách 1
    temp = []
    for i in a:
        if i in b and i not in temp:
            temp.append(i)
    arr = np.array(temp)
    print(arr)

def cau2IIIA ():
    a = np.array([1,2,3,2,3,4,3,4,5,6])
    b = np.array([7,2,10,2,7,4,9,4,9,8])
    # Cách 2
    arr = np.intersect1d(a,b)
    print(arr)

def IVA ():
    a = np.array([2, 6, 1, 9, 10, 3, 27])
    arr = np.array([k for k in a if k > 5 and k < 10])
    print(arr)

# Phần B
def cau1B ():
    k = int(input("Vui lòng nhập vào kích thước 1 ma trận vuông lớn hơn 2: "))
    while (k<=2):
        k = int(input("Vui lòng nhập lại kích thước 1 ma trận vuông lớn hơn 2: "))
    matrix = np.ones((k,k))
    for i in range(1,k-1):
        for j in range(1,k-1):
            matrix[i,j] = 0
    print(matrix)
    

matrix = np.random.randint(1,10,size=(3,5))

def cau2aB ():
    print(matrix)
    sumDong = np.sum(matrix,axis = 1)
    sumCot = np.sum(matrix,axis = 0)
    print(sumDong," ",sumCot)
        
def cau2bB ():
    print(matrix)
    maxDong = matrix.max(axis = 1)
    maxCot = matrix.max(axis = 0)
    minDong = matrix.min(axis = 1)
    minCot = matrix.min(axis = 0)
    print(maxDong," ",maxCot)
    print(minDong," ",minCot)

def cau2cB ():
    print(matrix)
    sochan = matrix[matrix % 2 == 0]
    sole = matrix[matrix % 2 != 0]
    print(sochan)
    print(sole)

def cau2dB ():
    print(matrix)
    sole = matrix[:,::2]
    tbc = np.mean(sole,axis=0)
    print(tbc)

def cau2eB():
    print(matrix)
    tong = np.sum(matrix[:,::2])
    print(tong)

def cau2fB():
    print(matrix)
    max_row = np.amax(matrix,axis = 1)
    min_row = np.amin(matrix,axis = 1)
    print(max_row - min_row)

def cau3aB ():
    matrix = np.random.randint(0,10,size=(5,5))
    print(matrix)
    chinh = np.sum(np.diag(matrix))
    phu = 0
    for i in range(len(matrix)):
        phu += matrix[i,len(matrix)-i-1]
    print(chinh," ",phu)

def cau3bB ():
    matrix = np.random.randint(0,10,size=(5,5))
    print(matrix)
    chinhMax = np.amax(np.diag(matrix))
    chinhMin = np.amin(np.diag(matrix))
    for i in range(len(matrix)):
        phuMax = np.amax(matrix[i,len(matrix)-i-1])
        phuMin = np.amin(matrix[i,len(matrix)-i-1])
    print(chinhMax,chinhMin)
    print(phuMax,phuMin)
