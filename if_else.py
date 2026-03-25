# 1. Eligible or not for vote
# age=int(input("Enter youe age"))
# if age>=18:
#     print("Eligible for vote")
# else:
#     print("Not eligible for vote")


# 2. Even or Odd
# no=int(input("Enter any number"))
# if no%2==0:
#     print("NO is Even")
# else:
#     print("No is Odd")


# 3. Check no is divisible by 7 or not
# num=int(input("Enter any number"))
# if num%7==0:
#     print("number is divisible by 7")
# else:
#     print("number is not divisible by 7")


# 4. Display hello when entered no is multiple by 5 otherwise Bye 
# num=int(input("Enter any number"))
# if num%5==0:
#      print("Hello")
# else:
#      print("Bye")

# 5. calculate electricity bill
# amount=0
# nu=int(input("Enter the electricity unit"))
# if nu<=100:
#     amount=0
# if nu>100 and nu<=200:
#     amount=(nu-100)*5
# if nu>200:
#     amount=500+(nu-200)*10
# print("Amount to pay",amount)


# 6. print the last digit of number
# num=int(input("Enter any number"))
# num=num%10
# print("number last disit",num)


# 7. check the last no of digit is divisible by 3 or not
# num=int(input("Enter any number"))
# num=num%10
# if num%3==0:
#     print("The last number of digit is divisible by 3")
# else:
#     print("The last number of digit is not divisible by 3")


# 8. Grade for marks
# nu=int(input("Enter the Marks"))
# if nu>90:
#     print("Grade:A")
# if nu>80 and nu<=90:
#     print("Grade:B")
# if nu>60 and nu<=80:
#     print("Grade:C")
# if nu<=60:
#     print("Grade:D")

# 9. calculate tax according to user price
# tax=0
# prise=int(input("Enter the prise of bike"))
# if prise>100000:
#     tax=(prise*15)/100
# if prise>50000 and prise<=100000:
#     tax=(prise*10)/100
# if prise<50000:
#     tax=(prise*5)/100
# print("Tax to pay",tax)


# 10. leap year or not
# year=int(input("Enter the year"))
# if year%4==0:
#     print("This is leap year")
# else:
#     print("This is not leap year")

# Days select from number 
# num=int(input("Enter the number between 1 to 7: "))
# if num==1:
#     print("Monday")
# if num==2:
#     print("Tuesday")
# if num==3:
#     print("wednesday")
# if num==4:
#     print("Thurday")
# if num==5:
#     print("ftriday")
# if num==6:
#     print("Saturday")
# if num==7:
#     print("Sunday")
# if num>7:
#     print("Please enter the number between 1 to 7")


# Months select form input by user 1 to 12
# num=int(input("Enter the number between 1 to 12: "))
# if num==1:
#     print("January and no. of days is 31")
# elif num==2:
#     print("February and no.of days is 28")
# elif num==3:
#     print("March and no.of days is 31")
# elif num==4:
#     print("April and no.of days is 30")
# elif num==5:
#     print("May and no.of days is 31")
# elif num==6:
#     print("June and no.of days is 30")
# elif num==7:
#     print("July and no.of days is 31")
# elif num==8:
#     print("August and no.of days is 31")
# elif num==9:
#     print("September and no.of days is 30")
# elif num==10:
#     print("Octuber and no.of days is 31")
# elif num==11:
#     print("November and no.of days is 30")
# elif num==12:
#     print("December and no.of days is 31")
# else:
#     print("Please select number between 1 to 12")


# Enter no is three digit or not
# num=(input("Enter the Digit: "))
# l=len(num)
# if l==3:
#     print("The enter number is three digit ")
# else:
#     print("The enter number is not three digit")


# Eligible for voting or not
# age=int(input("Enter the age: "))
# if age>=18:
#     print("Eligible for vote")
# else:
#     print("Not eligible for vote")


# Senior citizen or not
# age=int(input("Enter the age: "))
# if age>=60:
#     print("Person is senior citizen")
# else:
#     print("Person is not senior citizen")


# find lowest number between two user input
# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))
# if num1>num2:
#     print("The lowest number is: ",num2)
# else:
#     print("The lowest number is: ",num1)


# find largest number between two user input
# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))
# if num1>num2:
#     print("The largest number is: ",num1)
# else:
#     print("The largest number is: ",num2) 


#find the entered number is positive or negative
# num=int(input("Enter the number: "))
# if num>0:
#     print("Number is positive")
# elif num==0:
#     print("Numnber is zero")
# else:
#     print("Numebr is negative")


# Even or Odd
# num=int(input("Enetr the Number: "))
# if num%2==0:
#     print("Number is Even")
# else:
#     print("Numebr is Odd")


# enter numebr is divisible by 2 and 3 both or not
# num=int(input("Enter the number: "))
# if num%2==0 and num%3==0:
#     print("Enter number is divisible by 2 and 3 both") 
# else:
#     print("Enter number is not divisible by 2 and 3 ") 


#find the largest number between three number 
# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))
# num3=int(input("Enter the third number: "))
# if num1>num2 and num1>num3:
#     print("The largest number is: ", num1)
# elif num2>num3 and num2>num1:
#     print("The largest number is: ", num2)
# elif num3>num2 and num3>num1:
#     print("The largest number is: ", num3)


# number is prime or not
# count=0
# num=int(input("Enetr the number: "))
# if num==0 or num==1:
#     count=1
# for i in range(2,num):
#     if num%i==0:
#         count=1
# if count==1:
#     print("Numebr is not prime")
# else:
#     print("Number is prime")


