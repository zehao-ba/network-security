#Zehao Ba (B00732676)

import sys
def readPacket(filename):
    try:
        file = open(filename)
    except Exception:
        print "The packet input is not correct!"
        sys.exit("\nThe file contains ACL cannot be opened!ERROR!\n")    
    packet = []
    line = file.readline()
    while line:
        line = line.strip('\n')
        #print "packet", line
        p_list = line.split(' ')
        packet.append(p_list)
        line = file.readline()
    file.close()
    return packet

def readStdACL(filename):
    try:
        file = open(filename)
    except Exception:
        print "The ACL input is not correct!"
        sys.exit("\nThe file contains ACL cannot be opened!ERROR!\n") 
    acl = []
    interface = []
    ip = []
    line = file.readline()
    while line:
        line = line.strip('\n')
        acl_list = line.split(' ')
        #print "acl", acl
        #acl_list = line.strip()
        if acl_list[0]=='access-list':
            acl.append(acl_list)
            line = file.readline()
            #print acl_list
        elif acl_list[0]=='interface':
            interface.append(acl_list)
            line = file.readline()
        elif acl_list[0]=='ip':
            ip.append(acl_list)
            line = file.readline()
    file.close()
    return acl
    return interface
    return ip
    

def Computation(mask, src):
    address1 = []
    address1 = mask.split('.')

    address2 = []
    address2 = src.split('.')

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

def compare(dest_1,dest_2): #dest_1 is result, dest_2 is packet's src
    dest2_list = dest_2.split('.')
    #print dest_1
    #print dest2_list
    return_flag = True
    for i in range(0,4):
        if int(dest_1[i]) == 255 and int(dest2_list[i]) <= 255:
            #mask includes 255
            #print "dest_1", dest_1[i]
            #print "dest_2", dest2_list[i]
            return True
        if (int(dest_1[i]) != int(dest2_list[i])):  #mask is 0.0.0.0 
            return False
    return True

def aclLength(acl):
    for item in acl:
        #print item
        if len(item) < 8:
            return True
        else:
            return False

def portCheck(port_1, port_2):
    if (port_1 == port_2) | (port_2 == '80'):
        return True
    else:
        return False

def check(acl, packets):
    std = aclLength(acl)
    #print "std",std
    #Check extend ACL
    if (std == True):
        #print "standard?", std
        for packet in packets:
            found = False
            #print "break here?"
            #print "packet", packet
            for item in acl:
                p_source = packet[0]
                #print "source", p_source
                destination = packet[1]
                #print item
                #print "destination", destination
                command = item[2]
                #print "command", command
                a_source = item[3]
                mask = item[4]
                #print "mask", mask
                result = Computation(mask, a_source)
                #print "result",result
                #print "p_source", p_source
                dest_match = compare(result, p_source)
                #print "match", dest_match
                if(dest_match == True):
                    found = True
                    print p_source, destination, "is", command
                    #print "found", found
                if (found == True):
                    #print "break"
                    break
                if (found == False):
                    #print "not found"
                    continue
            if (found == False):
                if (command == 'deny'):
                    print p_source, destination, "is permit"
                elif (command == 'permit'):
                    print p_source, destination, "is deny"
#Check extend ACL
    if (std == False):
        for packet in packets:
            found = False
            #print "break here?"
            #print "packet", packet
            for item in acl:
                p_source = packet[0]
                #print "source", p_source
                p_destination = packet[1]
                p_port = packet[2]
                #print item
                #print "destination", destination
                command = item[2]
                #print "command", command
                a_source = item[4]
                src_mask = item[5]
                a_dest = item[6]
                dest_mask = item[7]
                a_port = item[9]
                #print "mask", mask
                src_result = Computation(src_mask, a_source)
                src_match = compare(src_result,p_source)
                dest_result = Computation(dest_mask, a_dest)           
                dest_match = compare(dest_result, p_destination)
                port_match = portCheck(p_port, a_port)
                #print "match", dest_match
                if(src_match == True & dest_match == True & port_match == True):
                    found = True
                    print p_source, p_destination, "is", command
                    #print "found", found
                if (found == True):
                    #print "break"
                    break
                if (found == False):
                    #print "not found"
                    continue
            if (found == False):
                if (command == 'deny'):
                    print p_source, p_destination, "is permit"
                elif (command == 'permit'):
                    print p_source, p_destination, "is deny"
               
 
if __name__ == "__main__":
    print "Please input name of ACL file(such as ACL1.txt):"
    aclfile = raw_input()
    acl = readStdACL(aclfile)
    #print interfaces
    #print acls
    print "Please input the name of packets(such as packet1.txt):"
    packetfile=raw_input()
    packets = readPacket(packetfile)
    check(acl,packets)
