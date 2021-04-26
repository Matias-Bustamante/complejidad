from timeit import default_timer
inicio=default_timer(); 
X=[13,15,14] 
Y=[16,14,15]

lista=[]; 
for i in range(0,len(X)): 
    lista.append(X[i])
    lista.append(Y[i]);  

lista=sorted(lista); #ordeno la lista de forma creciente

total=len(lista); 
if (total%2)==0: 
    total=total//2; 
    suma=lista[total]+lista[total-1]; 
    suma=suma/2; 
final=default_timer(); 
final=final-inicio; 
print(suma, "Tiempo de ejecucion: %.8f"% final); 
