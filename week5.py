# fy
# fy object: python object let access

# raw bytes
# decoded text

# r for reading, t for text mode

#r: default
#w:writing erases previous content 1st - bytes
#a:writing - appending
#t:text data
#b:binary data

#iterator don't hold


# fobj remain to the end of the file


# series: 2
# data
# index

#
# index is not part of data, but is part of Series object


#list
# dates.index

#array
#ser.array
#ser.index

#Series index are mutable

#DataFrames
#DataFrames constructor: pd.DataFrames(argument)
#think it as labelled collection of series objects
#



# Exercise: print following
#     a   b
# c   1   4
# d   2   5
# e   3   6
import pandas as pd
df=pd.DataFrame(
    {
        'a':[1, 2, 3],
        'b':[4, 5, 6]
    },
    index=['c', 'd', 'e']
)
print(df)


#ensure ur Series and DataFrame objects are sorted bu the index

#assemble ur Series and/or DataFrame

#check: is_monotonic_increasing
#Return True

#default of implacement is F

#convert


