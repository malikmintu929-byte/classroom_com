# string
# concatenation+length

# str1="this is a string"

# print(len(str1))
# str2="we create it in python"

# print(len(str2))
# final_str= str1+ " " + str2
# print(final_str)
# print(len(final_str))
# # indexing
# str="mintu malik"
# print(str[5])\
#slicing :-
# str="mintu malik"
# print(str[:6])#[0:6]
# print(str[6:11])#[6:11]
# # negetive indexing:-
# print(str[-6:-2])#[5:9]
# staring function:-

# str="my name is mintu malik"
# print(str.endswith("lik"))
# str=str.capitalize()
# print (str)
# print(str.replace("mintu","RINTU"))
# print(str.find("m"))
# print(str.count("m"))
#wap  to  input user's name & print its length.
# str1=input("enter your name:")
# print(len(str1))
# print(str1)
#wap to  find the occurrence of 's' in a string.
# str1=" Hi, $iam the $ symbol $99.99 and $ is $used $ for $currency $ representation."
# print(str1.count("$"))
#conditional statements:-
# age= 16
# if( age >= 18):
#     print ("can vote and appliy for  driving")
# else:
#print("cannot vote and cannot apply for driving")
# light= input("enter the traffic light color:")
# if (light=="red"):
#     print("stop")#indentation
# elif (light=="yellow"):
#     print("wait")   
# elif (light=="green"):
#     print("go")
# else:
#         print("invalid color")
# grade student based on marks:-
# marks= int(input("enter your marks:"))
# if (marks>=90):
#     print("grade is", "A")
# elif(marks<90 and marks>=80):
#         print("grade is", "B")
# elif(marks>=70 and marks<80):
#         print("grade is", "C")
# elif(marks>=60 and marks<70):
#         print("grade is", "D")
# else:
#       print("fail")
# nesting:-
# age=30
# if(age>=18):
#     if(age>=31):
#        print ("can't vot")
#     else:
#         print("can vot")
# else:
#     print("can't vot")    
# wap a program  if a number entred by the user is odd or even .
# num= int (input("enter a number"))
# nam=num%2
# if (num==0 ):
#     print("the number is even")
# else:
#     print("the number is odd")
# wap to find the greatest of 3 num entered by the user:-
# num1=int(input("enter the first number"))
# num2=int(input("enter the second number"))
# num3=int(input("enter the third number"))
# if (num1>=num2 and num1>=num3 ):
#    print("num1 is greater",num1)
# elif (num2 >= num3 ):
#    print("num2 is greater",num2)
# else:
#     print("num3 is greater",num3)
    # wap to cheack if a num is a multiple of 7or not:-
x=int(input("enter the first number"))
if (x%7==0):
    print("multiple of 7 ")
else:
    print("not multiple of 7 ")
