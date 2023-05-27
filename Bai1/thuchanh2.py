# Phan A
# 1)
s = "pythonfile.py"
#a
print(s[2])
#b
print(s[-1])
#c
print(len(s))
#d
print(s[0:7])
#e
print(s[6:10])
#f
first = s.find(".")
print(s[first:])
#g
for i in range(len(s)):
    print(s[len(s)-i-1],end="")

print()
#2a)
def dectobin ():
    binary = input("input binary here: ")
    dec = int(binary,2)
    print(dec)

#b
def bintodec ():
    decimal = input("Decimal: ")
    binary = bin(int(decimal))
    print(binary)

#c
def hextodec ():
    hex = input("Hex: ")
    dec = int(hex,16)
    print(dec)

#d
def octatobin ():
    octa = input("Octa: ")
    binary = bin(int(octa))
    print(binary)

# Phan B
# 1)
def tachchuoi ():
    string = input("Input String here: ")
    list = string.split(" ")
    for i in list:
        print(i+" ",end="")

# 2)
def tachchuoivabin ():
    string = input("Input String here: ")
    list = string.split(",")
    for i in list:
        decimal = int(i,2)
        print(decimal,sep=',',end="")

# 3)
def countletter ():
    cnt = 0
    string = input("Input String here: ")
    for i in string:
        if (i.isalpha()):
            cnt+=1
    return cnt

# 4)
def captilizeletter ():
    string = input("Input String here: ")
    ss = string.split(" ")
    for i in ss:
        word = i.capitalize()
        print(word+" ",end="")

# 5)
def comparestr ():
    up,low=0,0
    string = input("Input String here: ")
    for i in string:
        if (i.isupper()):
            up+=1
        elif (i.islower()):
            low+=1
    print("so chu hoa:",up)
    print("so chu thuong:",low)

# 6)
import math
def isprime (k):
    if (k<2):
        return 0
    for i in range(2,k):
        if(k%2==0):
            return 0
    return 1

def checkprime ():
    string = input("Input String here: ")
    ss = string.split(",")
    for i in ss:
        if(isprime(int(i))):
            print(i+" ",end="")
# checkprime()

# 7)
def checkLap ():
    cnt = 0
    map = {}
    string = input("Input String here: ")
    for i in string.split(" "):
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    print(map)
checkLap()

