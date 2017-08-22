def getCipher():
    print "Please choose Caesar(C), Vigenere(V) or Matrix transposition(M) cipher: "
    cipher = raw_input()
    return cipher

def getMode():
    print "Please choose to encrypt(e) or decrypt(d): "
    mode = raw_input()
    return mode

def getPT():
    print "Enter the message: "
    plaintext = raw_input().lower()
    return plaintext

def getSK():
    print "Enter the secret key: "
    secretkey = raw_input()
    return secretkey

def Caesar(plaintext, secretkey, mode):
    #print 'CCCCC'
    secretkey = int(secretkey)
    if mode == 'e':
        secretkey = secretkey
    else:
        secretkey = - secretkey
    c_output = ""
    for item in plaintext:
        pt_num = ord(item)
        en_num = pt_num + secretkey
        if en_num < 123 and en_num > 96:
            c_output += chr(en_num)
        elif en_num > 122:
            en_num = en_num - 26
            en_char = chr(en_num)
            c_output += en_char
        elif en_num < 97:
            en_num = en_num + 26
            en_char = chr(en_num)
            c_output += en_char
    print 'The encrypted output is:', c_output

def Vigenere(plaintext, secretkey, mode):
    #print 'Vvvvv'
    while (len(plaintext) > len(secretkey)):
        secretkey += secretkey
    v_output = ""
    for i in range(len(plaintext)):
        pt_num = ord(plaintext[i])
        if mode == 'e':
            secretkey = secretkey.lower()
            key_num = ord(secretkey[i]) - 97
        else:
            secretkey = secretkey.lower()
            key_num = 97 - ord(secretkey[i])
        en_num = pt_num + key_num
        if en_num < 123 and en_num > 96:
            v_output += chr(en_num)
        elif en_num > 122:
            en_num = en_num - 26
            en_char = chr(en_num)
            v_output += en_char
        elif en_num < 97:
            en_num = en_num + 26
            en_char = chr(en_num)
            v_output += en_char
    print 'The encrypted output is:', v_output

def MatrixTransposition(plaintext, secretkey, mode):
    key_length = len(secretkey)
    PT_length = len(plaintext)
    plaintext = plaintext.replace(" ", "%")
    PT = []
    for item in plaintext:
        PT.append(item)
    if mode == 'e':
        reminder = PT_length % key_length
        while reminder != 0:
            PT.append('%')
            reminder = len(PT) % key_length
        PT_len = len(PT)
        #print 'pt_len', PT_len
        pt_key = PT_len/len(secretkey)
        #print 'pt_key', pt_key
        #print 'PT WITH %: ', PT
        
        group=[[]for i in range(pt_key)]
        #print group
        for j in range(pt_key):
            #print len(group[j])
            while len(group[j]) < len(secretkey):
                group[j].append(PT[0])
                del PT[0]
        #print 'group:', group
        result = []
        for n in range(len(secretkey)):
            for m in range(len(group)):
                result.append(group[m][int(secretkey[n])-1])
        
        final = ""
        for item in result:
            final += ''.join(item)
        print 'The encrypted result is:', final

    if mode == 'd':
        PT_len = len(PT)
        pt_key = PT_len/len(secretkey)
        group=[[]for i in range(pt_key)]
        for j in range(len(secretkey)):
            while len(group[j]) < pt_key:
                group[j].append(PT[0])
                del PT[0]
        #print 'group:', group

        result = []
        for k in range(len(group)):
            for m in range(1, len(secretkey)+1):
                for n in range(len(secretkey)):
                    if int(secretkey[n]) == m:
                        result.append(group[n][k])                    
        #print 'The decrypted result:', result

        final = ""
        for item in result:
            final += ''.join(item)
            final = final.replace('%', ' ')
        print 'The decrypted result is:', final
            
            
cipher = getCipher()
mode = getMode()
plaintext = getPT()
secretkey = getSK()

if cipher == 'C':
    Caesar(plaintext, secretkey, mode)
elif cipher == 'V':
    Vigenere(plaintext, secretkey, mode)
elif cipher == 'M':
    MatrixTransposition(plaintext, secretkey, mode)
