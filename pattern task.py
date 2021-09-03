Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range (1,6):
	print('*'*i)

	
*
**
***
****
*****
>>> for i in  range (1,6):
	print(f"{i}"*i)

	
1
22
333
4444
55555
>>> for i in range (1,7):
	print(" "*(6-i),end" ")
	
SyntaxError: invalid syntax
>>> for i in range (1,7):
	print(" "*(7-i), end = "")

	
                     
>>> for i in range (1,7):
	print(" "*(7-i), end = "")
	print("*"*i)

	
      *
     **
    ***
   ****
  *****
 ******
>>> for i in range (1,6)
SyntaxError: invalid syntax
>>> for i in range (1,6):
	print("*"*i,end = "")
	print(' '*(10-i),end='')
	print("*"*i)

	
*         *
**        **
***       ***
****      ****
*****     *****
>>> for i in range (1,6):
	for i in range(1,i):
		print(i,end="")
	print("")

	

1
12
123
1234
>>> 