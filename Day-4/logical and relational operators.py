Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
a//b
2
a%b
0
a**b
10240000000000
9//2
4
9%2
1
2**3
8
4**2
16
a<b
False
>>> a>
SyntaxError: incomplete input
>>> a>b
True
>>> a<=b
False
>>> a>=b
True
>>> a==b
False
>>> a!=b
True
>>> c
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> c
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> NameError: name 'c' is not defined
SyntaxError: invalid syntax
>>> c=10
>>> c+=10
>>> c+=10
>>> c%3
0
>>> c**2
900
>>> c/=2
>>> c
15.0
>>> c-=10
>>> c
5.0
>>> True and True
True
>>> n = 10
>>> n%2==0
True
>>> n%3==0
False
>>> n%2==0 and n%3==0
False
>>> n%8==0 or n%3==0
False
n
10
n<5
False
not n<5
True
#str list tuple set dict
s="codegnan"
"e" in s
True
"z" in s
False
"f" in s
False
"o" in s
True
"o" not in s
False
1=[1,2,3,4]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
1=[1,2,3,4]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
1=[1,2,3,4]
4 in l
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
6 in l
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    6 in l
NameError: name 'l' is not defined

L = [1,2,3,4]
4 in L
True
2 not in L
False
4 in L
True

S={1,2,3,4,5,6,7}
6 in s
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    6 in s
TypeError: 'in <string>' requires string as left operand, not int
S={1,2,3,4,5,6,7}
6 in S
SyntaxError: multiple statements found while compiling a single statement
"<pyshell#51>"
'<pyshell#51>'
d = {"name" : "karthik", "batch" : 63,"course": "python"}
"name" in d
True
"python" in d
False
"age" not in d
True
l = [1,2,3,4]
id(1)
140711352584632
m = [1,2,3,4]
id(1)
140711352584632
1 is m
False
n = 1
id(n)
140711352584632
l is n
False
1 is not m
True
1 is not n
False
a+=10
a
30
id(a)
140711352585560
s = {1,2,3,4}
id(s)
1566132099264
s.add(5)
s
{1, 2, 3, 4, 5}
id(s)
1566132099264
id(1)
140711352584632
9 & 10
8
9|10
11
9^10
3
8>>2
2
8<<2n
SyntaxError: invalid decimal literal
8>>3
1
~8
-9
~12
-13
~45
-46
a = 10
b = 10.3
c = "Codegnan"
print(a,b,c)
10 10.3 Codegnan
print("a value is",a)
a value is 10
print("a value is",a,"| b value is" ,b,' | c value is' , c)
a value is 10 | b value is 10.3  | c value is Codegnan
print(a,b,c)
10 10.3 Codegnan
print(a,b,c,sep = '')
1010.3Codegnan
print(a,b,c,sep = '')

1010.3Codegnan
print(a,b,c,sep= '\n')
10
10.3
Codegnan
print(a,b,c,sep = '\t')
10	10.3	Codegnan
print(a,b,c,sep = '\t' , end = "@")
10	10.3	Codegnan@
print(a,b,c,sep = '\t' , end = '\n\n')
10	10.3	Codegnan

print(f'a={a} b={b} c={c} ')
a=10 b=10.3 c=Codegnan 
print(f'a=%d b=%f c=%s' % (a,b,c))
a=10 b=10.300000 c=Codegnan
print(f "a value is {a} | b value is {b} | c value is {c}")
SyntaxError: invalid syntax
print(f"a value is {a} | b value is {b} | c value is {c}")
a value is 10 | b value is 10.3 | c value is Codegnan
print("a = %d b=%f c=%s' % (a,b,c))
      
SyntaxError: incomplete input
print("a = %d b=%f c=%s" % (a,b,c))
      
a = 10 b=10.300000 c=Codegnan
