print('fjfjfjpytho')

# def decore(num):
#     def inner():
#         print('inner function')
#         num()
#         print('after inner')
#     return inner

# @decore
# def num():
#     print('we will use this function')
#     print('fiwufwejeofj')

# num()


# def decore(num):
#     def inner():
#         a =num()
#         add = a*5
#         return add
#     return inner

# @decore
# def num():
#     return 10        

# print(num())

# class Student():
#     def __init__(self):
#         print('nffjifjifj')
#     def __init__(self,x):
#         print('mffjjjgjgj')  

#     def __init__(self,x,y):
#         print('mffjjjgjgj')      
# # s=Student('ijfj')
# Student('hh','fjifj')

# class Test:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
#     def a(self):
#         self.marks=60
# test=Test('raj',60)
# test.a() 
# test.age=60
# # test.marks=80
# # print(test.__dict__)       

# class Test:
#     a=10
#     def __init__(self):
#         self.a=20
# t= Test()
# print(t.a,Test.a)       
# 
#  
# class Test:
#     def setName(self,name):
#         self.name=name     
#     def getName(self):
#         return self.name 
# t =Test()
# t.setName('raj')
# print(t.getName(),'kumar')              
        

# def dec_fucn(myfunction):
#     def wrapper():
#         print('reuihhgh')
#         myfunction()
#     return wrapper

# @dec_fucn
# def test():
#     print('ehruhgurhegh')
# test()    


# def add(myfunction):
#     def aa():
#         b=myfunction()
#         b=b*5
#         return b    
#     return aa
# @add
# def test1():
#     return 5
# print(test1())    


# Python program to convert
# JSON file to CSV
 
# Python program to convert
# JSON file to CSV


# import json
# import csv


# # Opening JSON file and loading the data
# # into the variable data
# with open('data.json') as json_file:
# 	data = json.load(json_file)

# employee_data = data['employee_details']

# # now we will open a file for writing
# data_file = open('data_file.csv', 'w')

# # create the csv writer object
# csv_writer = csv.writer(data_file)

# # Counter variable used for writing
# # headers to the CSV file
# count = 0

# for emp in employee_data:
# 	if count == 0:

# 		# Writing headers of CSV file
# 		header = emp.keys()
# 		csv_writer.writerow(header)
# 		count += 1

# 	# Writing data of CSV file
# 	csv_writer.writerow(emp.values())

# data_file.close()


# x= lambda a,b,c:a+b+c
# print(x(2,4,6))

# y= lambda a,b:a*b
# print('area of rectangel',y(2,4))



# SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
#             1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

# def approximate_size(size, a_kilobyte_is_1024_bytes=True):
   
#     if size < 0:
#         raise ValueError('number must be non-negative')

#     multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
#     for suffix in SUFFIXES[multiple]:
#         size /= multiple
#         if size < multiple:
#             return '{0:.1f} {1}'.format(size, suffix)

#     raise ValueError('number too large')

# if __name__ == '__main__':
#     print(approximate_size(100, False))
#     print(approximate_size(1000000000000))


value_of_user = input('Enter you input:')
aa= value_of_user.split()
a= ' '.join(aa[::-1])
print(a)

list =[]
for i in aa:
    list.append(i[::-1])
b=''.join(list)
print(b)