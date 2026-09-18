#dictionary 
# 1
# dict={
#     "name": "mintu malik",
#     "age": 19,
#     "class": "1st year",
#     "marks": 98

# }
# # dict["roll"]= 60
# # dict["name"]="rintu malik"
# print(type(dict))
# print(dict)
# del dict["age"]
# print(dict)
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# for key,value in  dict.items():
#     print(key,":", value)
# if "age" in dict:
#         print("key exists")
# else:
#     print("key not exists")
marks={
          "pysics":98,
          "chemistry": 85,
          "math":98,
          "biology":87

       
 }
total=sum(marks.values())
print("total:",total)