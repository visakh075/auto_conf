
    
class tag:
    '''
    comment on ttype
    
    Value               5
    close               1
    sigle tab or xml    2
    open                0
    '''
    name=""
    atrr=[]
    l=0
    c=0
    t_type=0
    folded=0
    def __init__(self,inner,parent,l,c,f_type=0):
        cont=inner.split(' ')
        self.atrr=cont
        self.name=cont[0]
        self.parent=parent
        if(cont[0][0]=='/'):
            self.t_type=1
            self.name=str(self.name[1:])
        elif(cont[0][-1]=='/' or cont[0][-1]=='?'):
            self.t_type=2
        elif(f_type!=0):
            self.t_type=f_type
        self.parent=parent
        self.l=l
        self.c=c
        self.folded=0

class extractor:
    root=tag("root",0,0,0)
    filename=""
    slist=[]
    elist=[]
    taglist=[]
    pairs=[]
    atr_list=[]
    stag=[]
    result=[]
    def __init__(self,filename):
        #print("init")
        self.filename=filename
        self.fp=open(self.filename,"r",encoding='UTF8')
        self.fout=open(self.filename+"out.txt","w",encoding='UTF8')
        self.log=open(self.filename+"log.txt","w",encoding='UTF8')
        
        #tag extraction
        self.extract_tags()
        #tag pairing
        self.pairing(0, len(self.stag)-1, self.root)
        
    def extract_tags(self):
        s=""
        l=1
        r=0
        while(1):
            c=self.fp.read(1)
            loc=self.fp.tell()
            
            if(c=='<'):
                if(len(s)>0):
                    self.stag.append(tag(s,self.root,l,r-len(s),5))
                s=""
                self.slist.append(loc)
            elif(c=='>'):
                if(len(s)>0):
                    self.stag.append(tag(s,self.root,l,r-len(s)))
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

    def pairing(self,start,end,parent):
        
        i=start
        int_folds=0
        while(i<end):
            if(self.stag[i].t_type==0):
                j=i+1
                #j looping
                while(j<=end):    
                    if(self.stag[i].name==self.stag[j].name and self.stag[j].t_type==0):
                        # same opening tab
                        int_folds+=1
                    if(self.stag[i].name==self.stag[j].name and self.stag[j].t_type==1):
                        if(int_folds>0):int_folds-=1
                        else:
                            self.pairs.append([self.stag[i],self.stag[j],parent])
                            for p_s in range(i+1,j):
                                self.stag[p_s].parent=self.stag[i]
                            self.pairing(i+1, j-1, self.stag[i])
                            i=j
                            break
                    j+=1
            i+=1
       
            # folding normally if start to end is finished
            #for fo in range(start,end+1):
            #    self.stag[fo].folded=1
                
    def out(self,index=0):
        if(index==0):
            for m in self.stag:
                                if(m.t_type==5):
                                        self.fout.write(m.name+"\n")
        elif(index==1):
            for i in range(len(self.pairs)):
                self.fout.write("["+str(self.pairs[i][0])+","+str(self.pairs[i][1])+"]"+str(self.pairs[i][2])+" -> "+str(self.pairs[i][3])+b'\n')
        
    def out_stag(self):
        file=open("stagout.txt","w",encoding="utf-8")
        k=0
        for i in self.stag:
            file.write('<---->\n')
            file.write("index:"+str(k)+"\n")
            k+=1
            file.write("name : "+i.name+"\n")
            file.writelines(i.atrr)
            file.write("\ntype : "+str(i.t_type)+"\n")
            file.write("location : "+str(i.l)+","+str(i.c)+"\n")
        file.close()
        
    def search_tag(self,cont,field=0):
        '''
        name=""
        atrr=[]
        l=0
        c=0
        t_type=0
        '''
        result=[]
        for i in self.stag:
            got=""
            if(field==0):
                got=i.name
            elif(field==1):
                got=i.l
            elif(field==2):
                got=i.c
            elif(field==3):
                got=i.t_type
            
            if(got==cont):
                result.append(i)
        return(result)
    def search_section(self,cont,field=0):
        '''
        name=""
        atrr=[]
        l=0
        c=0
        t_type=0
        '''
        result=[]
        for i in self.pairs:
            got=""
            if(field==0):
                got=i[0].name
            elif(field==1):
                got=i[0].l
            elif(field==2):
                got=i[0].c
            elif(field==3):
                got=i[0].t_type
            
            if(got==cont):
                result.append(i)
        return(result)
    def show_results(self):
        self.fout.flush()
        for i in range(len(self.result)):
            self.fout.write(self.print_root(i)+"\n")
            self.fout.flush()
            
    def print_root(self,index):
        item=(self.result[index][0])
        resultstring=""
        while(item.name!="root"):
            resultstring=(item.name+"("+str(item.l)+","+str(item.c)+")>"+resultstring)
            item=item.parent
        resultstring=item.name+">"+resultstring
        return resultstring
    def close_streams(self):
        self.fp.close()
        self.fout.close()
        self.log.close()
        
    def search_in(self,target,content,field=0):
        '''

        Parameters
        ----------
        target : TYPE
            DESCRIPTION.
        content : TYPE
            DESCRIPTION.
        field : TYPE, optional
            DESCRIPTION. The default is 0.

        Returns
        -------
        None.

        '''
        if(target=="TAG" or target==0):
            return(self.search_tag(content,field))
        elif(target=="SECTION" or target==1):
            return(self.search_section(content,field))
        
        