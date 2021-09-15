import math

def replace_char_at_index(org_str, index, replacement):
    new_str = org_str
    if index < len(org_str):
        new_str = org_str[0:index] + replacement + org_str[index + 1:]
    return new_str

def ipToBinary(ip):
    return ('.'.join([bin(int(x)+256)[3:] for x in ip.split('.')]))

def convert_ipv4(ip):
    return tuple(int(n) for n in ip.split('.'))

def check_ipv4_in(addr, start, end):
    return convert_ipv4(start) < convert_ipv4(addr) < convert_ipv4(end)

def binaryToIp(binary):
    binBezTacke = binary.replace('.','')
    octet = []
    octet.append(int(binBezTacke[0:8], 2))
    octet.append(int(binBezTacke[8:16], 2))
    octet.append(int(binBezTacke[16:24], 2))
    octet.append(int(binBezTacke[24:32], 2))
    return octet

def ipToClass(ip):
    binary = ipToBinary(ip)
    if (binary[0] == '1' and binary[1] == '0'):
        return "Class B"
    if (binary[0] == '1' and binary[1] == '1' and binary[2] == '0'):
        return "Class C"
    if (binary[0] == '1' and binary[1] == '1' and binary[2] == '1' and binary[3] == '0'):
        return "Class D"
    if (binary[0] == '1' and binary[1] == '1' and binary[2] == '1' and binary[3] == '1'):
        return "Class E"
    return "Class A"
    
def networkAndBroadcast(ip, mask):
    binary = ipToBinary(ip)
    binBezTacke = binary.replace('.','')
    maskBezTacke = '0' * 32
    networkBinary = ""
    broadcastBinary = ""
    for i in range(mask):
        maskBezTacke = replace_char_at_index(maskBezTacke, i, '1')
    for i in range(32):
        if maskBezTacke[i] == '1':
            networkBinary += binBezTacke[i]
            broadcastBinary += binBezTacke[i]
        else:
            networkBinary += '0'
            broadcastBinary += '1'
    #print("Mrezna adresa", binaryToIp(networkBinary))
    #print("Emisiona adresa", binaryToIp(broadcastBinary))
    result = dict()
    result["network"] = binaryToIp(networkBinary)
    result["broadcast"] = binaryToIp(broadcastBinary)
    return result

def networkCapacity(ip):
    maxCapacity = '1'*32
    binary = ipToBinary(ip)
    binaryBezTacke = binary.replace('.','')
    return int(maxCapacity,2) - int(binaryBezTacke, 2) - 1

def canBePublic(ip):
    ranges.append(("10.0.0.0", "10.255.255.255"))
    ranges.append(("172.16.0.0", "172.31.255.255"))
    ranges.append(("192.168.0.0","192.168.255.255"))
    result = False
    for _ in ranges :
        if check_ipv4_in(ip, *_) == True:
            result = True
    return result

def sameNetwork(ip1,ip2,mask):
    binary1 = ipToBinary(ip1)
    binary1.replace('.','')
    binary2 = ipToBinary(ip2)
    binary2.replace('.','')
    binaryMask = ipToBinary(mask)
    binaryMask = binaryMask.replace('0','')
    binaryMask = binaryMask.replace('.','')
  #  print(binaryMask)
    onesInMask = len(binaryMask)
   # print(onesInMask)
    mreza1 = binary1[0:onesInMask]
    #print(mreza1)
    mreza2 = binary2[0:onesInMask]
    #print(mreza2)
    #return mreza1 == mreza2
    statistics1 = networkAndBroadcast(ip1, onesInMask)
    statistics2 = networkAndBroadcast(ip2, onesInMask)
    #print("stats1", statistics1, "stats2", statistics2)
    if statistics1["network"] != statistics2["network"]:
        return False
    return True

def addBinary(x,y):
        maxlen = max(len(x), len(y))

        #Normalize lengths
        x = x.zfill(maxlen)
        y = y.zfill(maxlen)

        result = ''
        carry = 0

        for i in range(maxlen-1, -1, -1):
            r = carry
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0

            # r can be 0,1,2,3 (carry + x[i] + y[i])
            # and among these, for r==1 and r==3 you will have result bit = 1
            # for r==2 and r==3 you will have carry = 1

            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1       

        if carry !=0 : result = '1' + result

        return result.zfill(maxlen)

def networkRange(ip, mask, members):
    nb = networkAndBroadcast(ip,mask)
    currentStart = ".".join(map(str,nb["network"]))
    currentStartBinary = ipToBinary(currentStart).replace('.','')
    subnet = 1
    for member in members:
        capacityNeeded = 2 ** int(math.ceil(math.log2(member)))
        currentEndBinary = addBinary(currentStartBinary, "{0:b}".format(capacityNeeded))
        #print("Current End Binary", currentEndBinary)
        currentEnd = binaryToIp(currentEndBinary)
        currentMaskBinary = '1'*(32-int(math.ceil(math.log2(member))))
        currentMaskBinary += '0'*(32-len(currentMaskBinary))
        currentBroadcastBinary = ""
        for i in range(32):
            if currentMaskBinary[i] == '1':
                currentBroadcastBinary += currentStartBinary[i]
            else:
                currentBroadcastBinary += '1'
        #print("Current Start", binaryToIp(currentStartBinary))
        #print("Current mask binary ", currentMaskBinary)
        #print("Current mask", binaryToIp(currentMaskBinary))
        #print("Current broadcast binary", currentBroadcastBinary)
        #print("Current broadcast", binaryToIp(currentBroadcastBinary))
        
        print("Subnet",subnet, "Net.address", ".".join(map(str,binaryToIp(currentStartBinary))),
                                              "Mrezna Maska", ".".join(map(str,binaryToIp(currentMaskBinary))),
                                              "Broadcast addr.", ".".join(map(str,binaryToIp(currentBroadcastBinary))))

        currentStartBinary = addBinary(currentBroadcastBinary, "1")
        subnet+=1

def nivo1(binary):
    print(".".join(map(str,binaryToIp(binary))))

def nivo2(ip):
    print(ipToClass(ip))

def nivo3(ip,mask):
    nb = networkAndBroadcast(ip,mask)
    print("Mrezna adresa", ".".join(map(str,nb["network"])))
    print("Emisiona adresa", ".".join(map(str,nb["broadcast"])))
def nivo4(ip):
    print(networkCapacity(ip))
def nivo6(ip1, ip2, mask):
    if(sameNetwork(ip1,ip2,mask)):
        print("Da")
    else:
        print("Ne")
def nivo7(ip, mask, members):
    networkRange(ip, mask, members)
        
    
                      
    
    
    
    
    
    
