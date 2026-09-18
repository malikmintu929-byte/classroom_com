# #  loop:
# #while loops:
# # while conditioin:
# # count=1
# # while count<=5 :
# #  print("hello world ",count)
# #  count+=1
# # # print number from one tom 5:
# # i=1
# # while i<=5:
# #  print(i)
# #  i+=1
# #  print ("loop ened")
# # revers:

# # i=5
# # while i>=1:
# #  print(i)
# #  i-=1
# #q1
# # i=1
# # while i<=10:
# #     print(i)
# #     i+=1

#     # q2
# # i=100
# # while i>=1:
# #     print(i)
# #     i-=1
# #q3
# # n=int(input("enter number"))
# # i=1
# # while i<=10:
# #     print(i*n)
# #     i+=1
#     #q4
# # i=1
# # while i<=10:
# #     print(i*i)
# #     i+=1
# #q4
# # num=[1,4,9,16,25,36,49,64,81,100]
# # idx=0
# # while idx <len(num):
# #     print(num[idx])
# #     idx+=1
# #q5
# # num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# # x = 36
# # i = 0

# # while i < len(num):
# #     if num[i] == x:
# #         print("Found at index", i)
# #         break
# #     else:
# #         print("finding ")
# #     i += 1
# # # continue:
# # i=0
# # while i<=10: #63,64,66,67,68,65
# #     if(i%2==0):
# #         i+=1
# #         continue # skip
# #     print(i)
# #     i+=1
# # for loop:
# # list=[1,2,3,4,5]
# # for  el in list:
# #     print(el)
# # tup=(1,2,4,5,6)
# # for  num  in tup:
# #      if(num == 5) :
# #        print("5 found")
# #        break
# #      print(num)

# # else:
# #      print("end")    
# #Q1 print the element  of following list using a loop:
# # list=[1,4,9,13,25,36,49,64,81,100]
# # for el in list:
# #     print(el)
# # Q2 search for anumber x in this tuple using loop:

# # nums=(1,4,9,16,25,36,49,64,81,49,36,100)
# # x = 49

# # idx = 0
# # for el in nums:
# #      if(el==x):
         
# #           print(" nums found  at idx",idx)
# #           print("element",el)
# #           break
# #      print(el)
# #      idx += 1
# # range: start from 0 and increase by +1:
# # seq= range(5)
# # for char in seq:
# #     print(char) 

# # for  i  in range(2,10,3):
# #     print(i)
# # for i in range(1,10,):
# #     if(i%2==0):
# #         print("the element",i)
# # for i in range(2,100,2):
#     # print(i)
# # Q1
# # for num in  range(1,101):
# #     print(num)
#     #q2
# # for num in  range(100,1,-1):
# # #   print(num)
# # for num in  range(1,11):
# #   print(num*10)
# #  # past statment: ( it is use when you want a null statement that does nothing . it is used as a  placeholder for future code.) for el, range(10): print(i)
# # for i in range(5):
# #    pass
# # print("mintu malik")
# #q4
# # num=int(input("enter a number:"))
# # i=1
# # sum=0
# # while(i<=num):
# #    sum=sum + i
# # #    i=i+1
# # # print("sum ",sum)
# # n=int(input("enter a number:"))
# # i=1
# # fact=1
# # while(i<=n):
# #    fact*=i
# #    i+=1

# # print("factorial",fact)  
# # n=int(input("enter a number:"))
# # fact=1
# # for i in range(1,n+1):
# #   fact*=i
# # print("fact=",fact)
# # loop:
# # i=1
# # while :
# #   print(i)
# #   i+=1b
# # list=[1, "mintu", True,"this", "rohan"]
# # i=0
# # while (i<len(list)):
# #     print(list[i])
# #     i+=1
# #for lopp:
# # list=(1,2,4,2,5,6,3,4)
# # for i in list:
# #     print(i)
# # s= "mintu malik"
# # for i in s:
# #     print(i) 
# # t=(1,2,4,2,5,6,3,4)
# # for item in t:
# #     print(item)
# # else :
# #     print("done")    # this is print when  the loop exhaust!
# # # break:
# # for i in range(1,100,2):
# #  if(i==81):
# #   break # exit the loop right now
# #  print(i)

# # for i in range(1,30,2):
# #   if(i==21):
# #    continue# skip this iteration
# #   print(i)  
# # list =[ "mintu", "ankit","sujoy","raj"]
# # for i in list:
# #  print(i)
# # pass# null satement
# # i=0
# # while(i<45):
# #    print(i)
# #    i+=1   
#    #q1
# # n =int(input("enter a num:"))  
# # for i in range(1,11):
# #     print(f"{n}x{i}={n*i}")# f= formatted str = (f"text{variable}")
# l= ["mintu","malik","ritam","rupomay","raj","sahbhu"]
# for name in l:
#     if(name.startswith ("m")):
#         print(f"hello{name}")

#q3
# n=int(input("enter  your number"))
# for i in range(2,n):
#  if (n%i)==0:
#       print ("the number is not  prime")
#       break
# else:
#   print("number is   prime")
#q4
# n=int(input("enter  your number"))
# sum=0
# for i in range(1,n): 
#  sum+=i
# print(sum)

# n=int(input("enter  your number"))
# fact=1
# for i in range(2,n+1):
#  fact=fact*n
# print(f"the fact{n} is {fact}")
#q7
# n=int(input("enter  your number"))
# for i in range(1, n + 1):
#  print(" " * (n - i), end="")
#  print("*" * (2 * i - 1), end="")
#  print(" ")
#q8
# n=int(input("enter your number"))
# for i in range(1, n + 1):
#  if(i==1 or i==n):
#     print("*"* n , end ="")
#  else:
#     print("*" , end ="")
#     print(" " * (n-2), end="")
#     print("*", end ="")
#  print("")
#  #q10
n=int(input("enter your number"))
for i  in range (11,0,-1):
   print(f"{n}x{i}={n*i}")

