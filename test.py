#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 23:26:34 2022

@author: erkattiri
"""

from data_extractor import extractor
from html_gen import html_report
        
# TEST SET 1
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