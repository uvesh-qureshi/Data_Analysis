
# functions

# make a user define function for factorial
# def fact(num):
#     factorial=1
#     while num>=1:
#         factorial*=num
#         num=num-1
#     print(factorial)
    
# fact(10)



# create a function that takes two arguments a,b and return true if a,b are paliendrome 
# def check_pal(a,b):
#     if b==a[::-1]:
#         return True 
#     else:
#         return False
     
# print(check_pal("121","121"))


# def check_pal(num1, num2):
#     return str(num1) == str(num2)[::-1]

# result = check_pal(123, 321)
# print(result)  # True


# max of three number 
# def check_max(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c

# print(check_max(10,20,30))


# add all item in a list 
# def list_sum(nums):
#     sum=0
#     for i in nums:
#         sum+=i
#     return sum

# print(list_sum([1,2,3,4,5,6,7,8,9])) 


# multiply of all list item 
# def list_sum(nums):
#     mul=1
#     for i in nums:
#         mul*=i
#     return mul

# print(list_sum([1,2,3,4,5,6,7,8,9])) 


# reverse a string 
# def rev_string(word):
#     for i in word:
#         # return word[-1:-8:-1] 
#         return word[::-1] 
    
# print(rev_string("chandan"))

#for find the vowel in a string
# def str(a):
#     count=0
#     for i in a:
#         if i in "aeiou":
#             count+=1
#     return count
        
# print(str("chandan"))

# def max(num):
#     max=num[0]
#     for i in num:
#         if max<i:
#             max,i=i,max
#     return max

# print(max(num=[3,2,1,4,5,6,55]))


# w r p to create a funt two list as an argument and return true if the second list is shorted list of 1st list 
# def check_sort(a,b): or 
# def check_sort(a:list,b:list):
#     '''This function will check if the second list is sorted list of first one'''
#     a.sort()
#     if b==a:
#         return True
    
# print(check_sort([1,3,2,4],[1,2,3,4]))


# w a f that accept string as an argument and count the upper and lower case 
# def count(a):
#     '''this function is will count the upper and lower case in the given string'''
#     upper="QWERTYUIOPASDFGHHJKLZXCVBNM"
#     lower="qwertyuiopasdfghjklzxcvbnm"
#     countlower=0
#     countupper=0
#     for i in a:
#         if i in upper:
#             countupper+=1
#         elif i in lower:
#             countlower+=1
#     return countupper,countlower

# print(count("My name is Chandan"))



# find the factorial using Recursion 
# def factorial(n):
#     if n==0:
#         return 1
#     elif n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))


# print fabonacci series using recursion 
# def fibbinocci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     return fibbinocci(n-1)+fibbinocci(n-2)

# for i in range(11):
#     print(fibbinocci(i),end=" ")


# check the number lie in the given range 
# def test_range(n):
#     if n in range(1,9):
#         return ("%s is in the range"%str(n))
#     else:
#         return ("%s is not in range"%str(n))

# print(test_range(5))

# 2nd option
# def check_num(n,s,l):
#     '''This function is define the vale is present in the given range.
#     n-->Number which can you seach.
#     s-->Starting value of the range.
#     l-->Last value of the range.'''
#     return s<=n<=l if l>=s else l<=n<=s

# print(check_num(5,1,9)) 


# return a new list with distinct elements from a list 
# def distinct_element(a:list):
#     '''This function return a new list which element is distinct from a list.'''
#     x=[]
#     for i in a:
#         if i in x:
#             a.remove(i)
#         else:
#             x.append(i)
#     return x

# print(distinct_element(a=[1,1,2,2,3,4,4,4,3,2,2,2,5,6,7,8,9]))

# check no is prime or not
# def prime(a):
#     if a==1:
#         return False
#     else:
#         for i in range(2,a):
#             if a%i==0:
#                return False
#         return True
             
# print(prime(2))


# print even number from a given list 
# def distinct_element(a:list):
#     '''This function return thr new list which can store the even values in the given first list .'''
#     x=[]
#     for i in a:
#         if i%2==0:
#             x.append(i)

#     return x

# print(distinct_element(a=[1,1,2,2,3,4,4,4,3,2,2,2,5,6,7,8,9]))
     

# check if number is perfect i.e: 6// 6/1,2,3 and 1+2+3=6
# def perfect_num(n):
#     sum=0
#     for i in range(1,n):
#         if n%i==0:
#             sum+=i
#     return sum==n

# print(perfect_num(28))

# def check_pal(a:str):
#     '''this function is return true or false when the srting if palindrome'''
#     b=a[::-1]
#     if a==b:
#         return True 
#     # else:
#         return False
     
# print(check_pal("chahc"))

# 13. pascal triangle




# 14. check whether a string is a pangram or not
# import string

# def is_pangram(sentence):
#     alphabet = set(string.ascii_lowercase)
#     sentence_letters = set(sentence.lower())
#     return alphabet <= sentence_letters

# print(is_pangram("The quick brown fox jumps over the pink lazy dog"))



# 15. sort hyphen-separated sequence of words alphabetically
# items =[ n for n in input("enter hyphen-separated sequence").split('-')]
# items.sort()
# print('-'.join(items))


# 16. create a list of square of 1 to 30
# def square_list():
#     result=[]
#     for i in range(1,31):
#         i=i**2
#         result.append(i)
#     return result

# print(square_list())


# 17. bold italic underline
# def bold(fn):
#     def wrapped():
#         return "<b>"+fn()+"</b>"
#     return wrapped

# def italic(fn):
#     def wrapped():
#         return "<i>"+fn()+"</i>"
#     return wrapped

# def underline(fn):
#     def wrapped():
#         return "<u>"+fn()+"</u>"
#     return wrapped

# @bold
# @italic
# # @underline
# def hello():
#     return "Hello world"

# print(hello())


# count the local variable decleared in the program.
# def fun():
#     a=1
#     b=2
#     c=a+b
#     return c 

# no_locals=fun.__code__.co_nlocals
# print("number of local variable in the function:",no_locals)

 
#Tower of hanoi

# decorator -- it is a function that takes argumrnt as function and return values as function 
def main(func):
    def opr():
        print("this is a rapper function class")
        func()
        print("we are learning decorator")
    return opr





# lambda 
# a=[1,2,3,4,5,6,7,8]
# b=list(filter(lambda x:x%2==0,a))
# print(b)


a=[1,2,3,4,5,6,7,8]
a=[x for x in a if x%2==0]
print(a)


# map 
a=[1,2,3,4,5,6,7,8,9]
b=list(map())