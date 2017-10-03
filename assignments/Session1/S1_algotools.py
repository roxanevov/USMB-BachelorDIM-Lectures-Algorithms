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
    
    #first_item=input_list[0]
    #init critical variable
    #Som=0
    #N=0
    
    #compute the average of positive elements of a list
    if len(input_list)==0 :
        raise ValueError()
    for item in input_list:
        if item>0:
            positive_values_sum+=item
            positive_values_count+=1
        elif item==0:
            print('This value is not positiv:'+str(item))
        else:
            print('This value is negative:'+str(item))
        if positive_values_count==0:
            raise ZeroDivisionError()
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
    
'''  
#test max_value
mylist=[-1,2,3,4,7]
result=max_value(mylist)
print(result)
'''

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

#exercice4

#matrix processing lib
import numpy

size_rows=10
size_cols=10
myMat=numpy.zeros([size_rows, size_cols], dtype=int)


#set a value in a specific cell
"""myMat[1,3]=1"""

#filling someting in the matrix, the basic way
"""for row in range(5,8):
        for col in range(7,9):
            myMat[¸row,col]=1
"""

#filling someting in the matrix, a nic way
#myMat[2:4,5:9]=1
#myMat[4:7,7:9]=numpy.ones([3,2])
"""print(myMat[8,2])"""

def roi_bbox(myMat):
   ##
   #basic function able to get bounding box
   # @param myMat : the input matrix 
    xmin=size_cols
    xmax=0

    ymin=size_rows
    ymax=0
    #output coordonee matrix
    for y in xrange(size_rows):
        for x in xrange(size_cols):
            if myMat[y,x]==1:
                if xmin>x:
                    xmin=x
                if xmax<x:
                    xmax=x
                if ymin>y:
                    ymin=y
                if ymax<y:
                    ymax=y
                    
    bbox_coordonee=numpy.zeros([4, 2], dtype=int)
    bbox_coordonee[0,:]=numpy.array([ymin, xmin])
    bbox_coordonee[1,:]=numpy.array([ymin, xmax])
    bbox_coordonee[2,:]=numpy.array([ymax, xmin])
    bbox_coordonee[3,:]=numpy.array([ymax, xmax])
    return bbox_coordonee
'''
#test roi_bbox
result=roi_bbox(myMat)
print(result)
'''


#Exercice 5
from random import randint


size_rows=2
size_cols=5
myTab=numpy.chararray([size_rows, size_cols])
myTab[:]=' '

#print myTab
v=size_rows*size_cols

def alea(v) :
    return(randint(0, v));

vfill=alea(v)


def random_fill_sparse(myTab, vfill):
    i=0
    while i<=vfill:
        #lign=alea(myTab.shape[1])
        #col=alea(myTab.shape[0])
        print i
        myTab[alea(myTab.shape[0]-1),alea(myTab.shape[1]-1)] = 'X' 
        i = i + 1
    return myTab

#print random_fill_sparse(myTab,vfill)
        
chaine='salut toi ca va '

def remove_whitespace(chaine):
    i=0
    while i<len(chaine):
        if chaine[i]==" ":
            chaine=chaine[:i]+chaine[i+1:]
        i= i+1
    return chaine
#print remove_whitespace(chaine)

liste=[1,2,3,4]
def shuffle(liste):
    tab=[]
    i = len(liste)
    while len(liste):
        temp = alea(len(liste)-1)
        tab.append(liste[temp])
        liste.pop(temp)
        print len(liste)
    return tab
#print shuffle(liste)

def game(nbPlayer):
    
