#임의의 여러수를 입력으로 받아 평균을 내는 함수를 작성하고,
#함수를 호출하여 사용하는 프로그램을 작성하세요.

def func_avg(*args):
    sum=0
    for n in args:
        sum+=n
    return sum/len(args)


avg_res = func_avg(10,20,30,40,50)
print(avg_res)
