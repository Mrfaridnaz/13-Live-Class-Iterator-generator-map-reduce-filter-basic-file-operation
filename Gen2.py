def sqrt_fun(n):
    x = [i**2 for i in range(1,n+1)]
    yield x


for i in sqrt_fun(6):
    print(i)