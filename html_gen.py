#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 19:04:10 2022

@author: erkattiri
"""

class html_log:
    def __init__(self,log_name):
        print("Log initiated")
        self.log_file=open(log_name,"w")
    def __del__(self):
        print("Log Closed")
        self.log_file.close()
    def write(self,string):
        self.log_file.write(string)
        self.log_file.flush()

log_f=log("x.log")
del(log_f)