# README 1.2
# write a function which will be able to generate a sqrt of a particular number till 10

def sqrt(a):
    li = []
    for i in range(1,a+1):
        i = i**2
        li.append(i)
    return li

print(sqrt(5))