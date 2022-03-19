Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
math=30
english=50
korean=70
sum=math+english+korea
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    sum=math+english+korea
NameError: name 'korea' is not defined. Did you mean: 'korean'?
sum=math+english+korean
average=sum/3
print(sum,average)
150 50.0
