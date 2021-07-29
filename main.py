import os
	
''' Search through tags 
	in the list select one and go through the next ones until you find
	a closing tag 
	
	if you find the closing tag selelect the next tag from
	
	
	alg
	start to end
	
	loop1:	for i from start in end+1
		loop2:	for j from i to end +1
				if(tag list i==taglist j)
				{
				found the closing tag
					recurrent[i+1,j-1] including 
				break from loop2
				
				}
		i=j;
		from the next line
	
	'''
	
from extractor_mod import extractor,tag

#m=tag("?xml version=\"1.0\" encoding=\"UTF-8\" ?")
#print(m.atrributes)

s=extractor("sample.xml")
s.extract_tags()
#s.pairing(-1,len(s.taglist),"none")
print(s.stag[10].name)
#s.out(0)

