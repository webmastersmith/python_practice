# reverse sentence
# sampleInput = "DoG"
# str_len = len(sampleInput)
# s = sampleInput
# upper_num = 0

# for i in s:
#     # find caps
#     if ord(i) < 91:
#         upper_num += 1
# lower_num = abs(str_len - upper_num)
# print(s.upper() if upper_num > lower_num else s.lower())

# find num vowels
# sampleInput = input()
# # result = -404;
# vowels = ["a", "e", "i", "o", "u"]
# num_vowels = 0
# for i in sampleInput:
#     if i in vowels:
#         num_vowels += 1

# #write your Logic here:


# #OUTPUT [uncomment & modify if required]
# print(num_vowels)


# sampleInput = "The big dog jumped high over the lazy red fox and the man with the red hat sat high in the chair and laughed"
# # result = -404;
# s = list(map(lambda x: x.lower(), sampleInput.split(' ')))
# #write your Logic here:
# print(s)
# unique = set(s)
# d = {}
# for i in unique:
#     d[i] = 0

# for i in s:
#     d[i] += 1

# over_one = []
# for k,v in d.items():
#     if v > 1:
#         over_one.append(f'{k}: {v}')
# # print(l)
# print("\n".join(sorted(over_one)))


# s = 'abcdabcdabcdefegeheiabcedi'
# l = ['a', 'b', 'a', 'A']
# print(' '.join([str(s.count(v)) for v in 'aeiou']))

# print(pow(2, 2))
# s = '1234567 89'
# n = 2
# o = '-'.join([s[i:i+n] for i in range(0, len(s), n)])
# print(o)


# o = []
# for i in range(0, len(s), n):
#     o += [s[i:i+n]]
# print(*o, sep='-')


# print(10 // 3)
# a = 'hello'
# b = a
# b = b.capitalize()
# print(a, b)


import math


def sumDigits(a, b):
    A = 1
    for n in range(1, a+1):
        A *= n
    B = 1
    for n in range(1, b+1):
        B *= n
    Q = str(math.floor(A / B))
    R = 0
    for n in Q:
        R += int(n)
    # print(R)
    return R


x = [(5, 3), (8, 6), (12, 12)]
# 5,3 = 2
# 8,6=11
# 12,12 = 1
# print(sumDigits(a, b))
# print(int(math.factorial(a) / math.factorial(b)))
for a, b in x:
    print(sum([int(n) for n in str(int(math.factorial(a)/math.factorial(b)))]))
