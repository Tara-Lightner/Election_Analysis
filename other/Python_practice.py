from tkinter.tix import DirSelectDialog


print('Hello World')



#3.2.5 Lists indexing/slicing, dynamic, mutable # I could not do this section I need help?

counties = ["Arapahoe", "Denver", "Jefferson"]

counties_tuple = ["Arapahoe","Denver","Jefferson"]

for county in counties:
    print (county)



#This is an example of a how to print a generic list
#numbers = [0, 1, 2, 3, 4]
#for num in numbers:
#    print(num)
#Instead of runnng a list, in which you have to type everything in, use a range:
#for num in range(5):
#    print(num)

for i in range(len(counties)):
    print(counties[i])