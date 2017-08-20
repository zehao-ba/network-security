import sys
import math
def ReadFile(f_key,f_text,output):
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
    letters=[]
    for line in text_data:
        for l in line.strip():
            letters.append(l)
    ni=math.ceil(len(letters)/float(n))
   
    for i in range(0,int(ni)):
        col=[]
        for j in range(0,n):
            col.append(' ')
        matrix.append(col)
    row=0
    col=0
    #print matrix
    i=0
    col=int(keys[i])-1
    for l in letters:
        #print l
        if row==ni:
            i+=1
            col=int(keys[i])-1
            row=0
     
        matrix[row][col]=l
        row+=1

    Output=open(output,'w')

    #print matrix
    for line in matrix:
        for i in range(0,len(line)):
            Output.write(line[i])
    Output.close()
        
        
        
print "Please input the file that contains key"
f_key = raw_input()
print "Please input the file that contains encrypted text"
f_text = raw_input()
print "Please input the name of output file that contains decrypted text"
f_output = raw_input()
ReadFile(f_key,f_text,f_output)
