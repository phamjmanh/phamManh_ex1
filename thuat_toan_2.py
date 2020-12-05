print("nhập x:")
x=int(input())
print("nhập y:")
y=int(input())
count=0
while x >= y:
    print('nhập lại lại x:')
    x = int(input())
    print('nhập lại lại y:')
    y = int(input())
while x != y   :
    if y%2!=0:
        y=y+1
        count = count + 1
        print('y:',y)
    else:
        y=y/2
        count = count +1
        print('y:',y)
    if x==y+1:
        count =count +1
        break
print('số bước là',count)
