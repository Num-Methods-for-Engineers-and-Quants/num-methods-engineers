#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 20:29:34 2026

@author: brice-nelson
"""

# Reading input
a = input('Input a: ')
print(f'a: {a} ', type(a))  # print a and its type

# Evaluate input
b = eval(a)
print(f'b {b}', type(b))  # print b and its type

# Evaluation of strings must be in quotes