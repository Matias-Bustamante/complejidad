from  timeit import default_timer; 
inicio=default_timer(); 
X=[13,15,14]; 
X=sorted(X); 
Y=[16,14,15];
Y=sorted(Y); 
if (len(X)==len(Y)): 
    total=len(X)-1; 
    suma=X[total]+Y[0]; 
    suma=suma/2; 
    print(suma); 
final=default_timer(); 
final=final-inicio; 
print("Tiempo de ejecucion: %.8f"% final); 