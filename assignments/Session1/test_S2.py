# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 10:40:06 2017

@author: vovardr
"""
import pytest
import S1_algotools as algo
#test
'''def inc(x):
    return x+1

def test_answer():
    assert inc(3)==5
'''    
def test_average_above_zero_listPositive():
    myList = [1,2,3]
    assert algo.average_above_zero(myList)==2

def test_average_above_zero_listNegative():
    myList = [-1,-2,-3]
    with pytest.raises(ZeroDivisionError) :
        algo.average_above_zero(myList)

def test_average_above_zero_listEmpty():
    myList = []
    with pytest.raises(ValueError) :
       algo.average_above_zero(myList)


def test_max_value_listPositive():
    input_list=[1,2,3]
    assert algo.max_value(input_list)==3

def test_max_value_listNegativ():
    input_list=[-1,-2,-3]
    assert algo.max_value(input_list)==-1
  
def test_max_value_listNul():
    input_list=[0,0,0]
    assert algo.max_value(input_list)==0

def test_max_value_listAlea():
    input_list=[-1,0,5]
    assert algo.max_value(input_list)==5

def test_max_value_listFloat():
    input_list=[-1,0.5,5.6]
    assert algo.max_value(input_list)==5.6
    
def test_max_value_listEmpty():
    input_list = []
    with pytest.raises(ValueError) :
        algo.max_value(input_list)

def test_reverse_table():
    input_list =[1,2,3,4,5]
    assert algo.reverse_table(input_list)==[5,4,3,2,1]
def test_reverse_table2():
    input_list =[1,'b',3,'c',5]
    assert algo.reverse_table(input_list)==[5,'c',3,'b',1]    
def test_reverse_table3():
    input_list =[]
    assert algo.reverse_table(input_list)==[]   
def test_reverse_table4():
    input_list =[1,'' ,2,3]
    assert algo.reverse_table(input_list)==[3,2, '',1]       
    
import numpy
def test_roi_bbox_empty():
    size_rows=10
    size_cols=10
    myMat2=numpy.zeros([size_rows, size_cols], dtype=int)
    bbox_coordonee=numpy.zeros([4, 2], dtype=int)
    bbox_coordonee[0,:]=numpy.array([10, 10])
    bbox_coordonee[1,:]=numpy.array([10, 0])
    bbox_coordonee[2,:]=numpy.array([0, 10])
    bbox_coordonee[3,:]=numpy.array([0, 0])
    assert numpy.all(algo.roi_bbox(myMat2) == bbox_coordonee)

def test_roi_bbox_1():
    size_rows=10
    size_cols=10
    myMat=numpy.zeros([size_rows, size_cols], dtype=int)
    myMat[1,3]=1
    assert numpy.all(algo.roi_bbox(myMat) == [[1, 3],[1, 3],[1 ,3],[1, 3]])
    
def test_roi_bbox_2():
    size_rows=10
    size_cols=10
    myMat=numpy.zeros([size_rows, size_cols], dtype=int)
    for row in range(5,8):
        for col in range(7,9):
            myMat[row,col]=1
    assert numpy.all(algo.roi_bbox(myMat) == [[5, 7],[5, 8],[7, 7],[7, 8]])
    

def test_random_fill_sparse():
    size_rows=2
    size_cols=5
    myTab=numpy.zeros([size_rows, size_cols], dtype=str)
    v=size_rows*size_cols
    vfill=algo.alea(v)
    result=numpy.sum(algo.random_fill_sparse(myTab, vfill)=='X')
    assert result==vfill
    
def test_remove_whitespace():
    chaine="hello world"
    assert algo.remove_whitespace(chaine)=="helloworld"

def test_remove_whitespace2():
    chaine="1 2 3 4"
    assert algo.remove_whitespace(chaine)=="1234"

def test_remove_whitespace3():
    chaine=[1,2,3]
    with pytest.raises(TypeError) :
        algo.remove_whitespace(chaine)

import copy
def test_shuffle():
    liste=[1,2,3,4]
    liste_before=copy.deepcopy(liste)
    liste_after=algo.shuffle(liste)
    assert sorted(liste_before)==sorted(liste_after)

def test_shuffle2():
    liste='abcd'
    with pytest.raises(TypeError) :
        algo.shuffle(liste)   