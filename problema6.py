c=input("introdu cuvantul: ")
l=input("introdu litera: ")
for i in range(len(c)):
    print(c[:i]+l+c[i+1:])