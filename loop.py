'''n = int(input("enter the number"))
i = 1
while(i<=10):
    print(n,"x",i, "=",n*i)
    i = i+1'''
'''n = int(input("enter the number"))
for i in range(1,11):
    print(n*i)'''
'''n = int(input("enter the number"))
fact=1
while n>=1:
    fact=fact*n
    n=n-1
# print("the efactorial is ",fact)'''

# Print 10 natural number
# for i in range(11):
#     print(i)

# 10 Even number
# for i in range(2,21,2):
#     print(i)
    
# 10 odd number
# for i in range(1,21,2):
#     print(i)

# backword 10 even number
# for i in range(20,1,-2):
#     print(i)

# print table 
# num=int(input("Enter the number for table: "))
# for i in range(1,11):
#     print(num,"X",i,"=",num*i)

# num=int(input("Enter the number: "))
# p=1
# while(num):
#     r=num%10
#     p=p*r
#     num=num//10
# print("The product of digit is:",p)


#factorial of number
# num=int(input("Enter the number for factorial"))
# fac=1
# for i in range(1,num+1):
#     fac=fac*i
# print("factorial is:",fac) 


#factorial of number
# num=int(input("Enter the number for factorial"))
# fac=1
# i=1
# while i<=num:
#     fac=fac*i
#     i=i+1
# print(fac)


# prime number
# num=int(input("Enter the number"))
# count=0
# if num==0 or num==1:
#     count=1
# for i in range(2,num):
#     if num%i==0:
#         count=1
# if count==1:
#     print("this is not prime number")
# else:
#     print("this is prime number")


# print pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4 
# 1 2 3 4 5
# no=int(input("Enter the for print the pattern"))
# for i in range(1,no+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

# * * * * * 
# * * * *
# * * *
# * *
# *
# no=int(input("Enter the for print the pattern"))
# for i in range(no,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# Accept 10 number from user and calculate their average
# sum=0
# for i in range(10):
#     no=int(input("Enetr ten numbers: "))
#     sum=sum+no
# print("The average of given number is: ",sum/no)


# Prime number between two number which is input from user



# print sum of odd number and sum of even number between 12 and 39 // user input
# num1=int(input("Enter the first number"))
# num2=int(input("Enter the last number")) 
# so=0
# se=0
# for i in range(num1,num2+1):
#     if i%2==0:
#         se=se+i
#     else:
#         so=so+i
# print("Sum of odd number: ",so)
# print("Sum of even number: ",se)


# divisible by 11 and  not by 2 between 100 to 500
# for i in range(100,500):
#     if i%11==0 and i%2!=0:
#         print("Number which is divisible by 11 but not divisible by 2:",i)
#         i=i+1


# Number not divisible by 2 and  not by 3 between 1 to 20
# for i in range(1,20):
#     if i%2!=0 and i%3!=0:
#         print("Number which is divisible by 2 but divisible by 3:",i)
#         i=i+1


# print the table
# num=int(input("Enter the number for print the table: "))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)


# take input from user until user enter zero then display the sum and average of all number
# sum=0
# n=1
# i=-1
# while n!=0:
#     n=int(input("Enter the number when you stop enter then press 0: "))
#     sum=sum+n
#     i=i+1
# print("The sum of all number is: ",sum)
# print("The average of all number is: ",sum/i)

# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# n=int(input("Enter the number for print the pattern: "))
# for i in range(n,0,-1):
#     for j in range(i):
#      print(i,end=" ") 
#     print()

# for i in range(1,6):
#     for j in range(6-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         if j==0 or j==2*i-2:
#             print("*",end="")
#         else:
#             print(" ",end="")

#     print()

# * * * * *
# * * * * *
# * * * * *
# * * * * * 
# n=int(input("enter the row of pattern"))
# for i in range(n):
#     for j in range(n):
#         print('*',end=' ')
#     print()

# *
# * *
# * * *
# * * * *
# n=int(input("enter the row of pattern"))
# for i in range(n):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()

# * * * *
# * * *
# * *
# *
# n=int(input("enter the row of pattern"))
# for i in range(n):
#     for j in range(i,n):
#         print('*',end=' ')
#     print()

#       *
#     * *
#   * * *
# * * * *
# n=int(input("enter the row of pattern"))
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=' ')
#     print()


# for i in range(1,6):
#     for j in range(6-i):
#         print("",end=' ')
#     for j in range(i):
#         if j==0 or j==i-1 or i==0 or i==5:
#             print("*")
#         else:
#             print("")
# print()


# print even number using list
# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,1,19,20]
# for i in range(len(a)):
#     if a[i]%2==0:
#        print(a[i])



# /\
# \/
# n=10
# while n>5:
#     for i in range(1,int(n/2)):
#         for j in range(int(n/2)-i):
#             print(" ",end="")
#         for k in range(2*i-1):
#             if k==0 or k==2*i-2:
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#         print()
#     break
#     n=n-1
# while n-5>=1:
#     for i in range(2,int(n/2)):
#         for j in range(i):
#             print(" ",end="")
#         for k in range(2*int(n/2)-2*i-1):
#             if k==0 or k==2*int(n/2)-2*i-2:
#                 print("*",end="")
#             else:
#                 print(" ",end="")  
#         print()
#     break
#     n=n-1

# print A
# n=6
# for i in range(n):
#     for j in range(n):
#         if (i==0 and j==0) or (i==0 and j==n-1):
#             print(" ",end="")
#         elif i==0 and 1<=j<n:
#            print("*",end="")
#         else:
#             if j==0 or j==n-1:
#                 print("*",end="")
#             elif i==3:
#                print("*",end="")
#             else:
#                 print(" ",end="")
#     print()