# check charecter is vowel or not using .lower function
# ch=input("Enter any character: ")
# ch.lower()=="aeiou"
# if ch.lower():
#     print("Enter character is vowel")
# else:
#     print("Enetr character is not vowel")



# check charecter is vowel or not
# ch=input("Enter any character: ")
# vow="aeiouAEIOU"
# if ch in vow:
#     print("Enter character is vowel")
# else:
#     print("Enetr character is not vowel")


# Percentage into grade
# per=int(input("Enter the percentage: "))
# if per>80:
#     print("Grade A+")
# elif per<=80 and per>60:
#     print("Grade A")
# elif per<=60 and per>50:
#     print("Grade B+")
# elif per<=50 and per>45:
#     print("Grade B")
# elif per<=45 and per>25:
#     print("Grade C")
# elif per<25:
#     print("Grade D")


# according to their service time give the bonus
# service=int(input("Enter the time period of service "))
# salary=int(input("Enter the salary"))
# if service>10:
#     b=10/100*salary
# if service>6 and service<=10:
#     b=6/100*salary
# if service<5:
#     b=5/100*salary
# print("Bonus is: ",b)


#calculate net amount(Marked amount-Discount)
# na=0
# d=0
# mp=int(input("Enetr the price: "))
# if mp>10000:
#     d=20/100*mp
# if mp>7000 and mp<=10000:
#     d=15/100*mp
# if mp<=7000:
#     d=10/100*mp
# na=mp-d
# print("The final price to pay: ",na)    


# take two input and operator form user and solved them
# num1=int(input("Enter the first digit: "))
# num2=int(input("Enter the second digit: "))
# op=input("Enter the operator ")
# if op=='+':
#     print("Your Answer is: ",num1+num2)
# if op=='-':
#     print("Your Answer is: ",num1-num2)
# if op=='*':
#     print("Your Answer is: ",num1*num2)
# if op=='/':
#     print("Your Answer is: ",num1/num2)
# if op=='%':
#     print("Your Answer is: ",num1%num2)
# if op=='**':
#     print("Your Answer is: ",num1**num2)
# if op=='//':
#     print("Your Answer is: ",num1//num2)


#accept age sex day and give the wages per day
# age=int(input("Enter the age"))
# sex=(input("Enter sex(M/F)"))
# nd=int(input("enter the number days"))
# if age>=18 and age<30 and sex.upper()=='M':
#     amt=nd*700
#     print("Amount is",amt)
# elif age>=18 and age<30 and sex.upper()=='F':
#     amt=nd*750
#     print("Amount is",amt)
# elif age>=30 and age<40 and sex.upper()=='M':
#     amt=nd*800
#     print("Amount is",amt)
# elif age>=30 and age<40 and sex.upper()=='F':
#     amt=nd*850
#     print("Amount is",amt)
# else:
#     print("enter appropriate age")


# print second largest number in three numebr
# num1=int(input("Enter the first number"))
# num2=int(input("Enter the second number"))
# num3=int(input("Enter the third number"))
# if (num1>num2 and num1<num3)or(num1>num3 and num1<num2):
#     print("The second largest number is: ",num1)
# if (num2>num3 and num2<num1)or(num2>num1 and num2<num3):
#     print("The second largest number is: ",num2)
# if (num3>num2 and num3<num1)or(num3>num1 and num3<num2):
#     print("The second largest number is: ",num3)

# accept three sides and check triangle is posible or not
# s1=int(input("Enter the first side of triangle"))
# s2=int(input("Enter the second side of triangle"))
# s3=int(input("Enter the third side of triangle"))
# if (s1+s2>s3 and s2+s3>s1 and s3+s1>s2):
#     print("The triangle is posible")
# else:
#     print("Triangle is not posible")


# calculate electricity bill
# un=int(input("Enter the unit of your bill: "))
# if un<=100:
#     am=0
# if un>100 and un<=300:
#     am=2*(un-100)
# if un>300:
#     am=400+(un-300)*5
# print("The total amount is: ",am)


# library charges to days
# day=int(input("Enter the days: "))
# if day<=5:
#     ch=day*2
# if day>=6 and day<=10:
#     ch=10+(day-5)*3
# if day>=11 and day<=15:
#     ch=25+(day-10)*4
# if day>15:
#     ch=45+(day-15)*5
# print("The total amount is: ",ch)


# library charges to days
# day=int(input("Enter the days: "))
# if day<=5:
#     ch=day*2
# if day>=6 and day<=10:
#     ch=day*3
# if day>=11 and day<=15:
#     ch=day*4
# if day>15:
#     ch=day*5
# print("The total amount is: ",ch)


# accept killometer calculate bill
# km=int(input("Enter killometer"))
# if km<=10:
#     ch=km*11
# if km>10 and km<=100:
#     ch=110+(km-10)*10
# if km>100:
#     ch=1010+(km-100)*9
# print("The charges is",ch)


# Accept marks and suggest for stream
# eng=int(input("Enter the English marks"))
# sci=int(input("Enter the Science marks"))
# mat=int(input("Enter the Maths marks"))
# sst=int(input("Enter the social Science marks"))
# if eng>80 and sci>80 and mat>80 and sst>80:
#     print("You are able to choose Science stream ")
# elif eng>80 and sci>50 and mat>50:
#     print("You are able to choose Commerce stream ")
# elif eng>80 and sst>80:
#     print("You are able to choose Humanites stream ")
# else:
#     print("you score less")

