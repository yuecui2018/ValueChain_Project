#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:49:17 2018

@author: yuecui
"""

from assist_level import assist_level
import pandas as pd



def assist_test():
    testdata = pd.DataFrame([{'indx': "1",'assist_method': 0}, 
                   {'indx': "2",'assist_method': 1},
                   {'indx': "3",'assist_method': 2},
                   {'indx': "4",'assist_method': 3},
                   {'indx': "5",'assist_method': 4},
                   {'indx': "5",'assist_method': 1}])
    
    
    result = assist_level(testdata)
    
    expected = 2
    
    #check expected output 
    assert result == expected
   
    
    



    