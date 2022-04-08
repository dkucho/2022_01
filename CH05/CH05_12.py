items = input("Enter items: ").split()
iLen = len(items)
sum = 0
for n in range(0,iLen):
    sum += int(items[n])
avg = round(sum/iLen,1)
print("{}개 수의 합계: {}, 평균: {}".format(iLen,sum,avg))
