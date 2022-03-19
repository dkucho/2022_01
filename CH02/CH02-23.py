Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#int()함수
a=int(5.5)
b=int('20')
print(a,b)
5 20
b=int('20.5')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    b=int('20.5')
ValueError: invalid literal for int() with base 10: '20.5'
a='100'
a+10
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a+10
TypeError: can only concatenate str (not "int") to str
int(a)+10
110
