# identity

x = [2,4,6]
y = [2,4,6]
z = y

print(x == y)
print(x is y) # is =  x ve y aynıdır. True yada False döner. False
print(x is not y) # x y değil midir? True yada False döner. True

print(z is y) # z ile y aynı nesne midir? True
print(z is not y)


# membership

print(2 in x) # in = 2  x in içinde var mıdır? True
print(20 in x) # False

print(20 not in x) # not in 20  x in elemanı değil midir? True
print(2 not in x) #False