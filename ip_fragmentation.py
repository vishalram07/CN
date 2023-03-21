import math
def frag(total,mtu):
    if(mtu%8!=0):
        mtu=mtu-(mtu%8)
    n=math.ceil(total/mtu)
    print(n)
    d={"Total_len" : [],'DF' : 1,'MF':[],'Offset':[]}
    l1=[]
    l2=[]
    l3=[]
    for i in range(0,n-1):
        l1.append(mtu+20)
        l2.append(1)
        l3.append(i*mtu//8)
        d["Total_len"]=l1
        d["MF"]=l2
        d["Offset"]=l3
    l1.append(total-(mtu*(n-1))+20)
    l2.append(0)
    l3.append((n-1)*mtu//8)
    d["Total_len"]=l1
    d["MF"]=l2
    d["Offset"]=l3
    for i in range(0,n):
        print("Mtu    : ",d["Total_len"][i])
        print("DF     : ",d["DF"])
        print("MF     : ",d["MF"][i])
        print("Offset : ",d["Offset"][i])
        print("-"*20)
total=5140
mtu1=1500
mtu2=620
print("R1\n")
frag(total-21,mtu1-20)
print("\n\nR2 or R3\n")
frag(mtu1-21,mtu2-20)
