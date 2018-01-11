"""
    python script.py <SRA_ID> <file_no>
"""
import sys
import csv
import pandas as pd
from Bio import Entrez
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')
Entrez.email="user@company.com"
try:
        handle = Entrez.efetch(db="sra", id=sys.argv[1])
        text=handle.readlines() 
        #print type(text)
        text1 = "".join(text)
        soup = BeautifulSoup(text1,'html.parser')
        #print soup.study_title.string
        #print soup.study_abstract.string
        with open('sra_abstracts'+sys.argv[2]+'.csv','a') as csvfile:
            writer = csv.writer(csvfile, delimiter='\t')
            if soup.study_title.string == None and soup.study_abstract.string == None:
                writer.writerow([sys.argv[1], 'None', 'None'])
            elif soup.study_title.string == None and soup.study_abstract.string != None:
                writer.writerow([sys.argv[1], 'None', soup.study_abstract.string])
            elif soup.study_title.string != None and soup.study_abstract.string == None:
                writer.writerow([sys.argv[1], soup.study_title.string,'None']) 
            else:             
                writer.writerow([sys.argv[1], soup.study_title.string, soup.study_abstract.string])            
except:                   
        print "Error getting data"  
