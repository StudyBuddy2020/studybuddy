Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> msg="purav"; type(msg);
<class 'str'>
>>> msg=10; type(msg);
<class 'int'>
>>> msg=10.22; type(msg);
<class 'float'>
>>> cats = "clara"; print(cats); type(cats);
clara
<class 'str'>
>>> cats = "clara"; cats; type(cats);
'clara'
<class 'str'>
>>>
>>>
>>>
>>>
>>>
>>> cats = "clara"; print(cats); type(cats);
clara
<class 'str'>
>>> cats = "clara"; cats; type(cats);
'clara'
<class 'str'>
>>>
>>>
>>> cats = "clara"; cats; type(cats);
'clara'
<class 'str'>
>>> cats = "jeff"; cats; type(cats)
'jeff'
<class 'str'>
>>> cats = "jeff"; cats; print (cats)
'jeff'
jeff
>>> cats = "jeff"; cats; print (cats); type(cats)
'jeff'
jeff
<class 'str'>
>>> msg ("Hello world")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'float' object is not callable
>>> msg = "Hello world"
>>> msg = "Hello world"; msg
'Hello world'
>>> cats = ["jeff", "bob"]; cats; print (cats); type(cats)
['jeff', 'bob']
['jeff', 'bob']
<class 'list'>
>>> cats = ["jeff", "bob"]; cats[0]; print (cats); type(cats)
'jeff'
['jeff', 'bob']
<class 'list'>
>>> cats = ["jeff", "bob"]; cats[1]; print (cats); type(cats)
'bob'
['jeff', 'bob']
<class 'list'>
>>> cats = ["jeff", "bob"]; cats[1]; print (cats[0]); type(cats)
'bob'
jeff
<class 'list'>
>>> 7/2
3.5
>>> 7//2
3
>>> 9/2
4.5
>>> 9//2
4
>>> 2*2
4
>>> 3*2
6
>>> 3**2
9
>>> "purav"
'purav'
>>> "purav"; print[0]
'purav'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>>
>>>
>>> name="purav"; print[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> name="purav"; print([0])
[0]
>>> name="purav"; print(name[0])
p
>>> name="purav"; print(name[0])
p
>>> name= "tom"; print(name[0]
... name= "tom"; print(name[0])
  File "<stdin>", line 2
    name= "tom"; print(name[0])
    ^
SyntaxError: invalid syntax
>>>
>>>
>>> name= "tom"; print(name[0])
t
>>> name= "tom"; print(name[1])
o
>>> name= "tom"; print(name[2])
m
>>> name= "tom"; print(name[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> name= "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"; print(name[3])
H
>>> name= "ABCDEF"; print(name[3])
D
>>> name= "ABCDEF"; print(name[1,2,3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: string indices must be integers
>>> name= "ABCDEF"; print(name[1][2][3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> name= "ABCDEF"; print(name[1],[2],[3])
B [2] [3]
>>> name= "ABCDEF"; print(name[1],name[2],name[3])
B C D
>>> name= "ABCDEF"; name[2:]
'CDEF'
>>> name= "ABCDEF"; name[-1]
'F'
>>> name= "ABCDEF"; name[:2]
'AB'
>>> name= "ABCDEF"; name[2:2]
''
>>> name= "ABCDEF"; name[2:2:1]
''
>>> name= "ABCDEF"; name[2:1:1]
''
>>> name= "ABCDEF"; name[1:1:1]
''
>>> name= "ABCDEFIJKLMN"; name[1:1:1]
''
>>> name= "ABCDEFIJKLMN"; name[2:1:1]
''
>>> name= "ABCDEFIJKLMN"; name[2:3:1]
'C'
>>> name= "ABCDEFIJKLMN"; name[2:3:3]
'C'
>>> name= "ABCDEFIJKLMN"; name[2:3]
'C'
>>> name= "ABCDEFIJKLMN"; name[2:4]
'CD'
>>> fname="purav"; lname="chavarkar"; print(a+b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> fname="purav"; lname="chavarkar"; print(a + b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> fname="purav"; lname="chavarkar"; print(fname + lname)
puravchavarkar
>>> fname="purav"; lname="chavarkar"; print(fname+" "+lname)
purav chavarkar
>>> fname="purav"; lname="chavarkar"; print(fname+"~"+lname)
purav~chavarkar
>>>
>>>
>>>
>>>
>>> age=12; fname="purav"; print(age+"~"+fname)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> age=12; fname="purav"; print(age+fname)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> age=12; fname="purav"; print(age+str(fname))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> age=12; fname="purav"; print(str(age)+fname)
12purav
>>>
>>>
>>> age=12; fname="purav"; print(str(age)+"~"+fname)
12~purav
>>> name=purav; name.upper
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'purav' is not defined
>>> name=purav; name.upper()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'purav' is not defined
>>> name=purav; name.upper();
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'purav' is not defined
>>> name="purav"; name.upper();
'PURAV'
>>> name="purav"; name.upper();
'PURAV'
>>> print("fish 1", "fish 2")
fish 1 fish 2
>>> print("fish 1", "fish 2".count(fish))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fish' is not defined
>>> print("fish 1", "fish 2".count(fish))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fish' is not defined
>>> print("fish 1", "fish 2"count(fish))
  File "<stdin>", line 1
    print("fish 1", "fish 2"count(fish))
                            ^
SyntaxError: invalid syntax
>>> print("fish 1", "fish 2".count(fish))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fish' is not defined
>>> print("fish 1", "fish 2").count(fish))
  File "<stdin>", line 1
    print("fish 1", "fish 2").count(fish))
                                         ^
SyntaxError: unmatched ')'
>>> print("fish 1", "fish 2");count(fish))
  File "<stdin>", line 1
    print("fish 1", "fish 2");count(fish))
                                         ^
SyntaxError: unmatched ')'
>>> print("fish 1", "fish 2"); count(fish))
  File "<stdin>", line 1
    print("fish 1", "fish 2"); count(fish))
                                          ^
SyntaxError: unmatched ')'
>>> print(("fish 1", "fish 2").(count(fish)))
  File "<stdin>", line 1
    print(("fish 1", "fish 2").(count(fish)))
                               ^
SyntaxError: invalid syntax
>>>
>>>
>>>
>>>
>>> print("fish 1, fish 2"); count(fish))
  File "<stdin>", line 1
    print("fish 1, fish 2"); count(fish))
                                        ^
SyntaxError: unmatched ')'
>>> print("fish 1, fish 2").count(fish))
  File "<stdin>", line 1
    print("fish 1, fish 2").count(fish))
                                       ^
SyntaxError: unmatched ')'
>>>
>>>
>>> print("fish 1, fish 2")
fish 1, fish 2
>>> print("fish 1, fish 2".count(fish))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fish' is not defined
>>>
>>>
>>>
>>> print("fish 1, fish 2".count("fish"))
2
>>> print("fish 1, fish 2".count("fish"))
2
>>>
>>>
>>>
>>>
>>> print("fish 1, fish 2, fishy 3".count("fish"))
3
>>> print("fish 1, fish 2, fissy 3".count("fish"))
2
>>> print ("The {} {} {} fox". format ('lazy', 'brown', 'sly'))
The lazy brown sly fox
>>> print ("The {3} {2} {1} fox". format ('lazy', 'brown', 'sly'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: Replacement index 3 out of range for positional args tuple
>>> print ("The {3} {2} {1} fox". format ('lazy', 'brown', 'sly'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: Replacement index 3 out of range for positional args tuple
>>> print ("The {} {2} {1} fox". format ('lazy', 'brown', 'sly'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: cannot switch from automatic field numbering to manual field specification
>>> print ("The {0} {2} {1} fox". format ('lazy', 'brown', 'sly'))
The lazy sly brown fox
