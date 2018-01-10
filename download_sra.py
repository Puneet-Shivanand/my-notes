# To run python sra-download.py sra_id               
# Example:  python sra-download.py ERR006600         
import wget               
import sys                
import os
sra_id = sys.argv[1]
url = 'ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/'+ sra_id[:3]+'/'+sra_id[:6]+'/'+sra_id+'/'+sra_id+'.sra'
print (url)
print ("Downloading... please wait!!")
filename = wget.download(url)
if filename:
            print ("\nDownload Complete "+ sra_id)
            print ("\nConverting...")
            cmd = 'fastq-dump '+sra_id+'.sra'
            os.system(cmd)
            print ("\n\n")

