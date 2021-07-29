class tag:
	name=""
	atrr=[]
	l=0
	c=0
	t_type=0
	def __init__(self,inner,parent,l,c,f_type=0):
		cont=inner.split(' ')
		self.atrr=cont
		self.name=cont[0]
		self.parent=parent
		if(cont[0][0]=='/'):
			self.t_type=1
		elif(cont[0][-1]=='/' or cont[0][-1]=='?'):
			self.t_type=2
		elif(f_type!=0):
			self.t_type=f_type
		self.parent=parent
		self.l=l
		self.c=c
		

class extractor:
	root=tag("root",0,0,0)
	filename=""
	slist=[]
	elist=[]
	taglist=[]
	pairs=[]
	atr_list=[]
	stag=[]
	def __init__(self,filename):
		#print("init")
		self.filename=filename
		self.fp=open(self.filename,"r")
		self.fout=open(self.filename+"out.txt","w")
	def extract_tags(self):
		s=""
		l=0
		r=0
		while(1):
			c=self.fp.read(1)
			loc=self.fp.tell()
			
			if(c=='<'):
				if(len(s)>0):
					self.stag.append(tag(s,self.root,l,r,5))
				s=""
				self.slist.append(loc)
			elif(c=='>'):
				if(len(s)>0):
					self.stag.append(tag(s,self.root,l,r))
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
		# for i in range(len(self.slist)):
		# 	self.fp.seek(self.slist[i])
		# 	tag_str=self.fp.read(self.elist[i]-self.slist[i]-1)
		# 	self.taglist.append(tag_str)
		# 	self.stag.append(tag(tag_str,"nill"))
	
	def pairing(self,start,end,parent):
		for st in range(start,end):
			for ed in range(st,end):
				if(b'/'+self.taglist[st]==self.taglist[ed]):
					self.pairs.append((st,ed,self.taglist[st],parent))
					self.pairing(st+1,ed-1,self.taglist[st])
					break
			st=ed+1
		#print(self.atr_list)
	def out(self,index=0):
		if(index==0):
			for i in range(len(self.taglist)):
				self.atr_list.append(tag(self.taglist[i]))
				#self.fout.writelines(self.atr_list[i].atrr+b'\n')
				self.fout.write("--> TAG "+self.taglist[i]+"\n")
				for j in range(len(self.atr_list[i].atrr)):
					self.fout.writelines(self.atr_list[i].atrr[j]+b'\n')
				#self.fout.write(self.taglist[i]+b'\n')
				
		elif(index==1):
			for i in range(len(self.pairs)):
				self.fout.write("["+str(self.pairs[i][0])+","+str(self.pairs[i][1])+"]"+str(self.pairs[i][2])+" -> "+str(self.pairs[i][3])+b'\n')
