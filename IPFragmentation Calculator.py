from prettytable import PrettyTable
def frag(d,h,m):
    if d == m :
        print("No fragmentation is required .The router can forward the whole datagram as it is ")
        return
    payload = d-h
    mtupayload = m - h
    l_main = [['No','Length','ID','MF Flag','Offset']]
    offset = mtupayload 
    loopno = payload/mtupayload
    loopno_int = int(loopno)
    if(loopno_int == loopno):
        size = loopno_int
    else :
        size = loopno_int + 1
    d1 = payload
    sr = 0
    for i in range(size-1):
        l = []
        l.append(sr)
        sr = sr + 1 
        l.append(mtupayload)
        l.append('XX')
        l.append('1')
        d1 = d1  - mtupayload
        #print(mtupayload)
        #print(" ",(offset*i)/8)
        l.append(int((offset*i)/8))
        l_main.append(l)
                 
    #print(d1)
    #print(" ",(offset*(size-1))/8)
    l = []
    l.append(sr)
    l.append(d1)
    l.append('XX')
    l.append('0')
    l.append(int((offset*(size-1))/8))
    l_main.append(l)
    print("\nNo of fragemnts needed are : ",size)
    tab = PrettyTable(l_main[0])
    tab.add_rows(l_main[1:])
    for i in tab:
        print("")
        print(i)


datagramsize = int(input("Enter the size of the datagram :"))
headersize = int(input("Enter the size of the IP header :"))
mtu = int(input("Enter the MTU size :"))
frag(datagramsize,headersize,mtu)
