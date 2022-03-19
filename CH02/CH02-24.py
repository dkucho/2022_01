Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#float() 함수
x=float(5)
y=float('15.5')
z=x+y
print(x,y,z)
5.0 15.5 20.5
int('15.5')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int('15.5')
ValueError: invalid literal for int() with base 10: '15.5'
fval=float('15.5')
ival=int(fval)
print(fval,ival)
15.5 15
