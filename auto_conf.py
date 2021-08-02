# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 14:52:00 2021

@author: hermit

Integration

manifest file
    input

        
        
report file
    output    

TODO
--> Search Type
checklist=[[item]]

item:
    
    ['file to search',[[search item]]]
    
    search item:
        [type,cont]
        
        
        
        
    ['MyECU.ecuc.arxml.txt',[[0,'VARIANT-PRE-COMPILE'],[1,'SHORT-NAME']]]




"""
def report_genrator(result_list):
    rfile=open("report.html","w",encoding='utf-8')
    rfile.write('<html>')
    for result_item in result_list:
        source_name,search_items=result_item
        
        header='<div id="'+source_name+'">'
        
        rfile.write(header)
        
        genaral_info ='<div id="gen_info">'
        genaral_info+='source name :'+source_name+'<br>'
        genaral_info+='</div>'
        
        rfile.write(genaral_info)
        
        #sc=0
        for search_item in search_items:
            
            search_string,search_type,findings=search_item
            
            s_result_info ='<div id="search_info">'
            s_result_info+='<div>'+search_string+'</div>'
            s_result_info+='<div>found '+str(len(findings))+'</div>'
            
            s_result_info+='<div id="search_findings">'
                    
            for find in findings:
                if(search_type==0):
                    #find is a tag
                    s_result_info+='<div class="finding">'
                    s_result_info+='<div>'+find.name+'</div>'
                    s_result_info+='<div>location :('+str(find.l)+','+str(find.l)+')</div>'
                    s_result_info+='</div>'
                    
                elif(search_type==1):
                    s_result_info+='<div class="finding">'
                    s_result_info+='<div class="finding_name">'+find[0].name+'</div>'
                    s_result_info+='<div>location :('+str(find[0].l)+','+str(find[0].l)+')</div>'
                    s_result_info+='</div>'
                    
            s_result_info+='</div></div>'
            
            rfile.write(s_result_info)
            rfile.flush()
        rfile.write('</div>')
        rfile.flush()
    rfile.write('</html>')
    rfile.flush()
    rfile.close()
    
    
        
        
        
        
        