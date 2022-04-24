money=0

print("1.자장면:5500원")
print("2.짬뽕:6000원")
print("3.볶음밥:7000원")
print("4.탕수육:15000원")
print("5.주문종료")
print("")

while True:
    name=input("메뉴 번호를 선택해주세요: ")
    money+=money
    if name=='1':
        money+=5500
    elif name=='2':
        money+=6000
    elif name=='3':
        money+=7000
    elif name=='4':
        money+=15000
    else:
        name='5'
        print("주문종료")
        break

print("")
print("총 주문금액 : " + str(money) + "원")
