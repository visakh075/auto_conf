#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 23:26:34 2022

@author: erkattiri
"""

from data_extractor import extractor
from html_gen import *
        
#data=extractor("MyECU.ecuc.arxml.txt")
data=extractor("sample.xml")
data.search("feeds")

id_list=[str(x) for x in range(2100,2111)]
data.filter_search("feeds","id",id_list)
data.filter_search_out()


final_report=html_report("final_report.html")
for results in data.filter_result:
    s_key,result_items=results[0],results[1]
    for item in result_items:
        final_report.add_item(item)
k=final_report.data.html()
final_report.gen_report()
l=final_report.data.html()

#
#open_list_str=[]
#open_list_x=[]
#for i in data.open_list:
#    open_list_x.append([i.name,i.l,i.c])    
#log=open("log.txt","w")
#for i in data.tags_list:
#    if(i.t_type==0):    
#        open_list_str.append([i.name,i.l,i.c])
#        log.write(i.name+"("+str(i.l)+","+str(i.c)+")\n")
#log.close()
# define a dictonary to return the values that requires
#data.search("ECUC-CONTAINER-VALUE")
#data.search_out_all()


