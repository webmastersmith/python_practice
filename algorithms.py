# freecodecamp tutorial

# # Recursion ***********************************************************
# # simple loop
# def fac(n):
#     total = 1
#     for i in range(2, n+1):
#         total *= i
#     return total
# print(fac(5))

# # Recursion
# def fac(n, total):
#     if n == 0:
#         return total
#     return fac(n-1, (total * n))
# print(fac(5, 1))  # 120

# # Recursion 2
# def fac(n):
#     if n == 1:
#         return n
#     else:
#         temp = fac(n-1)
#         temp = temp * n
#     return temp
# print(fac(5))

# # same as
# def fac(n):
#     if n == 1: return n
#     else: return n * fac(n-1)
# print(fac(5))

# # same as
# def fac(n):
#     return n if n == 1 else n * fac(n-1)
# print(fac(5))

# # print(fac(3))

# Permutation ****************************************************
def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket, end=",")
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)


permute('abc')

# loop
