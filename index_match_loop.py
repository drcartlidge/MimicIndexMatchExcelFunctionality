#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
#----------------------------------------------------------------------------
# Created By  : Matthew Cartlidge, PhD, GISP
# Created Date: 03-01-22
# version ='1.0'
# ---------------------------------------------------------------------------
""" Purpose: Two sample scripts that mimics the functionality of combining
Index and Match functions paired together in an Excel formula."""

# Method 1
items = ['aaa', 111, (4,5), 2.01]  # list of items
tests = [(4,5), 3.14]  # lookup values
for key in tests:  # for each lookup value in list of items loop
    for i in items:  # for each item in list of items
        if i == key:  # if the item matches one of the keys
            print (key, "key found")  # do this function
            break  # break triggered for items that match
    else:  # else loop reached in script only for items that don't match (i.e., didn't initiate the break)
        print(key, " not found")  # function to be performed on items that don't match

# Method 2
for key in tests:
    if key in items:
        print(key, "was found")
    else:
        print(key, "not found")