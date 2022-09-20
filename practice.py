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


# x = [(5, 3), (8, 6), (12, 12)]
# for a, b in x:
#     print(sum([int(n) for n in str(int(math.factorial(a)/math.factorial(b)))]))

# n = 6
# print(''.join([str(i) for i in range(1, n+1)]) * n)
# a = 5
# b = 4
# print(f'{a-b}{a+b}')

# a = ['A', 'Z']
# for i in range(24):
#     a.insert(-1, ' ')

# print(a.count(' '))
# print(sum([k+1 for k, i in enumerate(a) if i == ' ']))

# def isprime(num):
#     for n in range(2, int(num**0.5)+1):
#         if num % n == 0:
#             return False
#     return True
# n = 10  # 7
# a = [i for i in range(2, n) if isprime(i)]
# print(a[-1])

# s = "AGCASERTASDFTT TTGGGGGGGG"
# fn = s.count
# print(*s)

# x = sum([int(str(n)[-1:]) for n in A])%(10**9 + 7)

# coding challenge
# def lastSum(N, A):
#     if N == 0:
#         return sum(A) % (10**9 + 7)

#     A.append(int(str(A.pop(N-1))[-1:]))
#     return lastSum(N-1, A)


# print(lastSum(3, [123, 324, 2133]))

# a = '4 4 4 4 4 4 4 4'
# b = '3 3 3 3 3 3 3 3'
# c = (sum(map(int, b.split())) - sum(map(int, a.split())))
# print(c)

# message = ['PROFESSOR', 'JIM', 'JONES']
# for m in message:
#     if m == 'PROFESSOR':
#         print("Prof", end='.')
#     elif m == 'DR.':
#         print("Dr.", end='')
#     else:
#         print(m[0], end='.')


# x = 'hello'
# def baseN(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
#     return ((num == 0) and "0") or (baseN(num // b, b).lstrip("0") + numerals[num % b])
# for i in x:
#     print(baseN(ord(i), 36), end=',')

# import base36
# base36.dumps([])
# print(''.join(['1', '2']))


# challenge 8-30-2022
# def averageValue(N, A):
#     A.sort()
#     return f"{sum(A[1:-1]) / (N-2):.5f}"


# print(averageValue(6, [2, 3, 1, 4, 5, 2]))  # 2.75000
# print(averageValue(4, [1, 3, 5, 7]))  # 4.00000
# print(averageValue(5, [1000, 2000, 3000, 4000, 5000]))  # 3000.00000


# codiing challenge 8-31-2022
# def tribonacciNumbers(N):
#     x = [0, 0, 1]
#     for i in range(N):
#         if N <= 2:
#             return 0
#         else:
#             if i > 2:
#                 x.append(x[i-1]+x[i-2]+x[i-3])
#     return x[-1]


# print(tribonacciNumbers(2))  # 0
# print(tribonacciNumbers(8))  # 13
# print(tribonacciNumbers(22))  # 66012


# recursion
# def lastSum(N, A):
#     if N == 0:
#         return sum(A)
#     A[N-1] = A[N-1] % 10
#     return lastSum(N-1, A)

# without recursion
# def lastSum(N, A):
#     return sum([n % 10 for n in A])


# print(lastSum(3, [123, 324, 2133]))  # 10
# print(lastSum(4, [1, 1223, 324, 2133]))  # 11
# print(lastSum(4, [12, 1223, 324, 2133]))  # 12


def leftrightString(S):
    first_letter = S[0]
    if S.count(first_letter) <= 1:
        return 0
    countIdx = 0
    tally = 0
    for idx, i in enumerate(S):
        # prevent errors by by-passing fist item in string.
        if idx == 0:
            continue
        # if letters are same and side-by-side.
        if i == first_letter and S[idx-1] == first_letter:
            countIdx = idx
            continue
        # track last match position and distance from new match.
        if i == first_letter:
            countIdx += 1
            tally += idx - countIdx
    return tally


# OUTPUT [uncomment & modify if required]
print(leftrightString('cdacebdaecaddddbdebed'))  # 9
print(leftrightString('abcdef'))  # 0
print(leftrightString('bbadba'))  # 2
