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

def average_above_zero(input_list):
   
    
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


#exercice2

def max_value(input_list):
    ##
    #basic function able to return the max value of a liste
    # @param input_list : the input list to be scanned
    # @throws an exception (ValueError) on an ampty list

    #firs check if provied list is not empty
    if len(input_list)==0:
        raise ValueError('provided list is empty')
    
    #inti max_value    
    max_value=input_list[0]
    max_idx=0
    
    """for item in input_list:
        if max_value<item:
            max_value=item 
    """     
    """    
    #generic style : iterate over the range of liste indexes
    for idx in range(len(input_list)):
        if max_value<input_list[idx]:
            max_value=input_list[idx] 
            max_idx=idx
    """     
    for idx, item in enumerate(input_list):
        if max_value<item:
            max_value=item 
            max_idx=idx
            
    return max_value,max_idx
    
"""   
#test max_value
mylist=[-1,2,3,4,7]
result=max_value(mylist)
print(result)
"""

def reverse_table(input_list):
   ##
   #basic function able to reverse a liste
   # @param input_list : the input list to be scanned

   #init lastIdx
   lastIdx=len(input_list)
  
   for idx in xrange(len(input_list)/2):
       lastIdx-=1
       temp=input_list[idx]
       input_list[idx]=input_list[lastIdx]
       input_list[lastIdx]=temp

   return input_list

"""
#test reverse_table
import copy
mylist=[-1,2,3,4,7]
listSource=copy.deepcopy(mylist)
result=reverse_table(mylist)
message='The reverse of {liste_values} is {res}'.format(liste_values=listSource,res=result)
print(message)
"""



