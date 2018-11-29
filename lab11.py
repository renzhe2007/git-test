#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:17:24 2018

@author: HFF
"""
import sys
import random

a=sys.argv

def swap(string_list,i,j):
    temp=string_list[i]
    string_list[i]=string_list[j]
    string_list[j]=temp
    return string_list

def shuffle(input_string):
    string_list=list(input_string)
    n=len(input_string)
    for i in range(n):
        j=random.randint(0,n-1)
        string_list=swap(string_list,i,j)
    final_string="".join(string_list)
    return final_string


print(a)
print(shuffle(a[1]))

    
    