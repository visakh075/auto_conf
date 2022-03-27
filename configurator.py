# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 10:40:19 2022

@author: hermit

    '''
    comment on ttype
    
    Value               5
    close               1
    sigle tab or xml    2
    open                0
    '''
"""
class tag:
    def __init__(self,content,parent,l,c,f_type=0):
        contents=content.split(' ')
        self.atrr=contents
        self.name=contents[0]
        self.parent=parent
        self.children=[]
        if(contents[0][0]=='/'):
            self.t_type=1
            self.name=str(self.name[1:])
        elif(contents[0][-1]=='/' or contents[0][-1]=='?'):
            self.t_type=2
        elif(f_type!=0):
            self.t_type=f_type
        else:
            self.t_type=0
        self.l=l
        self.c=c
class extractor:

    def __init__(self,filename):
        self.slist=[]
        self.elist=[]
        self.tags_list=[]
        self.open_list=[]

        self.root=tag("root",0,0,0)
        self.filename=filename
        self.fp=open(self.filename,"r",encoding='UTF8')
        self.fout=open(self.filename+"out.txt","w",encoding='UTF8')
        self.log=open(self.filename+"log.txt","w",encoding='UTF8')

        self.extract_tags()
        self.pairing()
    def extract_tags(self):
        print("Extracting "+self.filename)
        s=""
        l=1
        r=0

        while(1):
            c=self.fp.read(1)
            loc=self.fp.tell()
            
            if(c=='<'):
                if(len(s)>0):
                    self.tags_list.append(tag(s,self.root,l,r-len(s)))
                s=""
                self.slist.append(loc)
            elif(c=='>'):
                if(len(s)>0):
                    self.tags_list.append(tag(s,self.root,l,r-len(s)))
                s=""
                self.elist.append(loc)
            elif(c==' ' and len(s)==0):
                pass
            elif(c=='\n'):
                l+=1
                r=0
            else:
                s+=c
            if not c:
                break
            r+=1
        print("Extraction completed")
    def pairing(self):
        print("Starting Pairing")
        self.open_list=[]
        for tag in self.tags_list:
            if(len(self.open_list)>0):
                tag.parent=self.open_list[-1]
                self.open_list[-1].children.append(tag)
            if(tag.t_type==0):
                self.open_list.append(tag)
            elif(tag.t_type==1):
                if(len(self.open_list)>0 and self.open_list[-1].name==tag.name):
                    #print(tag.name,self.open_list[-1].name)
                    self.open_list.pop()
        print("Pairing Completed")
        
data=extractor("sample.xml")
#
# n=data.open_list
# value_tags=[]
# for i in data.tags_list:
#     if(i.t_type!=0):
#         value_tags.append(i)
        