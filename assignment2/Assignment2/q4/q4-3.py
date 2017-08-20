import sys
import math
def ReadFile(f_key,f_text):
    try:
        key_data = open(f_key)
        text_data = open(f_text)
    except Exception:
        sys.exit("\nThe file cannot be opened!ERROR!\n")
    for line in key_data:
	 
    	keys=line.split()
    matrix=[]
    col = []
    n=len(keys)
    for line in text_data:
        for l in line.strip():
            if len(col)<n:
                col.append(l)
                continue    
            if len(col)==n:
                matrix.append(col)                
                col=[]
                col.append(l)
                
    matrix.append(col)
    for col in matrix:
        if len(col)<n:
            for i in range(len(col),n):
                col.append(' ')
        

    #print matrix
    #print keys
    return keys,matrix

def process(keys,matrix,output):
    Output=open(output,'w')

 
    for index in keys:
        for i in range(0,len(matrix)):
            Output.write(matrix[i][int(index)-1])
    Output.close()
        
        
        
print "Please input the file that contains key"
f_key = raw_input()
print "Please input the file that contains plain text"
f_text = raw_input()
print "Please input the name of output file that contains encrypted text"
f_output=raw_input()
key,texts = ReadFile(f_key,f_text)
process(key,texts,f_output)
