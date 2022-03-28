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
    def __init__(self,content,parent,l,c,is_tag=True):
        contents=content.split(' ')
        self.atrr=contents
        self.name=contents[0]
        self.parent=parent
        self.children=[]
        if(is_tag==True):
            if(contents[0][0]=='/'):
                self.t_type=1
                self.name=str(self.name[1:])
            elif(contents[0][-1]=='/' or contents[0][-1]=='?'):
                self.t_type=2
            elif(contents[0][0]=='?' or contents[0][0]=='!'):
                self.t_type=2
            else:
                self.t_type=0
        else:
            self.t_type=5
        self.l=l
        self.c=c
    def show_map(self):
        tmp=self
        while(tmp.parent.name!="root"):
            print(tmp.name)
            tmp=tmp.parent
    def export(self):
        # single tab
        # open and clode without value
        # open and close with value
        # open and close with children
        if(self.t_type==2):
            return self.name+'\n'
        elif(self.t_type==0 and len(self.children)<2):
            return self.name+'\n'
        elif(self.t_type==0 and len(self.children)==2):
            return self.name + ":"+self.children[0].export()+"\n"
        elif(self.t_type==5):
            return ' '.join(self.atrr)
        else:
            tmp=''
            for i in self.children:
                if(i.name!=self.name):
                   tmp+=i.export()
            return tmp
class extractor:

    def __init__(self,filename):
        self.slist=[]
        self.elist=[]
        self.tags_list=[]

        self.root=tag("root",0,0,0)
        self.filename=filename
        self.fp=open(self.filename,"rb")
        self.log=open(self.filename+"__result.txt","w")
        self.log.close()
        self.extract_tags()
        self.pairing()
        self.search_results=[]
        self.filter_result=[]
    def extract_tags(self):
        print("Extracting "+self.filename+" ...")
        s=""
        l=1
        r=0
        while(1):
            c=self.fp.read(1)
            loc=self.fp.tell()
            
            if(c==b'<'):
                if(len(s)>0):
                    self.tags_list.append(tag(s,self.root,l,r-len(s),False))
                s=""
                self.slist.append(loc)
            elif(c==b'>'):
                if(len(s)>0):
                    self.tags_list.append(tag(s,self.root,l,r-len(s),True))
                s=""
                self.elist.append(loc)
            elif((c==b' ' and len(s)==0) or c==b'\r' or c==b'\t'):
                pass
            elif(c==b'\n'):
                l+=1
                r=0
            else:
                try :
                    s+=c.decode('utf-8')
                except :
                    pass
                    #print("decode error -> ("+str(l)+","+str(r)+")")
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
                    self.open_list.pop()
        print("Pairing Completed")
        
    def search(self,search_key):
        print("Searching "+search_key+"..")
        #self.search_results=[]
        tmp_result=[]
        for i in self.tags_list:
            if(i.name==search_key):
                tmp_result.append(i)
        print("Search Finished")
        if(len(tmp_result)>0):
            self.search_results.append([search_key,tmp_result])
        print("Added to Search Results")
    
    def filter_search(self,search_key,tag_name,list_value):
        tmp_result=[]
        for results in self.search_results:
            if(search_key==results[0]):
                # results[0] = the key to search
                # results[1] = the tags
                for result in results[1]:
                    for spec_tag in result.children:
                        if(spec_tag.name==tag_name and len(spec_tag.children)==2):
                            #simple open clode with one child
                            if(spec_tag.children[0].name in list_value):
                                # result element is filterd tag
                                tmp_result.append(result)
            self.filter_result.append([search_key,tmp_result])
                
    def search_out(self,search_key=""):
        print("Writing Search Resuts of "+search_key)
        if(search_key!=""):
            for results in self.search_results:
                if(results[0]==search_key and len(results[1])>0):
                    self.log=open(self.filename+"__result.txt","a")
                    len_res=str(len(results[1]))
                    idx=0
                    for result in results[1]:
                        idx+=1
                        self.log.write("Result for "+search_key+" -- "+str(idx) + " of "+ len_res+" -- \n")
                        self.log.write(result.export())
                        self.log.write("-- -- -- -- -- -- -- -- -- -- \n")
                    self.log.close()
        print("Writing Search Completed")
    def search_out_all(self):
        for results in self.search_results:
            self.search_out(results[0])
    def filter_search_out(self):
        print("Writing Search Resuts")
        if(len(self.filter_result)>0):
            self.log=open(self.filename+"__result.txt","a")
            for results in self.filter_result:
                len_res=str(len(results[1]))
                idx=0
                for result in results[1]:        
                    idx+=1
                    self.log.write("Result filterd for "+results[0]+" -- "+str(idx) + " of "+ len_res+" -- \n")
                    
                    head=""
                    head+="location : ("+str(result.l)+","+str(result.c)+")\n"
                    head+=result.export()
                    
                    self.log.write(head)
                    self.log.write("-- -- -- -- -- -- -- -- -- -- \n")
            self.log.close()
        print("Writing Search Completed")
        
data=extractor("MyECU.ecuc.arxml.txt")
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
data.search("ECUC-CONTAINER-VALUE")

data.search_out_all()
#short_list=["2111","2112"]
#data.filter_search("feeds","id",short_list)
#data.filter_search_out()
# value_tags=[]
# for i in data.tags_list:
#     if(i.t_type!=0):
#         value_tags.append(i)
#<SW-SYSTEMCONST-REF>
