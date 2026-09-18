# list and tuple:-
marks=[94.5,98.7,65.5,78.5]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))

# student list:-

student =["mintu",98.5,17, "kolkata"]
print(student)
print(student[0])
student[0]="malik"
print(student)
# list slicing:-
marks=[94.5,98.7,65.5,78.5]
print(marks[1:3])
print(marks[:3])
print(marks[1:])
print(marks[-3:-1])# 1st element not print 
# # # list method:
#  #1 sdding method:-
list=[1,2,4,5]
list.append(6) # adds one element at the end
print(list)
print(list.sort ())#sorts  in ascending order
print(list)
list.sort(reverse=True ) #sort in  decending order
print(list)
list=[1,2,4,8,7]
list.reverse()# reverses list
print(list)
list.insert(0,"mintu") #insert element at index

print(list)
# remove method:
list=[1,2,4,8,7]
list.remove(2) #removes first occurence of element 
print (list)
list.pop(0) # removes elements at idx
print(list)
# # tuples method:-
# #( a built - in data type that lets us creat immulate sequence of valus)
# # list use [] and tuples use ()
tup=(1,2,4,8,3,2,2,7)
print(tup)
print(type(tup))
print (tup[2])
# tup(5)=0  not allow becaes its  not assign any addition
tup=(1,) # if we not give , after int value then  this print  like a int
print (tup)
print ( type(tup))
print(tup.index(2))  # returns index of first occurrence
print (tup.count(2)) # count total occurrence

# # # Q1 WAP RO ASK THE USER  TO  enter names of 3 movies & store them in a list.
list=[] #list=move
str1= input("enter 1st move")
print (str1)
str2= input("enter 2st move")
print(str2)
str3= input("enter 3st move")
print(str3)

list.append(str1)
list.append(str2)
list.append(str3)
print(list)

#q2 wap to cheack if a list contains a palindrome of element .(hint use  copy() methode) 
list1=[1,2,3,2,1]

copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print ("pallandrom")
else:
    print("not")
list1=[1,2,2,3,2,1]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print ("pallandrom")
else:
    # print("not")

 # wap to count the number of student  with the"A" GRADE IN THE FOLLOWING  tuple:
 students= ("c","d","a","a","b","b","a")
print(students.count("a"))
# store the above value in a list them from "a to "d":
students= ["c","d","a","a","b","b","a"]
print(students.sort())
print (students)
#  q1:List Creation:Create a list containing 5 integers and print all the element:
list=[1,2,3,4,5]
print(list)
# #  #q2Indexing:
#  Given numbers = [10, 20, 30, 40, 50], print the first, third, and last elements:
num=[10,20,30,40,50]
print(num[0])
print(num[2])
print(num[4])
# #q3 List Methods:
# # Create a list and demonstrate the use of append(), insert(), remove(), and pop().
list =[1,2,3,5,4,6,7]
print(list.append(8))
print (list)
print(list.insert(0,9))
print(list)
print(list.remove(9))
print (list)
print(list.pop(5))
# # # q4 (List Methods:Slicing:)
# Given numbers = [1, 2, 3, 4, 5, 6, 7, 8], print:
# # First 4 elements
# # Last 3 elements
# # Elements from index 2 to 5 :

list =[1,2,3,5,4,6,7]
print(list[0:4])
print(list[4:])
print(list[2:5])
print(list)
# # #Q5 Sum & Maximum:
# # Write a program to find the sum, maximum, and minimum value from a list.
# # 
list=[10,20,23,40,50,60,]
print(sum(list))
print(max(list))
print(min(list))
print(list)
# #q 6Mixed Data Types:
# # Create a list containing an int, float, string, and boolean. Print each element and its data type.
list=[20,54.2,"mintu", True]
for x in list:
    print( x,type (x))
print(list) 
# #q7 (Tuple Creation:
# # Create a tuple containing 5 numbers and print its elements using a for loop.):-
num=(1,5,7,8,6)
for  list in num:
    print(list) 
#     #(q8uple Methods:
# # Given t = (10, 20, 30, 20, 40, 20), find:
# # Number of times 20 occurs
# # Index of the first 20):-
    t=(10,20,30,20,40,20)
    print(t.count(20))
    print(t.index(20))
#     #q9 ist → Tuple:
# #() Create a list of 5 elements and convert it into a tuple. Then convert the tuple back into a list.):-
    num=[1,5,7,8,9]
t=tuple(num)
print( t)
print(num)



