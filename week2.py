# single equal sign is for assignment

# string
#string means content in python
#String need quote
#Single double triple quote

tic='QAN.AX'
tic2="A"
tic3='''Be 
5'''  #can use in the contant that has multiple line
tic4="""Careful
3"""  #can use in the contant that has multiple line
print(tic,tic2)
print(tic3)
print(tic4)

#print a sentence with quote
str1='''He said to me,"I love Python"'''
str2="""He said, " I love my mom."""""
str3="He said to me,\"I love u\"."
str4='John said:"Let\'s learn python together".'
print(str1)
print(str2)
print(str3)
print(str4)

#int, float
a=1 #This is an integer of value 1
b=1.0 #This's a float of value 1
c=-1 #This's an int of value -1
d=1. # float
print(a,b,c)
print(type(a),type(b),type(c),type(d))


#devide will cause float, this process called "casting"
a=4/2
print(a)
print(type(a))


#integers can be compared directly
i=1
test=i==1
print(test)  #-->True  boolean-1st letter will be capital
test=i==2
print(test)
test=i<2
print(test)

# == compare
#!!!!careful when compare with float
f=0.2+0.2+0.2
print(f==0.6)   #-->False
print(f) #will give a numb with 16 decimal point

f=0.2+0.2
print(f==0.4) #this time it can generate the right answer
print(f)

#way to compare float - math.isclose
import math  #import 'math' package 1st
f=0.2+0.2+0.2
print(math.isclose(f,0.6))


#Booleans / bool
x=True
y=False
print(type(x),type(y))

#bool's 1st letter always been cap
# x=true
# print(type(x)) will occur 'NameError'

#double equal sign(==) is for comparing objects
1==2
2==2
print(1<2)
print(2<2)
print(2<=2)

# "not" to flip "True" to "False" and vice versa
not True #become False
not False #become True

# "and" to check both bools are "True"
True and True # T
True and False # F
False and True # F
False and False # F

# "or" to check at least 1 bool is "True"
True or True # T
True or False # T
False or True # T
False or False # F



#The NoneType
# None represents a null value, that's it
# operation between "None" and other basic types is not permitted
#2+None  #TypeError

# Primitive Types: str, int, float, bool, None

x=1
print(type(x))

xstr='1'
print(type(xstr))

test= x==xstr
print(test)
print(type(test))

#relation between types and classes
print(3+2) #5
print('3'+'2') #32

a='3'+'2'
print(type(a)) #str

print("1"+"1"+"1") # 111
print("2"*2) # 22 repeat 2 twice
print('x'*2) # xx



#Attribute: a value associated with an object be referenced by name using dot
#yfinance.download, download is a method in class<yfins>
#download is a function defined by yfinance

#every time import package will shows new class


#Namespaces: a place where variables are defined
x=1 #This is namespace, called global here
print(x)

#print(x)
#x=1  #NameError

print #no error, cause it is a buildin function
#1st see whether there's a variable called print; if not a buildin function/method, it will shows error
#e.g. ABC will cause error


x='abc'
x=str('abc') #is equivelant with the front
print(x)


#upper
#upper(x) #NameError: name 'upper' is not defined. Not a build-in function
#access <upper> method in <str> class
x=str('abc')
xup=str.upper(x)  #upper function belongs to str class    1st upper methond
print(xup)
print(str.lower(xup))  #lower fuction

y='abc'.upper()  #2nd upper method
print(y)
print('ABC'.lower()) #lower fuction


weird_case="My fUnNy tYpEcAsE sTrInG"
weird_case_lower=weird_case.lower()
print(weird_case_lower)

weird_case_upper=weird_case.lower().upper()
print(weird_case_upper)



#center the word "Hi" in a line of 40 character
"Hi".center(40)
"Hi".center(40,'$')


# mix str and int
# f-string
a=True
b=5
print("the value of a is a and the value of b is b")  #will just show the sentence
print(f"the value of a is {a} and the value of b is {b}") #f & {} make the value shows after =

#formatting strings
print("the value of a is {} and the value of b is {}".format(a,b))  #.format() & {} make the value shows after =



#Variable Names: Rules and Conventions
# naming rules
# 1.cannot use reserved words as a name , e.g. import=1 x will cause error
# 2.avoid certain variable names e.g.build-in function name
x=str(5)
print(x)

str='very bad idea!' # This will kill the build-in function str # "x=str(5)" after str="ver bad idea!" will cause TypeError
del(str) # to bring back the build-in function str
x=str(5)
print(x)

#如果非要用就加一个 _ 在build-in function 后面
str_= 'very bad idea!'
x=str(5)
print(str(5))




