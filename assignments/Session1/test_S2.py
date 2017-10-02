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
    algo.average_above_zero(myList)==2

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
    algo.max_value(input_list)==3

def test_max_value_listNegativ():
    input_list=[-1,-2,-3]
    algo.max_value(input_list)==0
  
def test_max_value_listNul():
    input_list=[0,0,0]
    algo.max_value(input_list)==-1

def test_max_value_listAlea():
    input_list=[-1,0,5]
    algo.max_value(input_list)==5

def test_max_value_listFloat():
    input_list=[-1,0.5,5.6]
    algo.max_value(input_list)==5
    
def test_max_value_listEmpty():
    input_list = []
    with pytest.raises(ValueError) :
        algo.max_value(input_list)
        
def test_reverse_table():
    input_list = [1,2,3]
    algo.reverse_table==[3,2,1]