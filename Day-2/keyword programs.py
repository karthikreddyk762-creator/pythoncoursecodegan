Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import keyword
print(keyword.kwlist)#List of all
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print(len(keyword.kwlist)#Total number of key words
a = 7
      
SyntaxError: '(' was never closed
print(len(keyword.kwlist))#Total number of key words
      
35
a=7
      
b=14
      
c=21
      
a
      
7
>>> b
...       
14
>>> c
...       
21
>>> a=b=c=7
...       
>>> a
...       
7
>>> b
...       
7
>>> c
...       
7
>>> a,b,c = 7,14,21
...       
>>> a
...       
7
>>> 
>>> b
...       
14
>>> c
...       
21
>>> 
>>> a,b = b,a
...       
>>> a
...       
14
>>> b
...       
7
>>> del a
...       
>>> a
...       
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a
NameError: name 'a' is not defined