# print B
# n=9
# for i in range(n):
#     for j in range(n):
#         if (i==0 and j>=n-4) or (i==n-1 and j>=n-4) or (i==4 and j>=n-4):
#             print(" ",end="")
#         else:
#             if (1<=i<=3 and 0<j<n-1) or (5<=i<=7 and 0<j<n-1):
#                 print(" ",end="")
#             else:
#                 print("*",end=" ")
        
#     print()

# print C
# n=9
# for i in range(n):
#     for j in range(n-4):
#         if (i==0 and j==0) or (i==n-1 and j==0):
#             print(" ",end="")
#         else:
#             if (i==0 or i==n-1) or (j==1):
#                 print("*",end=" ")
#     print()


# print D
# n=9
# for i in range(n):
#     for j in range(n):
#         if (i==0 and j>=n-5) or (i==n-1 and j>=n-5):
#             print(" ",end="")
#         else:
#             if (0<i<n-1 and 0<j<n-1):
#                 print(" ",end="")
#             else:
#                 print("*",end=" ")
#     print()


# progran for find divisible by 7 and 5 between 1500 and 2700
# for i in range(1500,2700):
#     if i%7==0 and i%5==0:
#         print(i)

# program temperature converter Fehranit into celcius and celcius into fehranit
# n=int(input("Enter the temperature for convert"))
# t=input("Conert into celsius (C) or Fehranit (F)")
# if t.upper()=='F':
#     print("Convertion into fehranit is: ",(n-32*5/9))
# elif t.upper()=='C':
#     print("Convertion into celsius is: ",(9*n)/5+32)

# guess game
# import random
# target,guess=random.randint(1,10),0
# while target != guess:
#     guess=int(input("Guess the number between 1 to 10 until you get it right: "))
# print("You guess the correct number")

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# n=5
# for i in range(n):
#     for j in range(i):
#         print("*",end=" ")    
#     print()
# for i in range(n,0,-1):
#     for j in range(i):
#         print('*',end=' ')
#     print()


# input a word and reverse it 
# word=input("Enter the woed wich you can reverse: ")
# for char in range(len(word)-1,-1,-1):
#     print(word[char],end="")
# print()


# find odd even in tuple
# number=(1,2,3,4,5,6,7,8,9,10)
# se=0
# se_count=0
# so_count=0
# so=0
# for x in number:
#     if  x%2==0:
#         se_count+=1
#         se=se+x
#     else:
#         so_count+=1
#         so=so+x
# print("Odd number is: ",so_count)
# print("Sum of odd number is: ",so)
# print("Even number is: ",se_count)
# print("sum of even number is: ",se)


# find the type of all list item
# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
# for i in datalist:
#     print("type of",i ,"is" ,type(i))



# enter no 0 to 6 and print without 3 and 6
# for i in range(1,6):
#     if i==3 :
#         continue
#     print(i, end=" ")


# fibonacci series 
# n=50
# a=0
# b=1
# print(a,b,end=" ")
# for i in range(2,n):
#     c=a+b
#     if c>50:
#         break
#     print(c,end=" ")
#     a=b
#     b=c


#fizzbuzz when no%3 fizz when no%5 buzz and both fizzbuzz
# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print("fizzbuzz",i)
#     elif i%3==0:
#         print("fizz",i)
#     elif i%5==0:
#         print("buzz",i)

# num=int(input("enter any number"))
# l=[]
# for j in range(1, num+1):
#     while(j):
#         r=j%2
#         l.append(r)
#         j=j//2
       
       
# for i in range(len(l)-1,-1,-1):
#     print()
#     print(l[i])


# making matrix of 2D array
# row=int(input("Enter the number of rows"))
# col=int(input("Enter the number of column"))
# mul_list= [  [0 for col in range(col)] for row in range(row) ]
# for row in range(row):
#     for col in range(col):
#         mul_list[row][col]=row*col
# print(mul_list)

# Create an empty list named 'lines'
# lines = []
# while True:
#     l = input()
#     if l:
#         lines.append(l.upper())
#     else:
#         break
# for l in lines:
#     print(l) 
	


#input a string and count the word ans digit in the string
# s = input("Input a string")
# d = l = 0
# for c in s:
#     if c.isdigit():
#         d = d + 1
#     elif c.isalpha():
#         l = l + 1
#     else:
#         pass
# print("Letters", l)
# print("Digits", d)


# write a program to 
# for i in range(1,6):
#     for j in range(i):
#         print(i,end=" ")
#     print()
    

#print X
# n=7
# for i in range(n):
#     for j in range(n-3):
#         if (i<=1 and j<=0) or (i>=n-2 and j==n-4) or (i<=1 and j==n-4) or (i>=n-2 and j==0) or(i==2 and j==1) or(i==2 and j==2) or (i==3 and j==2) or(i==4 and j==1) or (i==4 and j==2):
#             print("*",end=" ")
#         else:
#             print(" ",end="")
#     print()
    

# q pattern
# n=9
# for i in range(n):
#     for j in range(n):
#         if (i==0 and j==0):
#             print(" ",end="")
#         else:
#             print("*",end=" ")
#     print("")


# n=25
# for i in range(n-16):
#     for j in range(n):
#         if (i==2 and j==0) or(i==1 and j==0) or (i==0 and j<=3):
#             print(" ",end=" ")
#         else:
#             print("*",end="")
#     print("")


# n=25
# for i in range(n-16):
#     for j in range(n):
#         if (i==0 and j<=2) or (i==1 and j<=1) or (i==2 and j==0) or (i==1 and j==3) or (i==2 and 1<j<5) or (i==0 and 3<j>14):
#             print(" ",end="")
#         else:
#             print("*",end=" ")
#     print("")


# a=[2,3,4,5,6,7,8,9]
# a=[x**2 for x in a ]
# print(a)





