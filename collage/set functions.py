Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> dict = {'tag'={1:"boys"},'lucky'={2:"girls"}}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> KeyboardInterrupt
>>> dict = {'tag':{1:"boys"},'lucky':{2:"girls"}}
>>> dict['tag']
{1: 'boys'}
>>> dict1={'tag':23,'tag':23}
>>> dict1
{'tag': 23}
>>> a={1,2,3}
>>> b={3,4,5}
>>> a.union(b)
{1, 2, 3, 4, 5}
>>> a&b
{3}
>>> a.intersection(b)
{3}
>>> a.difference(b)
{1, 2}
>>> a-b
{1, 2}
>>> b-a
{4, 5}
>>> a^b
{1, 2, 4, 5}
>>> a.symmetric_differene(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.symmetric_differene(a)
AttributeError: 'set' object has no attribute 'symmetric_differene'. Did you mean: 'symmetric_difference'?
>>> a.symmetric_differene(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.symmetric_differene(b)
AttributeError: 'set' object has no attribute 'symmetric_differene'. Did you mean: 'symmetric_difference'?
>>> a.symmetric_difference(a)
set()
>>> a.symmetric_differene(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.symmetric_differene(b)
AttributeError: 'set' object has no attribute 'symmetric_differene'. Did you mean: 'symmetric_difference'?
>>> a.symmetric_difference(b)
{1, 2, 4, 5}
