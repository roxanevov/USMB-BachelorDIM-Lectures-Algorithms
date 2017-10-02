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

