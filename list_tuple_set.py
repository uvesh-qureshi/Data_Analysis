# list question:
# a=[1,2,3,2,4,5,6,7,8]
# for i in a:
#     if i==2:
#         a.remove(i)
# print(a)
        

# a=[1,2,3,8,9]
# b=[4,5,6]
# c=[]
# # print(a+b)
# for i in range(len(a)):
#     c.append(a[i])
#     if i<len(b):
#         c.append(b[i])
# print(c)

# a=[1,2,3]
# b=[4,5,6,7,8]
# c=[]
# # print(a+b)
# for i in range(len(b)):
#     if i<len(a):
#         c.append(a[i])
#     c.append(b[i])
# print(c)


# a=[1,2,3,4,5,6,7,8]
# max=a[0]
# for i in range(len(a)):
#    if max<a[i]:
#       max=a[i]
# print(max)

# a=[1,2,3,4,5,6,7,8,5,4,6,3,8]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)


a=[1,2,3,4,5,6,7,8]
b=[]
for i in range(len(a)):
    a.reverse(a[i])
    b.append(a[i])
print(b)

# a=[44,5,6,4,5,6,2,3,4,5,6,7,8,66]
# for i in range(1,int((len(a))/2)+1):
#     a[i-1],a[-i]=a[-i],a[i-1]
# print(a)

# a=[]
# for i in range(3):
#     b=[]
#     for j in range(3):
#         n=int(input("enter the number"))
#         b.append(n)
#     a.append(b)
# print(a)
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j],end="")
#     print()


# tuple question:
# tuple can't directly changed
# a=(2,3,4,5,6,7)
# b=list(a)
# b[2]=8765
# a=tuple(b)
# print(a)




# Set Questions:
# a={1,2,3}
# b={4,5,6}
# c={7,8,9}
# d=set()
# a.(b,c)
# # d=a
# print(a)

# fruits={"Apple","mango","banana"}
# fruits.add("orange")
# fruits.remove("banana")
# print(fruits)


# Iterate over set 
# fruits={"Apple","mango","banana","graphes","orange"}
# for i in fruits:
#     print(i)

# fruits={"Apple","mango","banana"}
# fruits.add("strawberry")
# fruits.remove("mango")
# print(fruits)

# remove item when it is present in the set 
# fruits={"Apple","mango","banana"}
# item_remove="orange"
# if item_remove in fruits:
#     fruits.remove(item_remove)
#     print(f"{item_remove} has been removed from the set")
# else:
#     print(f"{item_remove} is not present in set ")

# print(fruits)

# intersection of two set also used & for intersection
# a={1,2,3,4,5}
# b={4,5,6,7,8}
# c=a.intersection(b)  
# print(c)

# unoin of two set 
# a={1,2,3,4,5}
# b={4,5,6,7,8}
# c=a.union(b)  
# print(c)

# Difference of two set 
# a={1,2,3,4,5}
# b={4,5,6,7,8}
# c=b-a  
# print(c)

# symmetric difference : it is basically common chod kr baki sab dono set me 
# a={1,2,3,4,5}
# b={4,5,6,7,8}
# c=a.intersection(b) 
# d=a.union(b)
# e=d-c 
# print(e)

# a={1,2,3,4,5}
# b={4,5,6,7,8}
# c=a.symmetric_difference(b)
# print(c)


# a={1,2,3,4,5,7,8,}
# b={1,2,3,4,5,7,8,9}
# c=a.issubset(b)
# print(c)

# remove all the element
# a={1,2,3,4,5,7,8}
# a.clear()
# print(a)

# frozenset not be modify
# a=frozenset([1,2,3,4,5,7,8])
# b=frozenset([1,2,3,4,5,7,8,9])
# c=a&b
# print(c)

# a={1,2,3,4,5,7,8}
# max_value=max(a)
# min_value=min(a)
# print(max_value)
# print(min_value)

# fruits={"Apple","mango","banana"}
# item_p="orange"
# if item_p in fruits:
#     print(f"{item_p} has been removed from the set")
# else:
#     print(f"{item_p} is not present in set ")


# common element in two set 
# a={1,2,3,}
# b={1,2,3,4,5,6,7,8}
# if a.issubset(b):
#     print("a is superset of b")
# else:
#     print("a is not superset of b")


# find the element which is not present in another set 
# a={1,2,3}
# b={1,2,3,4,5,6,7,8}
# c=b.difference(a)
# print(c)

# a={1,2,3,9,10}
# b={1,2,3,4,5,6,7,8}
# c=a.intersection(b)
# a=a.difference(c)
# print(a)