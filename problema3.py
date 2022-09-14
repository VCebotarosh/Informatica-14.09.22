a=int(input())
b=int(input())
c=int(input())
d=int(input())
def adunare_fractii(numa1,numi1,numa2,numi2):
    return (numi2*numa1+numi1*numa2)/(numi1*numi2)
def inmultire_fractii(numa1,numi1,numa2,numi2):
    return (numa1*numa2)/(numi1*numi2)
if (b!=0 and d!=0):    
    print(f"Suma fractiilor este ({a} / {b}) + ({c} / {d}) : {adunare_fractii(a,b,c,d)}")
    print(f"Produsul fractiilor este ({a} / {b}) * ({c} / {d}) : {inmultire_fractii(a,b,c,d)}")
