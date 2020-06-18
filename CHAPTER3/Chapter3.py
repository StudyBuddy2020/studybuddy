#IF - ELIF - ELSE

#Example 1
"""
if 10<8 :                           #Change the expression and show 
    print("That is right") 
"""

#Example 2
"""
hungry = False

if hungry : 
    print("Can anyone feed me please")

"""
"""
hungry = True

if hungry : 
    print("Can anyone feed me please")
else:
    print("You are not hungry!")

"""

#Example 3
"""
loc = 'Michigan'

if loc == 'Ohio':
    print("I love Bueckeyes")
else :
    print("I dont belong to Ohio")
"""

#Example 4
"""
loc = 'Detroit'

if loc == 'Ohio':
    print("I love Bueckeyes")
elif loc == 'Michigan':
        print("Michigan is the best")
elif loc == 'Detroit':
        print("Detroit is the coolest city")
else :
    print("I dont belong to any of these states")
"""

# Example 5
#Remember identation matters a lot in Python so 
"""
loc = 'Seattle'

if loc == 'Ohio':
    print("I love Bueckeyes")
elif loc == 'Michigan':
        print("Michigan is the best")
elif loc == 'Detroit':
        print("Detroit is the coolest city")
else :
    print("I dont belong to any of these states")
"""

# Example 6
#Complex boolean values
"""
weight = 64
height = 164

if 18.5 <= weight / height**2 < 25:
    print("BMI is normal")
else :
    print("It is not normal")
"""


#LOOPS
#FOR loops
#Example 1
"""
study_buddy = ['Saket','Purav','Abhida','Devansh','Aditya']

for buddies in study_buddy:
    print(buddies)
print("Here are your Python study_buddy program buddies")
"""

#Example 2
"""
nlist = [1,2,3,4,5,6,7,8,9,10]
for num in nlist:
    #Even nos
    if num % 2 == 0:
        print("It is an even number", num)
    else:
        print(f'Odd Number:{num}')             #fstring 
"""

#WHILE loops
#Example 1
"""
x = 0
while x <= 11:
    print(f'Current value of x is :{x}')
    x = x + 1
    #x += 1
"""
#Example 2
"""
x = 100
while x < 101:
    print(f'Current value of x is :{x}')
   # x = x + 1
    x += 1
else:
        print("X is obviously greater than 5")
"""

#BREAK, CONTINUE, PASS
#PASS
#Example 1
"""
a = [1,2,'hi']

for item in a :
    #comment
    pass         #Remove

print ("This can be used as a placeholder for programmers to come back to this later")
"""

#CONTINUE
#Example 1
"""
myname = "Nidhi"

for letter in myname:
    print(letter)

"""
"""
myname = "Nidhi"

for letter in myname:
    if letter == 'i':
     continue
    print(letter)
"""

#BREAK
#Example 1
"""
myname = "Nidhi"

for letter in myname:
    if letter == 'h':
     break
    print(letter)
"""

#Example 2 (Using while loop)

x = 0

while x < 11:
    if  x == 10:
        break
    print(f'Current value of x is :{x}')
    x = x + 1
