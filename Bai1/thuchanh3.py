# Phần A
# Bài 1
def bai1():
    x = 8
    y = 2
    print(x + y * 3)
    print((x + y) * 3)
    print(x**y)
    print(x % y)
    print(x / 12.0)
    print(x // 6)

# Bài 2
def bai2(): 
    x = 54.66
    print(round(x))
    print(int(x))

# Phần B
# 1)
def isprime(k):
    if (k<2):
        return 0
    for i in range(2,k):
        if (k%i==0):
            return 0
    return 1

def sodx (k):
   temp,s=(0,k)
   while k>0:
       temp = temp*10 + (k%10)
       k//=10
   if (temp == s):
       return 1
   return 0

def socp (k):
    import math
    scp = math.sqrt(k)
    if (scp*scp == k):
        return 1
    return 0

def sohh (k):
    sum = 0
    for i in range (1,k):
        if (k%i==0):
            sum+=i
    if (sum == k):
        return 1
    return 0

def caua():
    so = int(input("Vui lòng nhập 1 số nguyên: "))
    if (isprime(so) or sodx(so) or socp(so) or sohh(so)):
        return 1
    return 0

# 2)
def caub ():
    a = int(input("Vui lòng nhập số bắt đầu: "))
    b = int(input("Vui lòng nhập số kết thúc: "))
    for i in range (int(a),int(b)):
        if (isprime(i) or sodx(i) or socp(i) or sohh(i)):
            print(i)

# 3)
def gcdkodequy (a,b):
    maxNumber = max(a,b)
    gcd = 1
    for i in range (1,maxNumber+1):
        if (a%i==0 and b%i==0):
            gcd = i
    return gcd

def lcmkodequy (a,b):
    minNumber = min(a,b)
    lcm = 1
    for i in range (1,minNumber+1):
        if (a%i==0 and b%i==0):
            lcm = (a*b)//i
    return lcm

def gcd (a,b):
    if (b==0):
        return a
    return gcd(b,a%b)

def lcm (a,b):
    return int((a*b)/gcd(a,b))

# Bài 4
def listprime ():
    k = int(input("Vui lòng nhập số nguyên: "))
    for i in range (0,k+1):
        if (isprime(i)):
            print(str(i)+",",end='')

# Bài 5
def listfirstprime():
    m = int(input("Vui lòng nhập vào số nguyên: "))
    i = 0
    while (m>0):
        if (isprime(i)):
            print(str(i)+",",end='')
            m-=1
        i+=1

# Bài 6
def bai6 ():
    for i in range (99,1000):
        if (i%7==0 and i%5):
            print(str(i)+",",end="")

# Bài 7
def bai7():
    a = int(input("Vui lòng nhập số bắt đầu: "))
    b = int(input("Vui lòng nhập số kết thúc: "))
    for i in range (a,b+1):
        if (i%9==0 and i%7==0):
            print(i)
            break

# Bài 8
def bai8():
    k = int(input("Vui lòng nhập 1 số nguyên: "))
    cnt,sum=(0,0)
    while (k>0):
        sum += k%10
        cnt += 1
        k //= 10
    print("sum=",sum)
    print("count=",cnt)

# Bài 9
def luythuadivided (a,k):
    if (k==0):
        return 1
    if (k==1):
        return a
    if (k%2 == 0):
        return luythuadivided(a,int(k/2)) * luythuadivided(a,int(k/2))
    else:
        return a * luythuadivided(a,int(k/2)) * luythuadivided(a,int(k/2))

def luythuadequy (a,k):
    if (k==0):
        return 1
    return a * luythuadequy(a,k-1)

# Bài 10
def bai10 ():
    k = int(input("Vui lòng nhập số nguyên dương: "))
    cnt = 1
    temp = k
    while k>0:
        if ((k//10)>=1):
            cnt *= 10
        k //= 10
    while cnt > 0:
        print(int(temp/cnt))
        temp %= cnt
        cnt //= 10
