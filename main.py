from extractor_mod import extractor,tag
from auto_conf import report_genrator
import time

checklist=[
    ['MyECU.ecuc.arxml.txt',[[0,'VARIANT-PRE-COMPILE'],[1,'SHORT-NAME']]],
    ['sample.xml',[[0,'manoj'],[1,'description']]]
    ]

'''checklist=[
    ['sample.xml',[[0,'manoj'],[1,'description']]]
    ]'''
str_search=['tags','sections']

results=[]
for checklist_item in checklist:
    result=[]
    source_name,search_items=checklist_item
    print("starting extraction of "+source_name)
    s_time=time.time()
    s_extractor=extractor(source_name)

    print("finished extraction of "+source_name+" in "+str(time.time()-s_time)+"s")
    
    sc=0
    for search_item in search_items:
        search_type,search_string=search_item
        print(sc)
        print("search "+search_string+" in "+str_search[search_type])
        result.append([search_string,search_type,s_extractor.search_in(search_type, search_string)])
        print("search of "+search_string+" completed ")
        sc+=1
    results.append([source_name,result])
report_genrator(results)
#s=extractor("MyECU.ecuc.arxml.txt")
#print("extraction started")
#s.extract_tags()
#print("end of extraction")
#s.out_stag()
#tags=s.stag
#s.pairing(0,len(s.stag)-1,s.root)
'''
Structure of results

results=result_items
result_items=[result_item]
result_item=[source__name,search_items]
search_items=[search_item]
search_item=[search_string,search_type,findings]
findings=[find]
find= tag or [tag]

'''


root=tag("root",0,0,0)
hirarchy=[]
def tree(results):
    for result_item in results:
        source_name,search_items=result_item
        level=[]
        for search_item in search_items:
            search_string,search_type,findings=search_item
            
            for find in findings:
                chain=[]
                if search_type==0:
                    #find
                    pass
                else:
                    find=find[0]
                while(find.parent!=0):
                    chain=[find]+chain
                    find=find.parent
                level.append(chain)
        print("\n")
        hirarchy.append(level)
        #print(level)
tree(results)
def combine(hirarchy):
    for puzzle1 in hirarchy:
        for puzzle2 in hirarchy:
            if(puzzle1!=puzzle2):
                #conbine
                for link in range(min(len(puzzle1),len(puzzle2))):
                    
        #for piece in puzzle:
combine(hirarchy)           
