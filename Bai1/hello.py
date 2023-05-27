# import math
# from decimal import*
# from fractions import*
# getcontext().prec=2
# frac1 = Fraction(1,4)
# frac2 = Fraction(1,4)
# print(frac1+frac2)

# a = 10
# b = 2
# c = a ** b
# print("c=%d"%c)

# a = 'string 1'
# b = 'string 2'
# print(a+b)

# name = "Phong"
# print("Your name is " + name)

# print(16)
# print(16*4)
# print(16**4)
# print(16#24)
# print(6/9)
# print(4/0)

# import math
# radius = float(input("Input radius here: "))
# s = math.pi * (radius ** 2)
# print(s)

# import math
# def odd (a,b):
#     for i in range (a,b):
#         if(i%2==0):
#             print(i," ")

# odd(1,10)

# def prime (k):
#     if(k<2):
#         return 0
#     for i in range (2,int(math.sqrt(k))):
#         if (k%i==0):
#             return 0
#     return 1

# print("7 la so nguyen to",prime(7))

# p = "Python"
# t = "k" + p[1:]
# print(t)

# def maxOfpacks (n,k):
#     import array as arr
#     dp = [0] * k
#     for i in range(0,k):
#         dp[i] = [0] * n
#     for i in range(0,n):
#         for j in range(0,k):
#             if (i==0 or j==0):
#                 dp[i][j] = 0
#             elif (j >= i):
#                 dp[i][j] = max(i+dp[i-1][j-1],dp[i-1][j])
#             else:
#                 dp[i][j] = dp[i-1][j]
#     return dp[n][k]

# maxOfpacks(8,5)

