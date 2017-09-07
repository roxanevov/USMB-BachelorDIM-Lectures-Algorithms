# -*- coding: utf-8 -*-

#@autor: Roxane Vovard, LISTIC Lab, IUT Annecy le vieu
#@brief a set of generic functions for data management
"""
# a variable
a=1 #☺default type : int

#an empty list
mylist =[]

#a filled list
mylist2=[1,2,3]

#append to a list
mylist.append(10)

#a buggy list
mybuggylist=[1,'a',"Hi"]

#operatops
b=a+2
mylist_sum=mylist+mylist2
"""

#exerci 1


def average_above_zero(inpu_list):
   
    
    positive_values_sum=0
    positive_values_count=0
    
    first_item=input_list[0]
    #init critical variable
    Som=0
    N=0
    
    #compute the average of positive elements of a list
    for item in input_list:
        if item>0:
            positive_values_sum+=item
            positive_values_count+=1
        elif item==0:
            print('This value is not positiv:'+str(item))
        else:
            print('This value is negative:'+str(item))
    average=float(positive_values_sum)/positive_values_count
    print('Positive elements average is '+str(average))        
    return float(average)
"""
 #the input list
mylist=[1,2,3,4,-7]
result=average_above_zero(mylist)
message='The average of positive samples of{liste_values} is {res}'.format(liste_values=mylist,res=result)
print(message)
"""