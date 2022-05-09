a=int(input("1~29까지의 원하는 정수를 입력하세요. : "))

for i in range(1,a+1):
    if i%3==0:
        print("x",end=' ')
    else :
        print(i,end=' ')

