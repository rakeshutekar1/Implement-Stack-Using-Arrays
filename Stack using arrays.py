#NAME:RAKESH UTEKAR
#ROLLNO:3116066
#AIM: TO IMPLEMENT STACKS USING ARRAYS.

from array import *
print("::STACKS USING ARRAYS::\n\n")
stk=array("i",[])
ch=0
a=0
b=0
top=-1
while(ch<=5):
			print("1.INSERT AN ELEMENT(PUSH)\n")
			print("2.DELETE AN ELEMENT(POP)\n")
			print("3.PRINT STACK TOP(PEEK)\n")
			print("4.DISPLAY STACK\n")
			print("5.EXIT\n")
			ch=int(input("ENTER YOUR CHOICE:"))
			if(ch==1):
				a=int(input("ENTER THE ELEMENT YOU WANT TO ADD:"))
				stk.append(a)
				top+=1
			elif(ch==2):
				b=stk.pop()
				print("DELETED ELEMENT IS:\n"+str(b))
				top-=1
			elif(ch==3):
				c=stk[top]
				print("STACK TOP IS:\n"+str(c))
			elif(ch==4):
				for k in range(top):
	 				print("\n")
					print(stk[k])
			else:
				print("EXITING\n")
				exit()
"""
Output:
fy-comp17@fycomp17-ThinkCentre-M57e:~/cs116066$ python py.py
::STACKS USING ARRAYS::


1.INSERT AN ELEMENT(PUSH)

2.DELETE AN ELEMENT(POP)

3.PRINT STACK TOP(PEEK)

4.DISPLAY STACK

5.EXIT

ENTER YOUR CHOICE:1
ENTER THE ELEMENT YOU WANT TO ADD:2
1.INSERT AN ELEMENT(PUSH)

2.DELETE AN ELEMENT(POP)

3.PRINT STACK TOP(PEEK)

4.DISPLAY STACK

5.EXIT

ENTER YOUR CHOICE:1
ENTER THE ELEMENT YOU WANT TO ADD:3
1.INSERT AN ELEMENT(PUSH)

2.DELETE AN ELEMENT(POP)

3.PRINT STACK TOP(PEEK)

4.DISPLAY STACK

5.EXIT

ENTER YOUR CHOICE:1
ENTER THE ELEMENT YOU WANT TO ADD:4
1.INSERT AN ELEMENT(PUSH)

2.DELETE AN ELEMENT(POP)

3.PRINT STACK TOP(PEEK)

4.DISPLAY STACK

5.EXIT

ENTER YOUR CHOICE:2
DELETED ELEMENT IS:
4
1.INSERT AN ELEMENT(PUSH)

2.DELETE AN ELEMENT(POP)

3.PRINT STACK TOP(PEEK)

4.DISPLAY STACK

5.EXIT

ENTER YOUR CHOICE:3
STACK TOP IS:
3
1.INSERT AN ELEMENT(PUSH)

2.DELETE AN ELEMENT(POP)

3.PRINT STACK TOP(PEEK)

4.DISPLAY STACK

5.EXIT

ENTER YOUR CHOICE:4


2
1.INSERT AN ELEMENT(PUSH)

2.DELETE AN ELEMENT(POP)

3.PRINT STACK TOP(PEEK)

4.DISPLAY STACK

5.EXIT

ENTER YOUR CHOICE:5
EXITING

fy-comp17@fycomp17-ThinkCentre-M57e:~/cs116066$ 
"""
