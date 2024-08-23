# Extract the list from list
li  = [1,2,3,4,[3,4,5,6],"Farid",[13,34,45,56]]

def lis(n):
    li1 = []
    for i in li:
        if type(i) == list:
            li1.append(i)
    yield li1

for i in lis(li):
    print(i)