#PEP 8 style Guide    recommend read



#each module is a python file contains python code,  end with .py
#package must! contains at least 1 module and 1 file/module called _init_.py



#Exercise
a=56
b=33
h=30.5
print(f'the volume of the box is {a*b*h} cubic centremetres.')
print('the volume of the box is {} cubic centremetres.'.format(a*b*h))



#list
lst=[1,2,3]
print(lst)
print(type(lst))

lst=[1,1.0,'love',True,None] #list can contain any objects
lst=["a",lst] #even other list
print(lst)
print(type(lst))

#empty list
lst=[]
lst=list()
print(lst)

# an emmpty list is not = a list contains 'none'
lst1=[]
lst2=[None]
print(lst1)
print(lst2)
print(lst1==lst2)


#indexing
lst    =    ["a","b","c","d","e","f"] # From left to right  Default start with 0
#             ^   ^   ^   ^   ^   ^
# index       0   1   2   3   4   5
print(lst[0])

lst    =    ["a","b","c","d","e","f"] # From right to left  Default start with -1
#             ^   ^   ^   ^   ^   ^
# index      -6  -5  -4  -3  -2  -1
print(lst[-1])



#slicing
# start index is included, but end index is excluded
lst    =    ["0","1","2","3","4","5"]
#             ^   ^   ^   ^   ^   ^
# index       0   1   2   3   4   5
print(lst[0:4])

lst    =    ["0","1","2","3","4","5"]
#             ^   ^   ^   ^   ^   ^
# index      -6  -5  -4  -3  -2  -1
print(lst[-5:-3])
#总数-第几个就会得到负数位置，e.g.第一个的负数位置是1-6=-5

# if want to include the 1st / last index
lst    =    ["0","1","2","3","4","5"]
print(lst[:6])
print(lst[-6:])

# slicing 不需要考虑超过位数会造成error
lst    =    ["0","1","2","3","4","5"]
print(lst[:12])


#append: 在list最后添加element
lst1=[1]
list.append(lst1,2)  # 法1
print(lst1)

lst1.append(3)  # 法2
print(lst1)

lst = [1, True, None]
print(f"lst is originally {lst}" )
lst.insert(1, "string")       # lst is now [1, "string", True, None]
print(f"After insertion, lst is now {lst}")


#extend：在list后添加另一个list
lst1=[1]
lst2=[2,3]
lst1.extend(lst2) # 法1
print(lst1)

lst3=[4,5]
list.extend(lst1,lst3) # 法2
print(lst1)


#remove: eliminate the 1st object in the list with VALUE in()
lst=[1,2.0,1,'love',True,None]
lst.remove(True)  #True = 1   False = 0
print(lst)

#pop:#eliminate the LAST object in the list with VALUE in()
lst1=[1,'love',2,True,None,True]
lst1.pop(True)
print(lst1)

#clear: remove all elements in the list
lst=[1,2.0,1,'love',True,None,True]
lst.clear()
print(lst)


#reverse: 反转顺序
lst=[1,2,3]
lst.reverse()
print(lst)

#len：know how many items in the list
lst=[1,0.5,'love',True,None]
lst_no=len(lst)
print(lst_no)


#split: split a string into a list, default separator is whitespace
line="welcome to the class"
x=line.split()
print(x)
y=line.split('e',2) #(separator, how many split)
print(y)



#exercise
# Please write a short program to get the email domain name of the following example.
# 'From firstname,surname@unsw.edu.au Tue Oct 06 10:10:12 2020
domain='From firstname,surname@unsw.edu.au Tue Oct 06 10:10:12 2020'
print(domain.split()[1].split('@')[1])



#Tuples
t=(1,'word',True)
print(t[0],t[-1],t[0:])

#packing
tuple=(1,2)
(a,b)=tuple
print('a,b are {},{}'.format(a,b))



#set: remove duplicate object
# empty set
s=set()
#add an object in a set
s.add("A")
s.add("b")
s.add('c')
s.add('c')
print(s)
#remove an object in set
s.remove('c')
print(s)
#test whether an object is in a set
print('A' in s)
print('d' in s)
print('A' not in s)
print('d' not in s)
#test how many items in a set
print(len(s))



#dictionaries
#key:value
prc_dic={
    '2023.3.1':24,
    '2023.3.2':23
}
print(prc_dic['2023.3.2'])#只会找key

prc_dic['2023.3.1']=25 #有的会被更新
print(prc_dic)

prc_dic['2023.3.3']=24 #没有的就会被加上
print(prc_dic)

prc_dic['2023.3.1']=25


prc_dic.pop('2023.3.3') #删除key
print(prc_dic)

