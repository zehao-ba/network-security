
#standard
def readPacket():
    file = open('packet.txt')
    packet = []
    line = file.readline()
    while line:
        line = line.strip('\n')
        p_list = line.split(' ')
        packet.append(p_list)
        line = file.readline()
    file.close()
    return packet

def readStdACL():
    file = open('ACL.txt')
    acl = []
    interface = []
##    ip = []
    line = file.readline()
    while line:
        StdACL_list = line.strip()
        if StdACL_list[0] == 'access-list':
            acl.append(StdACL_list)
        if StdACL_list[0] == 'interface':
            interface.append(StdACL_list)
#        acl.append(acl_list)
        line = file.readline()
##        StdACL_list = line.strip('\n')
##        #StdACL_list = line.strip('')
##        if StdACL_list[0] == "access-list":
##            acl.append(StdACL_list)
##        if StdACL_list[0] == "interface":
##            interface.append(StdACL_list)
##        if StdACL_list[0] == "ip":
##            ip.append(StdACL_list)
    file.close()
    return acl,interface

def Computation(mask, src):
    address1 = []
    address1 = mask.split('.')
    #print "address1",address1

    '''
    int_address1 = []
    for num in address1:
        int_address1 = int(num)
        print "int address1", int_address1, type(int_address1)
        int_address1.append(int_address1)
        print "int_address1", int_address1 '''

    address2 = []
    address2 = src.split('.')
    '''
    int_address2 = []
    for num in address2:
        int_address2 = int(num)
        int_address2.append(int_address2)
        print "int_address2", int_address2 '''

    result = []
    for i in range (0,4):
        a = address1[i]
        b = address2[i]
        if a == '0':
            result.append(b)
        elif a == '255':
            b = '255'
            result.append(b)
        #print "list result a", a
        #print "list result b", b
    return result
    #print "src and mask result is", result

def compare(dest_1,dest_2): #dest_1 is result, dest_2 is packet's src
    dest2_list = dest_2.split('.')
    #print "dest_1", type(dest_1[0])
    #print "dest_2", type(dest2_list[0])
    for i in range(0,4):
        if int(dest_1[i]) == 255 & int(dest2_list[i]) <= 255:   #mask includes 255
            return True
        elif int(dest_1[i]) == int(dest2_list[i]):  #mask is 0.0.0.0 
            return True
    return False

def check(acl, packets):
    for packet in packets:
        source = packet[0]
        destination = packet[1]
        print "packet ", packet
        for item in acl:
            print "item",item
            #print "type",type(acl)
            #item = acl.strip('')
            #print "source",source
            command = item[2]
            #print "command", command
            #source = item[3]
            #print "source", source
            mask = item[4]
            #print "mask", mask
            dest_match = False
            result = Computation(mask, source)
            print "result",result
            if(compare(result, source)):
                dest_match = True
                print source, destination, "is", command
            else:
                continue
            if(not dest_match):
                print source, destination, "is discard"
             
        
    
            
 
if __name__ == "__main__":
    acl = readStdACL()
    packets = readPacket()
    check(acl, packets)
