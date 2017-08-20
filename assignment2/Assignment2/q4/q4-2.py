def ReadFile(f_key,f_text):
    try:
        key_data = open(f_key)
        text_data = open(f_text)
    except Exception:
        sys.exit("\nThe file cannot be opened!ERROR!\n")
    
    keys=[]
    for i in range(0,26):
        letter = chr(65+i)
        if letter !='J':
            keys.append(letter)
    #print keys
    keyMatrix=[[0 for x in range(5)] for x in range(5)] 
    i=0
    j=-1
    
    for line in key_data:
        line = line.strip().replace(' ','')
        for letter in line:
            if letter in keys:
              
                if j>=4:
                    j=0
                    i=i+1
                else:
                    j=j+1
                
     #           print keyMatrix
                keyMatrix[i][j]=letter
            
                keys.remove(letter)
    for letter in keys:
        if j>=4:
            j=0
            i=i+1
        else:
            j=j+1
      
      
        keyMatrix[i][j]=letter
    textpair=[]
    for line in text_data:
        line=line.strip().replace(' ','')
        l = len(line)
        i = 0
      #  print l
        if (l==0):
            continue
        i=0
        while (i<l-1):
            pair = line[i]
        
            if (i+1<l):
                if (line[i+1]==line[i]):
                    pair+='X'
                    i=i+1
                else:
                    pair+=line[i+1]
                    i=i+2
            else:
                pair+='Z'
                i+=1
       #     print pair
            textpair.append(pair)    
    #print textpair    
    #print keyMatrix
    return keyMatrix,textpair


def process(keyMatrix,textpair,output):
    Output=open(output,'w')
    plaintext=""
    preva=""
    prevb=""
    for pair in textpair:
        a=pair[0]
        b=pair[1]
        ai=-1
        aj=-1
        bi=-1
        bj=-1
        na=''
        nb=''
        for i in range(0,5):
            for j in range(0,5):
                if keyMatrix[i][j]==a:
                    ai=i
                    aj=j
                if keyMatrix[i][j]==b:
                    bi=i
                    bj=j
        if ai==bi:
            
            aj=aj-1
            bj=bj-1
            if aj<0:
                aj=4
            if bj<0:
                bj=4
        elif aj==bj:
            ai=ai-1
            bi=bi-1
            if ai<0:
                ai=4
            if bi<0:
                bi=4
        else:
            k=aj
            aj=bj
            bj=k
            
        na=keyMatrix[ai][aj]
        nb=keyMatrix[bi][bj]
        plaintext=plaintext+na+nb
        preva=na
        prevb=nb
    l=len(plaintext)
    
    for i in range(0,l):
        if (i<l-2 and plaintext[i-1]==plaintext[i+1] and plaintext[i]=='X'):
            continue
        Output.write(plaintext[i])
    
            

print "Please input the file that contains key"
f_key = raw_input()
print "Please input the file that contains encrpyted text"
f_text = raw_input()
print "Please input name of the output file that contains decrypted text"
f_output = raw_input()
keyMatrix,texts = ReadFile(f_key,f_text)
process(keyMatrix,texts,f_output)
