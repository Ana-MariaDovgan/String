a=input("introdu primul cuvant:")
b=input("introdu al doilea cuvant:")
c=input("introdu al treilea cuvant:")
d=input("introdu al patrulea cuvant:")
if ((len(a)<3) or (len(b)<3) or (len(c)<3) or (len(d)<3)):
    print("Error")
l1=a[:2]
l2=b[0]
l3=c[:3]
l4=d[:(len(d)//2)]
print("Cuvintele: ",a,b,c,d,sep="  ")
print("Cuvantul format",l1+l2+l3+l4)