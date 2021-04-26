X=[14,15,17,15,16,20]; 
Y=[-0.3,-0.8]; 
Y=sorted(Y); 
X=sorted(X); 
total=len(X); 
lista=[]; 
if (total%2==0): 
    total=total//2; 
    mediana=X[total-1]+X[total];
    mediana=mediana/2;  
else: 
    total=total//2; 
    mediana=X[total]; 
n=0; 

print("La mediana es: ", mediana); 
print(Y); 
