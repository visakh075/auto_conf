#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 19:04:10 2022

@author: erkattiri
"""

from data_extractor import extractor,tag

class ht:
    def __init__(self,tag_name,content,attr=""):
        self.contents=[]
        self.tag=tag_name
        self.attr=attr;
        #if(type(content)=="str"):
        self.contents.append(content)
        
    def add(self,content):
        #if(type(content))
        # dont want to check whether just_text or ht_tag_group
        self.contents.append(content)
    def __add__(self,other):
        self.add(other)
    def html(self):
        data=""
        if(self.attr!=""):    
            data='<'+self.tag+' '+self.attr+'>'
        else:
            data='<'+self.tag+'>'
        for content in self.contents:
            if(isinstance(content, ht)):
                data+=content.html()
            elif(isinstance(content, str)):
                data+=content
        data+='</'+self.tag+'>'
        return(data)

class html_report:
    
    def __init__(self,report_name):
        self.report_name=report_name
        self.head='''
            <head>
            <title>Report</title>
            <link rel="stylesheet" href="mystyle.css"/>
            </head>'''
        #self.head=("html",head)
        self.data=ht("html",self.head)
        self.report_file=open(self.report_name,'w')
        self.tag_list=[]
    
    def gen_report(self):
        
        #genrate html from tag_list
        # addd a coment box below waech tag for the user to give entr
        #
        #
        comment_section=ht("section","","class='comment_box'")
        comment_section+ht("div","visakh sethumadhavan","class='author_name'")
        body=ht("body","")
        entires=ht("section","","class='results'")
        
        for tag_i in self.tag_list:
            box_container=ht("section","","class='box_section'")
            
            box_container+self.tag_to_ht(tag_i)
            box_container+comment_section
            
            entires+box_container
            
        body+entires
        self.data+body
        self.report_file.write(self.data.html())
        self.report_file.flush()
        self.report_file.close()
        
        
    def tag_to_ht(self,tag_e):
        if(isinstance(tag_e,tag)):
            # tag element is instance of tag
            if(len(tag_e.children)==2):    
                tag_html=ht("div","","class='tag_obj single'")
            else:
                tag_html=ht("div","","class='tag_obj'")
            
            if(tag_e.t_type==5):
                tag_html+ht("div",tag_e.name,"class='tag_value'")
            elif(tag_e.t_type==2):
                tag_html+ht("div",tag_e.name,"class='tag_empty'")
            else:
                tag_html+ht("div",tag_e.name,"class='tag_head'")
            
            if(tag_e.t_type==0 and len(tag_e.children)<2):
                #simple open and close only head needed
                #open tag get data from child
                pass
            elif(tag_e.t_type==0 and len(tag_e.children)==2):
                tag_html+self.tag_to_ht(tag_e.children[0])
            elif(tag_e.t_type==0 and len(tag_e.children)>2):
                children_container=ht("div","","class='tag_children'")
                for child in tag_e.children[0:len(tag_e.children)-1]:
                    children_container+ht("div",self.tag_to_ht(child),"class='tag_child'")
                tag_html+children_container    
            #tag_html+self.tag_to_ht(child)
            
                
            return tag_html
            
        
    def add_item(self,tag_e):
        if(isinstance(tag_e,tag)):
            self.tag_list.append(tag_e)
