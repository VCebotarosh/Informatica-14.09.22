def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact*=i
    return fact

m=int(input("M ="))
n=int(input("N ="))
if n>m:
    print(factorial(n)/(factorial(m)*factorial(n-m)))
else:
    print("Nu ati introdus datele corect. Mai incercati")