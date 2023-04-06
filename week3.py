# list-mutable,ordered: can't modify
# set() can create empty set
# lst[start:stop]
# lst[start:]

# target
# str is not mutable

var1=['a']
var2=['a']
var3=['a']
var4=['a']

lst1=['a']
lst2=['b',lst1]
lst3=['b',['a']]
#not same

lst1=['a']
print(f'This is lst1:{lst1}')

lst2=['b',lst1]
print(f'This is lst2:{lst2}')

lst2[1].append('c')
print(f'This is lst2 after modifying it:{lst2}')


#appending ''')

#python will create multi


#control flow

#if
# if logical_expression:
#     statement_a
#     statement_b
#     ...


happy=False
if happy is True:
    print("I am happy")
print("this will print regardless of the value of happy")


happy=True
if happy is True:
    print("I am happy")
print("this will print regardless of the value of happy")

##
happy=True
very_happy=True

if happy is True:
    print("I am happy")
print("this will print regardless of the value of happy")

happy=5
if happy:
    print("I am happy")

happy=None
if happy:
    print("I am happy")

happy = 1
if happy:
 print("I am happy")#there at least have 1 space before print

#Falsy
# none
# false

#Truthy

#order：not,and,or
# not turns one to another

# value of True is equals to 1
print(1==True)

# print(1 is True)

#is and ==
var1='a'
var2='a'
var3=['a']
var4=['a']

var1 is var2 #identfy  the

var3==var4


a=-1
b=True
if a !=0:
    print("a is non-zero")
elif b is True:
    print("b is True")

    #print only the 1st satisfied sentence


#pass placeholder
happy=True
if happy is True:
    pass


# #my try
# Hours=input("how many hours does you work weekly?")#input generate str
# print(52.45*int(Hours)) #use int/float to cast str to int/float
# if float(Hours)<=35:
#     print(51.45*int(Hours))
# if float(Hours)>35:
#     print(88.46*(int(Hours)-35)+35*51.45)
#
# #standard method
# hours=input("how many hours does you work weekly?")
# hours=float(hours)
# normal_rate=51.45
# overloat_rate=88.9
#
# if hours>35:
#     pass

#loops
# pattern
# anti-pattern

# for<variable> si <iterabel>

letters_1st=["a","b","c","d"]
for letter in letters_1st:
 print(letter)

#split
tic="QAN.AX"
tic_base=tic.lower().split('.')[0]
print(tic_base)
# df.to_csv(f{tic_base}_stk_prec.csv)


# set doesnt allowed duplicate
tickers=set()
tickers.add("QAN.AX")
tickers.add("QAN.AX")
tickers.add("WES.AX")
print(tickers)


d={
    "beauty":True,
    "truth":True,
    "red wheelbarrow":10000,
    5:"fingers"
}
for key in d.values():
    print(d.values)
# lhs is key, rhs is value

#both key and value    use items()
d={
    "beauty":True,
    "truth":True,
    "red wheelbarrow":10000,
    5:"fingers"
}
for key_value_tuple in d.items():
    print(f"key_value_tuple is {key_value_tuple}")


#unpackage
a,b=1,2
#a,b,c=1,2,3,4  ValueError: too many values to unpack (expected 3)



d={
    "beauty":True,
    "truth":True,
    "red wheelbarrow":10000,
    5:"fingers"
}
for key,value in d.items():
    print(f'KEY')
    pass


#range generate sequences
# range(start,stop[,step]) ,  step is optional and default=1
print(range(1,4))

for i in range(0,5):
    print(f"i is now{i}")

for even in range(0,10,2):
    print(f"even is now{even}")


# for i in range(5,0,-1):
#     print(f"This message will self- i is now{i}")

letters=["a","b","c","d"]
i=0
# for x in letters:

#enumerarte
for tup in enumerate(letters):
    print(tup)
for i,x in enumerate(letters):
    print(i,x)

#practice
numbers=[3,9,1,5,7,2,11,0,3,12,3,15]
temp_largest=numbers[0]
print('before',temp_largest)
for number in numbers:
    if number>temp_largest:
        temp_largest=number
    print(number,temp_largest)
print(f'The largest value is {temp_largest}')

#  nested structures
# for outer_

#may nest"for" and "while" loops interchangeably as necessary


#white a nested for loop to print out all distinct pairs of integers made up of integers<=3
for i in range(1,4):
    for j in range(1,4):
         if i <= j:
             print(i,j)

#continue and break
#continue statement stop a loop
sum_of_evens = 0
for i in range(1,101):
    if i & 2==1:
        continue #skip, anything behind this wont be executed
    print(f'')

#break
#asa saw a break the loop finish

for even in range(0,10,2):
    print(even)
    if even>2:
        break

for odd in range(1,10,2):
    for even in range(0,10,2):
        if even > 2:
            break
    print(even,odd)




for even in range(0, 10, 2):
   print(even)
   if even > 2:
        continue

for even in range(0, 10, 2):
        if even > 2:
            continue
        print(even)

for even in range(0, 10, 2):
    if even > 2:
        continue
print(even)


# pass
# continue
# break
