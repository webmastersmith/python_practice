# reverse sentence
wd = 'the cat went up!'
str_list = ['.... ;.....', 'k)M a ?jz.nP']


for i in str_list:
    y = list(filter(lambda x: x == '.', i ))
    z = "".join(y)
    print(z)