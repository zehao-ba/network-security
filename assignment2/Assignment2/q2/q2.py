import sys

def readACL(filename):
    try:
        raw_data = open(filename)
    except Exception:
        sys.exit("\nThe file contains ACL cannot be opened!ERROR!\n")
    acls={}
    interfaces={}
    interface_name="";
    for line in raw_data:
        items=line.split()
        #print items
        if items[0]=='access-list':
            if items[1] not in acls.keys():
                acls[items[1]]=[]
            acls[items[1]].append(items[2:])

        if items[0]=='interface':
           interface_name=items[1]
           if items[1] not in interfaces.keys():
                interfaces[items[1]]=[]
        if items[0]=='ip':
            interfaces[interface_name].append(items[2:])
    return acls,interfaces


def readP(filename):
    try:
        raw_data = open(filename)
    except Exception:
        sys.exit("\nThe file contains ACL cannot be opened!ERROR!\n")
    packets=[]
    for line in raw_data:
        items=line.split()
        packets.append(items)   
    return packets
def maxnum(a,b):
    numc=""
    numd=""
    numa='{0:08b}'.format(int(a))
    numb='{0:08b}'.format(int(b))
   # print a
    #print b
    #print numa
    #print numb
    for i in range(0,8):
        if numa[i]=='1':
            numc+='1'
            numd+='0'
        else:
            numc+=numb[i]
            numd+=numb[i]
    
    return int(numd,2),int(numc,2)

def addrCheck(wild,src,srcadd):
    #print wild
    #print src
    for i in range(0,4):
        num = int(wild[i])
        if num==0 and src[i]!=srcadd[i]:
            return False
        elif num==0 and src[i]==srcadd[i]:
            continue
        elif num==255:
            continue
        else:
            minrange,maxrange=maxnum(num,src[i])
            #print "minirange ",minrange
            #print "maxrange ",maxrange
            #print "srcadd ",srcadd[i]
            if int(srcadd[i])>=minrange and int(srcadd[i])<=maxrange:
                continue
            else:
                #print "Wilde does not match"
                return False
    return True
    
def aclmatch(packet,acl):
    srcadd=""
    destadd=""
    srcport=""
    destport=""
    if  len(packet)==2:
        srcadd=packet[0].split('.')
        destadd=packet[1].split('.')
    if  len(packet)==4:
        srcadd=packet[0].split('.')
        destadd=packet[2].split('.')
        srcport=packet[1]
        destport=packet[3]
    
    if len(acl)<4:
        pd=acl[0]
        if pd=='deny':
            pd='denied'
        else:
            pd='accepted'
        src=acl[1].split('.')
        wild=acl[2].split('.')
        if addrCheck(wild,src,srcadd):
            print packet," ",pd,'\n'
            return True

    if len(acl)>=4:
        port=[]
        pd=acl[0]
        if pd=='deny':
            pd='denied'
        else:
            pd='accepted'
    
        protocol=acl[1]
        src=acl[2].split('.')
        wildsrc=acl[3].split('.')
        dest=acl[4].split('.')
        wilddest=acl[5].split('.')
        if len(acl)>6:
            for ind in range(6,len(acl)):
                port.append(acl[ind])
      
        if addrCheck(wildsrc,src,srcadd) and addrCheck(wilddest,dest,destadd):
            
            if  len(port) != 0:
                for ind in range(0,len(port)):
                    if destport == port[ind]:
                         print packet," ",pd,'\n'
                         return True
                return False
            else:
                
                print packet," ",pd,'\n'
                return True 
               
    return False            
                                
            
def process(acls,interfaces,packets):
   
    for packet in packets:# Go over all packets
        for key in interfaces.keys():
            acl_nums = interfaces[key]
            for i in range(0,len(acl_nums)):
                acl_key = acl_nums[i][0]
                inout = acl_nums[i][1]
                acl = acls[acl_key]
                found = False
                for  j in range(0,len(acl)):
                    if aclmatch(packet,acl[j]):
                        found = True
                    if found:
                        break
            if not found:
                print packet," denied",'\n' 
            #whether extent ot standard  
            
print "Please input the name of the file that contains ACL"
f_acl = raw_input()
acls,interfaces = readACL(f_acl)
#print interfaces
#print acls
print "Please input the name of hte file that contains packets"
f_pac=raw_input()
packets = readP(f_pac)
#print packets
process(acls,interfaces,packets)
